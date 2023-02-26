from pathlib import Path
import subprocess
from subprocess import STDOUT, CalledProcessError
import re

def get_previous_tag(tag_prefix):
    [status, prev_tag] = subprocess.getstatusoutput(
        f'git describe --tags --match={tag_prefix}-* --abbrev=0')

    if status:
        return None

    return prev_tag


def has_source_code_changed(src: Path, prev_tag: str, ignore: str):
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


def get_latest_version(tag_prefix: str):
    [status, tags] = subprocess.getstatusoutput(
        f'git tag --list --sort=taggerdate {tag_prefix}-*')

    if status:
        return None

    return int(
        re.sub(rf'^{tag_prefix}-', '', tags.splitlines()[-1]))


def get_version(src: Path, tag_prefix: str, ignore: str) -> tuple[bool, int]:
    prev_tag = get_previous_tag(tag_prefix)

    if prev_tag:
        if has_source_code_changed(src, prev_tag, ignore) is False:
            version = re.sub(rf'^{tag_prefix}-', '', prev_tag)
            return False, version

    latest_version = get_latest_version(tag_prefix)

    if latest_version:
        new_version = latest_version + 1
    else:
        new_version = 1

    return True, new_version

def set_version(tag_prefix: str, version: int) -> str:
    subprocess.getstatusoutput(f'git tag "{tag_prefix}-{version}"')
    [status, output] = subprocess.getstatusoutput(
        'git push --tags > /dev/null')

    return output if status else ''