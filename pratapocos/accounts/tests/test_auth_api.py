from unittest.mock import ANY

from pratapocos.accounts.models import User


def test_deve_retornar_usuario_nao_logado(client):
    resp = client.get("/api/accounts/whoami")

    assert resp.status_code == 200
    assert resp.json() == {"authenticated": False}


def test_deve_retornar_usuario_logado(client, user_jon):
    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/accounts/whoami")

    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        "user": {
            "id": ANY,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "avatar": None,
            "bio": "bio",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


def test_deve_fazer_login(client, user_jon):
    resp = client.post("/api/accounts/login", {"username": "jon", "password": "snow"})
    login = resp.json()

    resp = client.get("/api/accounts/whoami")
    data = resp.json()

    assert login["email"] == "jon@example.com"
    assert resp.status_code == 200
    assert data == {
        "user": {
            "id": ANY,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "avatar": None,
            "bio": "bio",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


def test_deve_fazer_logout(client_with_logged_user):
    resp = client_with_logged_user.post("/api/accounts/logout")

    assert resp.status_code == 200
    assert not resp.json()


def test_deve_fazer_logout_mesmo_sem_login(client):
    resp = client.post("/api/accounts/logout")
    assert resp.status_code == 200
