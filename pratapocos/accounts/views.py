# coding: utf-8
from django.http import JsonResponse
from django.contrib import auth

from ninja import Router, Form, Schema

from ..core.service import log_svc

router = Router()

class PermissionSchema(Schema):
    ADMIN: bool
    STAFF: bool


class UserSchema(Schema):
    id: int
    name: str
    username: str
    first_name: str
    last_name: str
    email: str
    avatar: str = None
    bio: str = None
    permissions: PermissionSchema


class LoggedUserSchema(Schema):
    user: UserSchema
    authenticated: bool



@router.post("/login", response=UserSchema)
def login(request, username: str = Form(...), password: str = Form(...)):

    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


@router.post("/logout")
def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return JsonResponse({})


@router.get("/whoami", response=LoggedUserSchema)
def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "avatar": user.avatar,
        "bio": user.bio,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d
