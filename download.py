#!/usr/bin/env python3
# -*- codi
from time import time

import requests


def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)
            urls = [("Event1", "https://www.python.org/events/801/"),
                    ("Event2", "https://www.python.org/events/790/"),
                    ("Event3", "https://www.python.org/events/798/"),
                    ("Event4", "https://www.python.org/events/807/"),
                    ("Event5", "https://www.python.org/events/757/"), ]
            start = time()
            for x in urls:
                url_response(x)
                print(f"Time to download: {time() - start}")
