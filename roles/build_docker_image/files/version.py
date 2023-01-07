#!/usr/bin/env python3

"""Get and set source code version using git tags as reference for diff"""

import sys
import argparse
import subprocess
import re

parser = argparse.ArgumentParser(
    description='Get and set source code version',
    epilog='Example: ./version.py --get --tag-prefix client --ignore node_modules --ignore src'
)
sub_parsers = parser.add_subparsers(dest='cmd')

get_parser = sub_parsers.add_parser(
    'get', description='get version of source code')
get_parser.add_argument(
    '--tag-prefix',
    help='prefix of GIT tag',
    required=True
)
get_parser.add_argument(
    '--ignore',
    help='coma separated list of source file patterns to ignore',
    action='append',
    default=[]
)

set_parser = sub_parsers.add_parser(
    'set', description='set version of source code')
set_parser.add_argument(
    '--tag-prefix',
    help='prefix of GIT tag',
    required=True
)
set_parser.add_argument(
    '--version',
    help='verson to set',
    required=True
)

def get_version(tag_prefix, ignore):
    """Get version of a source code"""

    [status, prev_tag] = subprocess.getstatusoutput(
        f'git describe --tags --match={tag_prefix}-* --abbrev=0')

    if status == 0:
        [status, _diff] = subprocess.getstatusoutput(
            f'git diff --quiet HEAD {prev_tag} -- . {ignore}')

        if status == 0:
            version = re.sub(rf'^{tag_prefix}-', '', prev_tag)
            print('changed=')
            print(f'version={version}')
            sys.exit()

    [_status, tags] = subprocess.getstatusoutput(
        f'git tag --list --sort=taggerdate {tag_prefix}-*')

    if tags:
        latest_version = int(
            re.sub(rf'^{tag_prefix}-', '', tags.splitlines()[-1]))
        new_version = latest_version + 1
    else:
        new_version = 1

    print('changed=true')
    print(f'version={new_version}')


def set_version(tag_prefix, version):
    """Set version of source code"""

    subprocess.getstatusoutput(f'git tag "{tag_prefix}-{version}"')
    [status, _output] = subprocess.getstatusoutput(
        'git push --tags > /dev/null')

    sys.exit(status)


args = vars(parser.parse_args())

match args['cmd']:
    case 'get': get_version(args['tag_prefix'], ','.join(args['ignore']))
    case 'set': set_version(args['tag_prefix'], args['version'])
