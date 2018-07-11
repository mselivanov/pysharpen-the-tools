from concurrent import futures
from random import randint
from datetime import datetime as dt
import requests
import os
from time import perf_counter_ns

COUNTRY_CODES = ['ad','ae','af','ag','ai','al','am','an','ao','aq','ar','as','at','au','aw','ax','az','ba','bb','bd','be','bf','bg','bh','bi','bj','bl','bm','bn','bo','bq','br','bs','bt','bv','bw','by','bz','ca','cc','cd','cf','cg','ch','ci','ck','cl','cm','cn','co','cr','cu','cv','cw','cx','cy','cz','de','dj','dk','dm','do','dz','ec','ee','eg','eh','er','es','et','eu','fi','fj','fk','fm','fo','fr','ga','gb-eng','gb-nir','gb-sct','gb-wls','gb','gd','ge','gf','gg','gh','gi','gl','gm','gn','gp','gq','gr','gs','gt','gu','gw','gy','hk','hm','hn','hr','ht','hu','id','ie','il','im','in','io','iq','ir','is','it','je','jm','jo','jp','ke','kg','kh','ki','km','kn','kp','kr','kw','ky','kz','la','lb','lc','li','lk','lr','ls','lt','lu','lv','ly','ma','mc','md','me','mf','mg','mh','mk','ml','mm','mn','mo','mp','mq','mr','ms','mt','mu','mv','mw','mx','my','mz','na','nc','ne','nf','ng','ni','nl','no','np','nr','nu','nz','om','pa','pe','pf','pg','ph','pk','pl','pm','pn','pr','ps','pt','pw','py','qa','re','ro','rs','ru','rw','sa','sb','sc','sd','se','sg','sh','si','sj','sk','sl','sm','sn','so','sr','ss','st','sv','sx','sy','sz','tc','td','tf','tg','th','tj','tk','tl','tm','tn','to','tr','tt','tv','tw','tz','ua','ug','um','us','uy','uz','va','vc','ve','vg','vi','vn','vu','web','wf','ws','xk','ye','yt','za','zm','zw']

MAX_WORKERS = 20
BASE_URL = 'http://localhost/flags/'
DOWNLOAD_DIR = os.path.join('c:\\', 'Tmp', 'downloads')

def print_exec_time(f):
    def measure_time(*args, **kwargs):
        start_time = perf_counter_ns()
        result = f(*args, **kwargs)
        duration = perf_counter_ns() - start_time
        print(f"{f.__name__} executed in: {duration:15} nanos")
        return result
    return measure_time

def get_file(base_url, path):
    resp = requests.get(f'{base_url}/{path}')
    return resp.content

def save_file(data, path):
    with open(path, 'wb') as f:
        f.write(data)

@print_exec_time
def single_thread_example(number_flags):
    for country_code in COUNTRY_CODES[:number_flags]:
        download_flag(country_code)

def download_flag(country_code):
        file_name = country_code + '.png'
        flag = get_file(BASE_URL, file_name)
        save_file(flag, os.path.join(DOWNLOAD_DIR, file_name))

@print_exec_time
def multithreaded_example(number_flags):
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        res = executor.map(download_flag, COUNTRY_CODES[:number_flags])


@print_exec_time
def multiprocess_example(number_flags):
    to_do = []
    with futures.ProcessPoolExecutor() as executor:
        for country_code in COUNTRY_CODES[:number_flags]:
            future = executor.submit(download_flag, country_code)
            to_do.append(future)
        done_iter = futures.as_completed(to_do)

def main():
    single_thread_example(len(COUNTRY_CODES))
    multithreaded_example(len(COUNTRY_CODES))
    multiprocess_example(len(COUNTRY_CODES))

if __name__ == '__main__':
    main()
