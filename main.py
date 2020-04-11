import requests


def get_upload_link(filename):

    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    params = {
        'path' : f'/test/{filename}',
        'overwrite' : 'true'
    }

    headers = {
        'Authorization' : 'AgAAAAA_cp8rAADLWwM2yabLMEdHvtlAjuTvdMI'
    }

    response = requests.get(URL, params=params, headers=headers)

    return response.json()['href']

def upload_file(filename):
    URL = get_upload_link(filename)
    with open(filename, 'rb') as file:
        response = requests.put(URL, data=file)
        print(response)

upload_file('test.txt')
upload_file('test.png')

