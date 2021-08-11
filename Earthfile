FROM alpine:latest

wrapper:
    RUN apk add curl jq --quiet --no-cache
    RUN wget $(curl -s https://api.github.com/repos/mortenlj/earthlyw/releases/latest | jq -r ".assets[] | select(.name | test(\"earthlyw\")) | .browser_download_url")
    RUN chmod a+x earthlyw
    SAVE ARTIFACT earthlyw /earthlyw

project:
    FROM python:3-alpine
    WORKDIR /code
    RUN pip install --use-feature=in-tree-build --upgrade wheel pip setuptools
    COPY setup.py ./
    COPY ibidem ibidem
    RUN pip wheel --wheel-dir=wheels --use-feature=in-tree-build .
    SAVE ARTIFACT wheels /wheels
    SAVE ARTIFACT ./ /src

test:
    FROM +project
    RUN pip install --find-links=wheels --use-feature=in-tree-build .[dev]
    COPY tests tests
    RUN pytest

build:
    FROM +project
    RUN pip install pex
    RUN pex -v --output-file=earthlyw --find-links=wheels -c earthlyw .
    SAVE ARTIFACT earthlyw /earthlyw AS LOCAL ./bin/earthlyw
