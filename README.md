# django-docker-template

Django porject template for docker.

## Usage

```shell

~$ django-admin startproject \
--template https://github.com/tinnguyentg/django-docker-template/archive/master.zip \
--extension py,yaml,conf,example \
--name robots.txt,start.sh \
project  # project name

~$ cd project
~$ docker compose up
```
