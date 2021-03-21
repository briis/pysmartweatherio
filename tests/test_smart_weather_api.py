"""Tests for pysmartweather_io."""

import aiohttp
import pytest

from pysmartweatherio.client import SmartWeather


@pytest.mark.asyncio
async def test_smartweather_creation():
    """Test we can create the object."""

    smw = SmartWeather(
        "20c70eae-e62f-4d3b-b3a4-8586e90f3ac8",
        2777,
        "metric",
        "mps",
        aiohttp.ClientSession(),
    )
    assert smw
