#!/usr/bin/env python3
"""Coroutine that collects 10 random numbers using async comprehension."""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collect 10 random numbers from async_generator."""
    return [num async for num in async_generator()]
