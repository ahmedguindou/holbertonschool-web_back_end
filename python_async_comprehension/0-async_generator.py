#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields
random floats between 0 and 10, with a 1-second delay.
"""

import asyncio
import random

async def async_generator():
    """
    Yield a random float between 0 and 10, 10 times, with a 1-second delay each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
