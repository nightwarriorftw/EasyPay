from django.test import TestCase
from bankserver.models import UserModel


class TestBankServer(TestCase):

    def setUp(self) -> None:
        UserModel.objects.create(full_name="Test User", balance=1000, PIN="1234", upi_key="testuser@oksbi", email="testuser@gmail.com")

    def test_should_be_able_to_get_user_balance(self):
        user = UserModel.objects.filter(full_name="Test User", PIN="1234", upi_key="testuser@oksbi").first()
        assert user.balance == 1000

    def test_should_fail_to_get_user_balance(self):
        user = UserModel.objects.filter(full_name="Test User", PIN="1234", upi_key="testuser@oksbii").first()
        assert user is None
