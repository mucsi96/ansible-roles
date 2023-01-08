#!/usr/bin/env python3

"""Get source code version using git tags as reference for diff"""

import subprocess
from subprocess import STDOUT, CalledProcessError
import re
from ansible.module_utils.basic import AnsibleModule


def get_previous_tag(tag_prefix):
    """Get git previous tag matching tag prefix"""

    [status, prev_tag] = subprocess.getstatusoutput(
        f'git describe --tags --match={tag_prefix}-* --abbrev=0')

    if status:
        return None

    return prev_tag


def has_source_code_changed(src, prev_tag, ignore):
    """check if source code has changed"""

    try:
        subprocess.check_output(
            f'git diff --quiet HEAD {prev_tag} -- . {ignore}',
            shell=True,
            text=True,
            stderr=STDOUT,
            cwd=src
        )
        return False
    except CalledProcessError:
        return True


def get_latest_version(tag_prefix):
    """Get latest version based on git tags matching tag prefix"""

    [status, tags] = subprocess.getstatusoutput(
        f'git tag --list --sort=taggerdate {tag_prefix}-*')

    if status:
        return None

    return int(
        re.sub(rf'^{tag_prefix}-', '', tags.splitlines()[-1]))


def get_version(src, tag_prefix, ignore):
    """Get version of a source code"""

    prev_tag = get_previous_tag(tag_prefix)

    if prev_tag:
        if has_source_code_changed(src, prev_tag, ignore) is False:
            version = re.sub(rf'^{tag_prefix}-', '', prev_tag)
            return {'changed': False, 'version': version}

    latest_version = get_latest_version(tag_prefix)

    if latest_version:
        new_version = latest_version + 1
    else:
        new_version = 1

    return {'changed': True, 'version': new_version}


def main():
    """ansible module"""

    fields = {
        'src': {'type': 'path', 'required': True},
        'tag_prefix': {'type': 'str', 'required': True},
        'ignore': {'type': 'list', 'elements': 'str', 'default': []}
    }

    module = AnsibleModule(argument_spec=fields)

    result = get_version(**module.params)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
