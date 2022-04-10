import pytest
import timeit
from services.city_service import get_weather_data

locations = ['2487610', '2442047', '2366355', '2487956', '2487889', '2488042', '2487796', '2488853', '349859', '773692', '2488867', '1132599']

@pytest.mark.asyncio
async def test_length():
    '''
    Tests that the number of items returned from get_weather_data matches locations given
    '''
    data = await get_weather_data(locations)
    assert len(data) == len(locations)

@pytest.mark.asyncio
async def test_speed():
    '''
    Tests that 12 locations finishes in four seconds or less
    '''
    start = timeit.default_timer()
    _ = await get_weather_data(locations)
    stop = timeit.default_timer()
    time = stop - start
    print(time)
    assert time <= 4
