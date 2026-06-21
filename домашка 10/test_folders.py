import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers_variable = {
    "Authorization": os.environ["CLICKUP_TOKEN"],
    "Content-Type": "application/json",
}

SPACE_ID = "90127627382"
created_folder_id = None


def test_post_folder():
    global created_folder_id
    response = requests.post(
        f'https://api.clickup.com/api/v2/space/{SPACE_ID}/folder',
        headers=headers_variable,
        json={"name": "test_folder"}
    )

    print('THIS IS MY CHECK FOR RESPONSE')

    assert response.status_code == 200
    assert response.json()["name"] == "test_folder"

    created_folder_id = response.json()["id"]


def test_get_lists():
    response = requests.get(
        f'https://api.clickup.com/api/v2/folder/{created_folder_id}/list',
        headers=headers_variable
    )

    print('THIS IS MY CHECK FOR RESPONSE')

    assert response.status_code == 200
    assert "lists" in response.json()


def test_put_folder():
    name = "test_folder_updated"
    response = requests.put(
        f'https://api.clickup.com/api/v2/folder/{created_folder_id}',
        headers=headers_variable,
        json={"name": name}
    )

    print('THIS IS MY CHECK FOR RESPONSE')

    assert response.status_code == 200
    assert response.json()["name"] == name

    response_for_get = requests.get(
        f'https://api.clickup.com/api/v2/folder/{created_folder_id}',
        headers=headers_variable
    )

    assert response_for_get.status_code == 200
    assert response_for_get.json()["name"] == name


def test_delete_folder():
    response = requests.delete(
        f'https://api.clickup.com/api/v2/folder/{created_folder_id}',
        headers=headers_variable
    )

    print('THIS IS MY CHECK FOR RESPONSE')

    assert response.status_code == 200

