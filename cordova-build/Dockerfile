FROM alvrme/alpine-android:android-35-jdk21

ADD https://services.gradle.org/distributions/gradle-9.0.0-bin.zip /tmp/gradle-9.0.0-bin.zip

RUN apk add --update --no-cache rsync nodejs npm jq \
 && npm install -g yarn cordova \
 && cordova telemetry off \
 && mkdir /opt/gradle \
 && unzip -d /opt/gradle /tmp/gradle-9.0.0-bin.zip \
 && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

ENV ANDROID_SDK_ROOT=/opt/sdk
ENV JAVA_HOME=/usr/lib/jvm/jdk
ENV GRADLE_HOME=/opt/gradle/gradle-9.0.0
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${GRADLE_HOME}/bin
