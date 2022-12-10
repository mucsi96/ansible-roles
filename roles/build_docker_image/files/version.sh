#!/bin/bash

if [[ -z "$TAG_PREFIX" ]]
then
    echo "Missing tag_prefix" >&2
    exit 2
fi

tag_prefix=$(echo "$TAG_PREFIX")
ignore=

if [[ ! -z "$IGNORE" ]]
then
    ignore=$(echo "$IGNORE" | tr ',' '\n' | sed "s/^/:(exclude)/" | tr '\n' ' ')
fi

prev_tag=$(git describe --tags --match=$tag_prefix-* --abbrev=0)
if [ $? -eq 0 ]
then
    git diff --quiet HEAD $prev_tag -- . $ignore
    if [ $? -eq 0 ]
    then
        version=$(echo "$prev_tag" | sed "s/^$tag_prefix-//")
        echo "changed="
        echo "version=$version"
        exit 0
    fi
fi

latest_version=$(git tag --list --sort=taggerdate $tag_prefix-* | tail -1 | sed "s/^$tag_prefix-//")
new_version=
if [[ -z "$latest_version" ]]
then
    new_version=1
else
    new_version=$((latest_version + 1))
fi

git tag "$tag_prefix-$new_version"
git push --tags > /dev/null

echo "changed=true"
echo "version=$new_version"