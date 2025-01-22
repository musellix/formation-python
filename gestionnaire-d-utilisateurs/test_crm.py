import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage

from crm import User

@pytest.fixture
def setup_db():
    # on defini la bdd pour les tests pour ne pas ecrire dans le json
    User.DB = TinyDB(storage=MemoryStorage)

@pytest.fixture
def user(setup_db):
    u = User(first_name="Patrick",
             last_name="Martin",
             address="Paris",
             phone_number="0123456789")
    u.save()
    return u

def test_full_name(user):
    assert user.full_name == 'Patrick Martin'

def test_exists(user):
    assert user.exists() is True

def test_not_exists(setup_db):
    u = User(first_name="Patrick",
             last_name="Martin",
             address="Paris",
             phone_number="0123456789")
    assert u.exists() is False

def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == 'Patrick'
    assert user.db_instance["last_name"] == 'Martin'
    assert user.db_instance["phone_number"] == '0123456789'
    assert user.db_instance["address"] == 'Paris'

def test_not_db_instance(setup_db):
    u = User(first_name="Patrick",
             last_name="Martin",
             address="Paris",
             phone_number="0123456789")
    assert u.db_instance is None

def test__check_phone_number(setup_db):
    user_good = User(   first_name="Patrick",
                        last_name="Martin",
                        address="Paris",
                        phone_number="0123456789")
    user_bad = User(   first_name="Patrick",
                        last_name="Martin",
                        address="Paris",
                        phone_number="abcd")

    with pytest.raises(ValueError) as error:
        user_bad._check_phone_number()

    expected_message = f"Numéro de téléphone {user_bad.phone_number} invalide."
    assert str(error.value) == expected_message

    user_good.save(validate_data=True)
    assert user_good.exists() is True

def test__check_names_onvalide_caracters():
    user_bad = User(first_name="Patrick%%%",
                    last_name="Martin+++",
                    address="Paris",
                    phone_number="abcd")

    with pytest.raises(ValueError) as error:
        user_bad._check_names()

    assert f"Nom invalide {user_bad.full_name}."

def test_save():
    user_test = User(first_name="Patrick",
                     last_name="Martin",
                     address="Paris",
                     phone_number="0123456789")
    user_test_bis = User(   first_name="Patrick",
                            last_name="Martin",
                            address="Paris",
                            phone_number="0123456789")
    first = user_test.save()
    second = user_test_bis.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1


def test_delete():
    user_test = User(first_name="Patrick",
                     last_name="Martin",
                     address="Paris",
                     phone_number="0123456789")

    user_test.save()
    first = user_test.delete()
    second = user_test.delete()
    assert len(first) > 0
    assert isinstance(first, list)
    assert len(second) == 0
    assert isinstance(second, list)
