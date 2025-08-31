import pytest
from faker import Faker

@pytest.fixture
def random_user_for_registration():
    fake = Faker()
    return {
        'email': fake.email(),
        'username': fake.user_name(),
        'password': fake.password(length=16)
    }

@pytest.fixture
def valid_user():
    return {
        'email': 'testuser@gmail.com',
        'username': 'testuser',
        'password': 'SecurePass123!'
    }