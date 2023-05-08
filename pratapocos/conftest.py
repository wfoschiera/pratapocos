import pytest

from pratapocos.accounts.models import User


@pytest.fixture
def user_jon(db):
    jon = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
        bio="bio",
    )
    return jon


@pytest.fixture
def client_with_logged_user(client, user_jon):
    client.force_login(user_jon)
    return client
