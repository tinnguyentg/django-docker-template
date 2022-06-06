FROM python:3.10.4-alpine as BUILDER

WORKDIR /build

RUN pip install --upgrade pip
RUN pip install --upgrade wheel
COPY requirements ./requirements
ARG DJANGO_ENV
RUN pip wheel --wheel-dir /build/wheels -r requirements/${DJANGO_ENV}.txt

###################################
# Build the docker image
###################################

FROM python:3.10.4-alpine as RUNNER

WORKDIR /app

# Install gettext
RUN apk add --no-cache gettext

COPY --from=BUILDER /build/wheels /wheels
COPY --from=BUILDER /build/requirements .

RUN pip install --no-index /wheels/*

COPY ./start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY . .
