FROM ubuntu:26.04

RUN apt update \
  && apt install -yq ffmpeg liquidsoap \
  && apt autoclean \
  && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*

CMD ["liquidsoap", "/etc/liquidsoap/radio.liq"]
