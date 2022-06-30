#!/bin/bash

/usr/local/bin/celery -A application worker --beat -S django -l info
