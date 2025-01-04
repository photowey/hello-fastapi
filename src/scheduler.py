# -*- coding:utf-8 -*-
"""
main scheduler.
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

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import logger

# ----------------------------------------------------------------


global global_scheduler


# ----------------------------------------------------------------

def init():
    global global_scheduler
    global_scheduler = BackgroundScheduler()


# ----------------------------------------------------------------

def scheduled_task():
    """scheduled task function"""
    logger.info("--- scheduled task ---")


# ----------------------------------------------------------------

# * * * * *
# | | | | |
# | | | | +--- 星期几(0 - 7)(星期天为0和7)
# | | | +----- 月份(1 - 12)
# | | +------- 日期(1 - 31)
# | +--------- 小时(0 - 23)
# +----------- 分钟(0 - 59)
def start():
    """start scheduler"""
    init()

    cron_expr = '0-59/1 * * * *'
    trigger = CronTrigger.from_crontab(cron_expr)
    global_scheduler.add_job(scheduled_task, trigger)

    try:
        logger.info('Start background scheduler with cron[`{0}`]'.format(cron_expr))
        global_scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.error('Received termination signal, shutting down gracefully.')
        global_scheduler.shutdown(wait=False)
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        global_scheduler.shutdown(wait=False)
    finally:
        logger.info('Background scheduler has been shutdown.')


def shutdown():
    """shutdown scheduler"""
    global_scheduler.shutdown()
