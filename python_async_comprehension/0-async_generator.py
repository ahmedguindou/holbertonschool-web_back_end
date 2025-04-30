#!/usr/bin/env python3
"""Module for async_generator coroutine."""

import asyncio
import random


async def async_generator():
    """Yield a random float between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
