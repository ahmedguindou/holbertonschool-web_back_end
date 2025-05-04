#!/usr/bin/env python3
"""Module containing an asynchronous comprehension function"""

from typing import List
async_generator = __import__('0-async_generator').async_generator
"""Module containing an asynchronous comprehension function"""


async def async_comprehension() -> List[float]:
    return [x async for x in async_generator()]
