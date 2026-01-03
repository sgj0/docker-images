FROM dunglas/frankenphp

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

ENV SERVER_NAME=:80

RUN install-php-extensions pdo_mysql intl zip

EXPOSE 80
