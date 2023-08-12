from src.services.service_user import ServiceUser


class TestServiceUser:
    def test_add_user_success(self):
        service = ServiceUser()
        expected_result = "User added"
        result = service.add_user(name="Maria", job="QA")
        assert result == expected_result

    def test_add_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.add_user(name=None, job="QA")
        assert result == expected_result

    def test_add_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.add_user(name=2, job="QA")
        assert result == expected_result

    def test_add_user_already_existent(self):
        service = ServiceUser()
        expected_result = "User already existent"
        service.add_user(name="Maria", job="QA")
        result = service.add_user(name="Maria", job="QA")
        assert result == expected_result

    def test_remove_user_success(self):
        service = ServiceUser()
        expected_result = "User removed"
        service.add_user(name="Maria", job="QA")
        result = service.remove_user(name="Maria")
        assert result == expected_result

    def test_remove_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.remove_user(name=None)
        assert result == expected_result

    def test_remove_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.remove_user(name=2)
        assert result == expected_result

    def test_remove_user_not_existent(self):
        service = ServiceUser()
        expected_result = "User not existent"
        result = service.remove_user(name="Maria")
        assert result == expected_result

    def test_update_user_success(self):
        service = ServiceUser()
        expected_result = "User updated"
        service.add_user(name="Maria", job="QA")
        result = service.update_user(name="Maria", newname="Mariana")
        assert result == expected_result

    def test_update_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.update_user(name=None, newname="Mariana")
        assert result == expected_result

    def test_update_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.update_user(name=2, newname="Mariana")
        assert result == expected_result

    def test_update_user_not_existent(self):
        service = ServiceUser()
        expected_result = "User not existent"
        result = service.update_user(name="Maria", newname="Mariana")
        assert result == expected_result

    def test_get_user_by_name_success(self):
        service = ServiceUser()
        expected_result = "Maria"
        service.add_user(name="Maria", job="QA")
        result = service.get_user_by_name(name="Maria")
        assert result == expected_result

    def test_get_user_by_name_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.get_user_by_name(name=2)
        assert result == expected_result

    def test_get_user_by_name_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.get_user_by_name(name=None)
        assert result == expected_result

    def test_get_user_by_name_not_existent(self):
        service = ServiceUser()
        expected_result = "User not found"
        result = service.get_user_by_name(name="Maria")
        assert result == expected_result