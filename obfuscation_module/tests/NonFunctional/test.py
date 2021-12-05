import requests
import concurrent.futures
import shutil
import time
import concurrent.futures
import urllib.request
import timeit
import os



def load_url(url):
    start = time.time_ns()
    rez = requests.get(url)
    end = time.time_ns()
    return (end-start) // 1000


def stress_test(stress, test_url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=stress) as executor:
        m = 0
        future_to_url = {executor.submit(load_url, test_url): test_url for _ in range(0, stress)}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                m += data

            return m


url = 'http://127.0.0.1:5000/deobfuscate-page?image-name=71266911.png'

if __name__ == "__main__":
    rez = []
    for i in range(500, 2000, 100):
        print("sress lvl = ", i)
        rez.append([i, stress_test(i,url)])

    print(rez)
