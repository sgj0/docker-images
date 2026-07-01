FROM alvrme/alpine-android:android-36.1-jdk21

ARG GRADLE_VERSION=8.14.3

ADD https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip /tmp/gradle-${GRADLE_VERSION}-bin.zip

RUN apk add --update --no-cache rsync nodejs npm jq \
 && npm install --location=global pnpm cordova \
 && mkdir /opt/gradle \
 && unzip -d /opt/gradle /tmp/gradle-${GRADLE_VERSION}-bin.zip \
 && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

ENV ANDROID_SDK_ROOT=/opt/sdk
ENV JAVA_HOME=/usr/lib/jvm/jdk
ENV GRADLE_HOME=/opt/gradle/gradle-${GRADLE_VERSION}
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${GRADLE_HOME}/bin
