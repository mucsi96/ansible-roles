#!/usr/bin/env python3

"""Set source code version using git tags"""

import subprocess
from ansible.module_utils.basic import AnsibleModule


def set_version(tag_prefix, version):
    """Set source code version using git tags"""

    subprocess.getstatusoutput(f'git tag "{tag_prefix}-{version}"')
    [status, output] = subprocess.getstatusoutput(
        'git push --tags > /dev/null')

    return output if status else ''


def main():
    """ansible module"""

    fields = {
        'tag_prefix': {'type': 'str', 'required': True},
        'version': {'type': 'int', 'required': True},
    }

    module = AnsibleModule(argument_spec=fields)

    error = set_version(**module.params)

    if error:
        module.fail_json(error)
    else:
        module.exit_json(changed=True)

if __name__ == '__main__':
    main()
