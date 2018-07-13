import requests
import json
from functools import partial
import uuid
from time import perf_counter_ns
import asyncio
import sys
import aiohttp


_DEFAULT_AUTH_URL = 'http://keycloak:10080/auth/realms/master/protocol/openid-connect/token'
_DEFAULT_ADMIN_CLIENT = 'admin-cli'
_DEFAULT_USERNAME = 'admin'
_DEFAULT_PASSWORD = 'admin'

_DEFAULT_HEADER_TEMPLATE = {'Content-Type': 'application/json', 'Authorization': 'bearer {}'}
_REALMS_URL = 'http://keycloak:10080/auth/admin/realms'
_CLIENT_URL_TEMPLATE = 'http://keycloak:10080/auth/admin/realms/{realm_name}/clients'
_USER_URL_TEMPLATE = 'http://keycloak:10080/auth/admin/realms/{realm_name}/users'

_REALM_DATA_TEMPLATE = {"id": None, "realm": "LoadRealm_{:05}"}
_CLIENT_DATA_TEMPLATE = {"id": None, "name": "Client_{:02}"}
_USER_DATA_TEMPLATE = {"id": None, "username": "User_{:06}"}

_MODEL = {
            "realms_count": 10,
            "clients_per_realm": 2,
            "users_per_realm": 10
         }

def measure_exec_time(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        result = f(*args, **kwargs)
        end_time = perf_counter_ns()
        print(f'Function {f.__name__} executed in: {(end_time - start_time)/10**9}')
        return result
    return wrapper

def get_access_token(url, client_id, username, password):
    data = {"grant_type":"password", "client_id": client_id, "username": username, "password": password}
    response = requests.post(url=url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    raise RuntimeError(f'Error during getting access token: {response.json()}')

default_access_token = partial(get_access_token,
                               _DEFAULT_AUTH_URL,
                               _DEFAULT_ADMIN_CLIENT,
                               _DEFAULT_USERNAME,
                               _DEFAULT_PASSWORD)

def create_headers(access_token):
    headers = dict(_DEFAULT_HEADER_TEMPLATE)
    headers['Authorization'] = headers['Authorization'].format(access_token)
    return headers

def create_entity(url, access_token, entity_data):
    response = requests.post(url=url, headers=create_headers(access_token), data=json.dumps(entity_data))
    return response

def delete_entity(url, access_token, key):
    delete_url = url+'/'+key
    response = requests.delete(url=delete_url, headers=create_headers(access_token))
    return response

create_realm = partial(create_entity, _REALMS_URL)
delete_realm = partial(delete_entity, _REALMS_URL)

def realm_data(idx):
        data = dict(_REALM_DATA_TEMPLATE)
        data["id"] = str(uuid.uuid1())
        data["realm"] = data["realm"].format(idx)
        return data
    
def client_data(idx):
        data = dict(_CLIENT_DATA_TEMPLATE)
        data["id"] = str(uuid.uuid1())
        data["name"] = data["name"].format(idx)
        return data

def user_data(idx):
        data = dict(_USER_DATA_TEMPLATE)
        data["id"] = str(uuid.uuid1())
        data["username"] = data["username"].format(idx)
        return data    
    
def generate_realm_data(model):
    return (realm_data(idx) for idx in range(model["realms_count"]))

def generate_client_data(model):
    return (client_data(idx) for idx in range(model["clients_per_realm"]))

def generate_user_data(model):
    return (user_data(idx) for idx in range(model["users_per_realm"]))

default_realm_data = partial(generate_realm_data, _MODEL)
default_client_data = partial(generate_client_data, _MODEL)
default_user_data = partial(generate_user_data, _MODEL)

def cleanup():
    for data in default_realm_data():
        print(data)
        print(delete_realm(default_access_token(), data["realm"]))
        
def generate_clients(realm):
    client_url = _CLIENT_URL_TEMPLATE.format(realm_name=realm)
    create_client = partial(create_entity, client_url)
    for client_data in default_client_data():
        create_client_response = create_client(default_access_token(), client_data)

def generate_users(realm):
    user_url = _USER_URL_TEMPLATE.format(realm_name=realm)
    create_user = partial(create_entity, user_url)
    for user_data in default_user_data():
        create_user_response = create_user(default_access_token(), user_data)

def generate_one(realm, data):
    response = create_realm(default_access_token(), data)
    if response.status_code == 201:
        generate_clients(realm)
        generate_users(realm)
    
def test_generate():
    for data in default_realm_data():
        realm = data["realm"]
        generate_one(realm, data)

@measure_exec_time
def test_generate():
    for data in default_realm_data():
        realm = data["realm"]
        response = create_realm(default_access_token(), data)
        if response.status_code == 201:
            generate_clients(realm)
            generate_users(realm)

async def create_realm_async(url, access_token, realm_data):
    headers = create_headers(access_token)
    print(headers)
    print(url)
    print(realm_data)
    async with aiohttp.ClientSession() as session:
        response = await session.post(url, headers=headers, data=json.dumps(realm_data))
    print(response.status)

def test_generate_async():
    loop = asyncio.get_event_loop()
    to_do = [create_realm_async(_REALMS_URL, default_access_token(), realm_data(0))]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    print(res)
            
#Sequential is executed in ~ 30 s             

def main():
    option = sys.argv[1]
    if option == 'g':
        test_generate()
    elif option == 'c':
        cleanup()
    elif option == 'ga':
        test_generate_async()
    else:
        print('Enter option')

if __name__ == '__main__':
    main()
