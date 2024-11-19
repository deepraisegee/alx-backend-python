#!/usr/bin/env python3
"""A python coroutine file"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """perform some calculations"""
    wait_second = random.uniform(0, max_delay)
    await asyncio.sleep(wait_second)
    return wait_second
