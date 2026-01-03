FROM dunglas/frankenphp

ENV SERVER_NAME=:80

RUN install-php-extensions pdo_mysql intl zip \
 && mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

EXPOSE 80
