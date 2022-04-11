import concurrent.futures
import requests
import threading


thread_local = threading.local()
returned_q = []

def get_session():
  if not hasattr(thread_local, "session"):
    thread_local.session = requests.Session()
  return thread_local.session

def get_json_from_url(url):
  session = get_session()
  return session.get(url).json()

def process_queue(reqs):
  with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    processes = list(executor.map(get_json_from_url, reqs))
    print(processes)
  return processes

# ten_requests = [f"https://brockhalladay.pythonanywhere.com/api/hookcatches/{x+1}" for x in range(10)]
# start = timeit.default_timer()
# process_queue(ten_requests)
# time = timeit.default_timer() - start
# print(f"Processed {len(returned_q)} in {time} seconds")
# print(returned_q)
