FROM dunglas/frankenphp

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer
COPY entrypoint.sh /entrypoint

ENV SERVER_NAME=:80
ENV MAX_REQUESTS=100
ENV COMPOSER_CACHE_DIR=/tmp

RUN install-php-extensions pdo_mysql intl zip

CMD ["--config", "/etc/frankenphp/Caddyfile", "--adapter", "caddyfile"]
ENTRYPOINT ["/entrypoint"]
