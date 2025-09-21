FROM ubuntu:24.04

ARG TARGETARCH
ARG LIQUIDSOAP_VERSION="2.3.3"

ADD https://cdn.sgj0.net/assets/liquidsoap_${LIQUIDSOAP_VERSION}_${TARGETARCH}.deb /tmp/liquidsoap.deb

RUN apt update \
  && apt install -yq ffmpeg /tmp/liquidsoap.deb \
  && apt autoclean \
  && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*

CMD ["liquidsoap", "/etc/liquidsoap/radio.liq"]
