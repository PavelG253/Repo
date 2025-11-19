from yougile_api import YouGileAPI

API_KEY = "RcX6cuqNkaKlWwBaos5f4KI4pArcarfv3TEHBQRCy7vDDqLnB46JTVZTn76vD-2R"


def test_positive_create_project():

    api = YouGileAPI(API_KEY)
    response = api.create_project("Projector")
    assert response.status_code == 201


def test_negative_create_project():

    api = YouGileAPI(API_KEY)
    response = api.create_project("")
    assert response.status_code == 400


def test_positive_get_project_by_id():

    api = YouGileAPI(API_KEY)

    create_response = api.create_project("Project to get")
    project_id = create_response.json()["id"]

    get_response = api.get_project(project_id)

    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == project_id


def test_negative_get_unexisted_project():

    api = YouGileAPI(API_KEY)

    response = api.get_project("Unexisted_id")

    assert response.status_code == 404


def test_positive_update_project_title():

    api = YouGileAPI(API_KEY)

    create_response = api.create_project("Preset")
    project_id = create_response.json()["id"]

    update_response = api.update_project_title(
        project_id, "Customized preset")

    assert update_response.status_code == 200


def test_negative_update_project_title():

    api = YouGileAPI(API_KEY)

    response = api.update_project_title(
        "Unexisted_id", "Smth new")

    assert response.status_code == 404
