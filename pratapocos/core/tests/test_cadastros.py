from pratapocos.core.models import Cadastro


def test_criar_cadastro_sem_login(client):
    resp = client.post("/api/core/cadastros/add", {"new_cadastro": "walk the dog"})
    assert resp.status_code == 401


def test_criar_cadastro_com_login(client_with_logged_user):
    resp = client_with_logged_user.post("/api/core/cadastros/add", {"description": "uma nova tarefa"})
    assert resp.status_code == 200


def test_listar_cadastro_com_login(client_with_logged_user):
    new_cadastro = Cadastro.objects.create(description="walk the dog")

    resp = client_with_logged_user.get("/api/core/cadastros/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"cadastros": [{"description": "walk the dog", "done": False, "id": new_cadastro.id}]}
