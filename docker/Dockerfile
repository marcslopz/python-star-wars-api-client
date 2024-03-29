FROM python:3.9-slim-buster

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl \
  make \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /tmp/python_star_wars_api_client
COPY . ./tmp/python_star_wars_api_client/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then cd /tmp/python_star_wars_api_client && poetry install --no-root ; else cd /tmp/python_star_wars_api_client && poetry install --no-root --no-dev ; fi"

RUN pip install /tmp/python_star_wars_api_client/
RUN rm -rf /tmp/python_star_wars_api_client/

RUN mkdir -p /workspace

# create user in the image mirroring the host user to avoid using root (and also avoid writing as root in host volumes)
ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

WORKDIR /workspace

CMD ["python-star-wars-api-client"]
