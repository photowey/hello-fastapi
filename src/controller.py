# -*- coding:utf-8 -*-
"""
controller module.
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


from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

import logger
import scheduler


# ----------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info('Fastapi lifespan.startup event.')
    scheduler.start()
    yield
    # Shutdown
    logger.info('Fastapi lifespan.shutdown event.')
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


# ----------------------------------------------------------------

@app.get("/")
async def health():
    logger.info('Receive health-check request.')

    return {"status": "UP"}


# ----------------------------------------------------------------


@app.get("/rpa/start")
async def rpa_start():
    logger.info('Receive rpa start request.')

    return {"code": 200, "message": "RPA started."}


@app.get("/rpa/stop")
async def rpa_stop():
    logger.info('Receive rpa stop request.')

    return {"code": 200, "message": "RPA stopped."}


# ----------------------------------------------------------------


# ----------------------------------------------------------------


@app.on_event("startup")
async def startup_event():
    logger.info('Receive startup event.')
    scheduler.start()


# @app.on_event("shutdown")
async def shutdown_event():
    logger.info('Receive shutdown event.')
    scheduler.shutdown()


# ----------------------------------------------------------------

def start():
    logger.info('Start app on port 12477(HTTP)')
    uvicorn.run(app, host="127.0.0.1", port=12477)
