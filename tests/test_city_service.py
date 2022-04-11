import timeit
import requests
from services.threaded_service import process_queue
# from services.async_service import gather_task


alt_locations = [f"https://brockhalladay.pythonanywhere.com/api/hookcatches/{x+1}" for x in range(12)]

def syncronous_reqs(locations):
    for loc in locations:
        requests.get(loc)

def test_length():
    '''
    Tests that the number of items returned from get_weather_data matches locations given
    '''
    data = process_queue(alt_locations)
    assert len(data) == len(alt_locations)

def test_threading_speed():
    '''
    Tests that threaded time is faster than iterating through each request
    '''
    start1 = timeit.default_timer()
    _ = process_queue(alt_locations)
    thread_time = timeit.default_timer() - start1

    start2 = timeit.default_timer()
    _syncproc = syncronous_reqs(alt_locations)
    sync_time = timeit.default_timer() - start2
    
    assert thread_time < sync_time

# "locations" are IDs for MetaWeather API - Not currently using these
# locations = ['2487610', '2442047', '2366355', '2487956', '2487889', '2488042', '2487796', '2488853', '349859', '773692', '2488867', '1132599']

# @pytest.mark.asyncio
# async def test_length():
#     '''
#     Tests that the number of items returned from get_weather_data matches locations given
#     '''
#     data = await gather_task(alt_locations)
#     assert len(data) == len(alt_locations)

# @pytest.mark.asyncio
# async def test_speed():
#     '''
#     Tests that 12 locations finishes in four seconds or less
#     '''
#     start = timeit.default_timer()
#     _ = await gather_task(alt_locations)
#     stop = timeit.default_timer()
#     time = stop - start
#     assert time <= 4
