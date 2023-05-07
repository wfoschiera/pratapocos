from pratapocos.accounts.models import User
from pratapocos.accounts.tests import fixtures
from pratapocos.core.models import Cadastro


def test_criar_cadastro_sem_login(client):
    resp = client.post("/api/core/cadastros/add", {"new_cadastro": "walk the dog"})
    assert resp.status_code == 401


def test_criar_cadastro_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/core/cadastros/add", {"new_cadastro": "walk the dog"})
    assert resp.status_code == 200


def test_criar_cadastro_com_login_2(client, db):
    fixtures.user_jon()
    Cadastro.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/core/cadastros/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"cadastros": [{"description": "walk the dog", "done": False, "id": 1}]}
