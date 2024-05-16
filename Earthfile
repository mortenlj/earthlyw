VERSION 0.6

FROM alpine:latest

wrapper:
    RUN apk add curl jq --quiet --no-cache
    RUN wget $(curl -s https://api.github.com/repos/mortenlj/earthlyw/releases/latest | jq -r ".assets[] | select(.name | test(\"earthlyw\")) | .browser_download_url")
    RUN chmod a+x earthlyw
    SAVE ARTIFACT earthlyw /earthlyw
