FROM php:8.4-fpm-alpine AS base

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

RUN apk add --update --no-cache nano rsync git nginx py-pip shadow libzip libpng libwebp libjpeg-turbo freetype icu \
  && apk add --update --no-cache --virtual=build-dependencies $PHPIZE_DEPS icu-dev libzip-dev libxml2-dev oniguruma-dev libpng-dev libwebp-dev libjpeg-turbo-dev freetype-dev \
  && docker-php-ext-configure gd --with-freetype --with-webp --with-jpeg \
  && docker-php-ext-install -j$(nproc) intl zip pdo pdo_mysql xml mbstring gd \
  && apk del --purge build-dependencies \
  && pip install --break-system-packages supervisor \
  && echo_supervisord_conf > /etc/supervisord.conf \
  && echo -e '[include]\nfiles = /etc/supervisor.d/*.ini' >> /etc/supervisord.conf \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

COPY conf/nginx/default.nginx /etc/nginx/http.d/default.conf
COPY conf/nginx/nginx.nginx /etc/nginx/nginx.conf
COPY conf/php/php-fpm.conf /usr/local/etc/php-fpm.d/zz-www.conf
COPY conf/supervisor/supervisor.conf /etc/supervisor.d/app.ini
COPY entrypoint.sh /entrypoint

ENTRYPOINT ["/entrypoint"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

EXPOSE 80
