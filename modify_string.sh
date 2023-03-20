#!/bin/bash

# 파일 경로
file_path="file.txt"

# 변경 전 문자열
old_string="old_string"

# 변경 후 문자열
new_string="new_string"

# 파일 내용 치환
sed -i "s/${old_string}/${new_string}/g" ${file_path}
