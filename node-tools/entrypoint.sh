#!/usr/bin/env sh

set -e

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or fallback to 1000
# Idea taken from https://denibertovic.com/posts/handling-permissions-with-docker-volumes/
USER_ID=${LOCAL_USER_ID:-1000}

if [ ! -z $LOCAL_USER_ID ]; then
  echo "Starting with UID : $USER_ID"

  # Fix git not happy with ownership on mac docker "fatal: detected dubious ownership in repository at '/app'"
  # (similar to https://github.com/go-gitea/gitea/issues/19455)
  git config --system --add safe.directory /app

  usermod -u $USER_ID node
  groupmod -g $USER_ID node
fi

exec "$@"
