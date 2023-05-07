from ..models import Cadastro


def add_cadastro(new_cadastro):
    cadastro = Cadastro(description=new_cadastro)
    cadastro.save()
    return cadastro.to_dict_json()


def list_cadastros():
    cadastros = Cadastro.objects.all()
    return [item.to_dict_json() for item in cadastros]
