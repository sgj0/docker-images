FROM dunglas/frankenphp:alpine AS base

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer
COPY --link --chmod=755 entrypoint.sh /entrypoint
COPY --link Caddyfile /etc/frankenphp/Caddyfile

ENV SERVER_NAME=:80

RUN apk add --update --no-cache shadow git \
  && install-php-extensions pdo_mysql intl zip \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

CMD ["--config", "/etc/frankenphp/Caddyfile"]
ENTRYPOINT ["/entrypoint"]

FROM node:lts-alpine AS node
FROM base AS dev

COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin

RUN npm install --location=global npm pnpm npm-check-updates npm-run-all cordova

RUN mv $PHP_INI_DIR/php.ini-development $PHP_INI_DIR/php.ini

FROM base AS prod

RUN mv $PHP_INI_DIR/php.ini-production $PHP_INI_DIR/php.ini
