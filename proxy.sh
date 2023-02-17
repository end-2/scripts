#!/bin/bash

# 원격 호스트 정보
remote_user="remote_username"     # 원격 호스트 사용자 이름
remote_host="remote_hostname"     # 원격 호스트 이름/IP
remote_port="remote_ssh_port"     # 원격 호스트 SSH 포트

# 로컬 호스트 정보
local_port="local_port_number"    # 로컬 호스트 포트 번호

# SSH 터널 설정
ssh -N -L $local_port:localhost:$remote_port $remote_user@$remote_host