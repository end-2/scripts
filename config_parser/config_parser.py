import yaml
import json
import configparser
import os
import xml.etree.ElementTree as ET

def parse_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def parse_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def parse_conf_file(file_path):
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(file_path)
    return {section: dict(config[section]) for section in config.sections()}

def parse_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if child:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    return parse_element(root)

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

def parse_file(file_path):
    file_extension = get_file_extension(file_path)

    if file_extension == '.yaml' or file_extension == '.yml':
        return parse_yaml_file(file_path)
    elif file_extension == '.json':
        return parse_json_file(file_path)
    elif file_extension == '.conf':
        return parse_conf_file(file_path)
    elif file_extension == '.xml':
        return parse_xml_file(file_path)
    else:
        raise ValueError('Unsupported file format.')

if __name__ == '__main__':
    file_path = input('Enter the file path: ')
    parsed_data = parse_file(file_path)
    print(parsed_data)