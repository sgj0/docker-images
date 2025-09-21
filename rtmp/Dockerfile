FROM alpine

RUN apk add --update --no-cache nginx nginx-mod-rtmp ffmpeg \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

CMD ["/usr/sbin/nginx"]

EXPOSE 80
