#!/usr/bin/env sh

if [ -z "$1" ]; then
  echo "Missing level: major|minor|patch"
  exit 1
fi

if [ ! -e "package.json" ]; then
  echo "File package.json does not exist."
  exit 1
fi

LEVEL=$1
VERSION=$(jq --raw-output '.version' package.json)
NEW_VERSION=$(semver -i $LEVEL $VERSION)

update_version_in_file() {

  if [ -e $2 ]; then
    FILENAME=$(basename -- "$2")
    EXTENSION="${FILENAME##*.}"

    if [ $EXTENSION = "json" ]; then
      CONTENT=$(jq ".version = \"$1\"" $2)
    elif [ $EXTENSION = "xml" ]; then
      CONTENT=$(yq -oy ".widget.+@version = \"$1\"" $2 -o xml)
    fi

    echo "New version in $2: $1"
    echo "$CONTENT" | tee $2
  else
    echo "$2 does not exist."
  fi
}

update_version_in_file $NEW_VERSION "package.json"
update_version_in_file $NEW_VERSION "composer.json"
update_version_in_file $NEW_VERSION "server/composer.json"
update_version_in_file $NEW_VERSION "server/package.json"
update_version_in_file $NEW_VERSION "client/package.json"
update_version_in_file $NEW_VERSION "mobile/package.json"
update_version_in_file $NEW_VERSION "mobile/config.xml"
