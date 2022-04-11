import concurrent.futures
import requests
import threading


thread_local = threading.local()

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
  return processes

