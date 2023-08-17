import requests
from django.http import JsonResponse
from backend_api.serializer import *


def serialize_and_save_to_json():
    serialized_vk_data = VKParserSerializers(VkParserData.objects.all(), many=True).data
    serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data

    data_for_json = {
        "vk": {
            "auth":
                {
                    "login": serialized_vk_data[0]['login'],
                    "password": serialized_vk_data[0]['password']
                },
            "urls": {
                "feed": serialized_task_data[0]['url_group'],
                "login": "https://vk.com/login"
            },
            "task": {
                "id_last_post": serialized_task_data[0]['id_last_post'],
                "text": serialized_task_data[0]['search_text'],
                "id_task": serialized_task_data[0]['id']
            }
        }
    }

    with open('config.example.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_for_json, json_file, indent=4, ensure_ascii=False)

    return JsonResponse(data_for_json, status=200)


def get_data_from_server():
    response = serialize_and_save_to_json()
    if response.status_code == 200:
        data = response
        return data
    else:
        print('Ошибка при получении данных')


def send_user_info_to_server(data):
    url = 'http://192.168.0.189:8000/found_data/'
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print('Данные успешно отправлены на сервер')
    else:
        print('Ошибка при отправке данных на сервер')