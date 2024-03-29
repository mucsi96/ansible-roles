#!/usr/bin/env python3

from pathlib import Path
import sys
root_directory = Path(__file__).parent.parent

sys.path.append(str(root_directory))

from lib.docker_utils import build_and_push_img
from lib.ansible_utils import load_vars

data = load_vars(root_directory / '.ansible/vault_key', root_directory / 'vars/vault.yaml')
docker_username = data['docker_username']
docker_password = data['docker_password']

build_and_push_img(
    src=root_directory / 'demo_app/client',
    docker_context_path=root_directory / 'demo_app/client',
    ignore=['node_modules', 'dist'],
    tag_prefix='demo-app-client',
    image_name='mucsi96/ansible-roles-demo-app-client',
    docker_username=docker_username,
    docker_password=docker_password
)

build_and_push_img(
    src=root_directory / 'demo_app/server/src',
    docker_context_path=root_directory / 'demo_app/server',
    tag_prefix='demo-app-server',
    image_name='mucsi96/ansible-roles-demo-app-server',
    docker_username=docker_username,
    docker_password=docker_password
)

build_and_push_img(
    src=root_directory / 'spring-boot-admin/src',
    docker_context_path=root_directory / 'spring-boot-admin',
    tag_prefix='spring-boot-admin',
    image_name='mucsi96/ansible-roles-spring-boot-admin',
    docker_username=docker_username,
    docker_password=docker_password
)