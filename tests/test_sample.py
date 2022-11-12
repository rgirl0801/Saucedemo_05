from pages.login_page import LoginPage
import time
import pytest
from locators.login_locators import LoginLocators as ll


class TestSample:
    @pytest.mark.parametrize(
        'username, password',
        [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')],
    )
    def test_sample(self, d, username, password):
        lp = LoginPage(d)
        assert lp.login_title() == ll.title
        lp.action_login(username, password)
        lp.action_logout()
