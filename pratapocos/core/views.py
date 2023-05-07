# coding: utf-8

from typing import List, Optional

from django.http import JsonResponse


from ninja import Router, Form, Schema

from .service import cadastros_svc


router = Router()


class TaskSchema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class ListTasksSchema(Schema):
    tasks: List[TaskSchema]




@router.post("/tasks/add", response=TaskSchema)
def add_cadastro(request, task: TaskSchema):
    new_cadastro = cadastros_svc.add_cadastro(task.description)

    return JsonResponse(new_cadastro)



@router.get("/tasks/list", response=ListTasksSchema)

def list_cadastros(request):
    cadastros = cadastros_svc.list_cadastros()
    return JsonResponse({"cadastros": cadastros})
