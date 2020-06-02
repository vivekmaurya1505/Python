
import time
import webbrowser as web
import requests


last = time.time()

try : 
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current-last
        
except Exception:
    exc = ("NO INTERNET - Searcher needs active internet connection")
    raise Exception(exc)

if tyme >= 5:
        raise Warning("INTERNET IS SLOW, extraction of information might take longer time")

web.open_new_tab("https://www.linkedin.com/feed/")
