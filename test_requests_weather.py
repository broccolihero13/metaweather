import pytest
import timeit
from request_weather import get_weather_data

locations = ['2487610', '2442047', '2366355', '2487956', '2487889', '2488042', '2487796', '2488853', '349859', '773692', '2488867', '1132599']
# Tests that the number of items returned from get_weather_data matches locations given
@pytest.mark.asyncio
async def test_length():    
    data = await get_weather_data(locations)
    assert len(data) == len(locations)

#Tests that 3 locations finishes in two seconds or less
@pytest.mark.asyncio
async def test_speed():
    start = timeit.default_timer()
    _ = await get_weather_data(locations)
    stop = timeit.default_timer()
    time = stop - start
    assert time <= 3
