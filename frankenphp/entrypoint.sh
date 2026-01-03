#!/usr/bin/env sh

set -e

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or fallback to 1000
# Idea taken from https://denibertovic.com/posts/handling-permissions-with-docker-volumes/
USER_ID=${LOCAL_USER_ID:-1000}

if [ $USER_ID -eq 0 ]; then # for windows with WSL
  echo "Starting as root"

  # Set php-fpm user to root
  sed -i "s/user = www-data/user = root/g" /usr/local/etc/php-fpm.d/zz-www.conf
  sed -i "s/group = www-data/user = root/g" /usr/local/etc/php-fpm.d/zz-www.conf
else
  echo "Starting with UID : $USER_ID"

  # Fix git not happy with ownership on mac docker "fatal: detected dubious ownership in repository at '/app'"
  # (similar to https://github.com/go-gitea/gitea/issues/19455)
  # git config --system --add safe.directory /var/www/html

  usermod -u $USER_ID www-data
  groupmod -g $USER_ID www-data
fi

exec "$@"
