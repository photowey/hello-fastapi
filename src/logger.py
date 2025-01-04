# -*- coding:utf-8 -*-
"""
logger module.
"""

#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


# ----------------------------------------------------------------

import logging

# ----------------------------------------------------------------

logging.basicConfig(
    filename='hello_fastapi.log',
    filemode='a',
    format='%(asctime)s %(name)s [%(threadName)s] %(levelname)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    encoding='utf-8'
)

logger = logging.getLogger('hello_fastapi')


# ----------------------------------------------------------------

def on_init():
    logger.info('Finished init logger')


# ----------------------------------------------------------------


def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)


def fatal(msg, *args, **kwargs):
    logger.fatal(msg, *args, **kwargs)
