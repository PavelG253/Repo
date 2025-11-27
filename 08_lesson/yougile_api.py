import requests


class YouGileAPI:

    def __init__(self, api_key):

        self.base_url = "https://ru.yougile.com/api-v2"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):

        data = {"title": title}

        response = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):

        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response

    def update_project_title(self, project_id, new_title):

        data = {"title": new_title}

        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response
