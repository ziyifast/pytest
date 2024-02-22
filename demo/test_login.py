import pytest

class TestLogin:
    accounts_list = [
        {
            "username":"user1",
            "password":"123456"
        },
        {
            "username":"user2",
            "password":"123456"
        },
        {
            "username":"user3",
            "password":"123456"
        }
    ]
    
    @pytest.mark.parametrize("account", accounts_list)
    def test_login(self, account):
        print(account, type(account))
        # flag = account["username"] == "user1" and account["password"] == "123456"
        # assert flag == True
            