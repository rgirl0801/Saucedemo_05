from conf import URL
from pages.login_page import LoginPage
import pytest
from locators.locators import LoginLocators as ll


class TestSample:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(
        'username, password',
        [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')],
    )
    def test_sample(self, driver, username, password):
        lp = LoginPage(driver)
        assert lp.login_title() == ll.title
        lp.action_login(username, password)
        lp.action_logout()

    '''
    Example of skipped test
    '''

    @pytest.mark.skip(reason="test is skipped because, ")
    def test_login_skip(self):
        pass

    '''
    Example of xfail test
    '''

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_login_invalid(self):
        pass

    '''
    Example of failed test
    '''

    @pytest.mark.xfail
    def test_always_fail(self):
        assert 1 == 0
