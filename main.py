import unittest
import re

special_characters = "\"!@#$%^&*()-+?_=,<>/'"
blocked = ["qwertyuiop", "azertyuiop", "123456789", "password", "abcdefg"]


def checkPwd(pwd):
    res = [True]

    if not(10 <= len(pwd) <= 25):
        res.append({"type": "len", "message": "Length must be between 10 and 25"})
        res[0] = False

    if not(any(c for c in pwd if c.isdigit())):
        res.append({"type": "digit", "message": "Must contains digits"})
        res[0] = False

    if not(any(c in special_characters for c in pwd)):
        res.append({"type": "special", "message": "Must contains special characters"})
        res[0] = False

    if not(any(c for c in pwd if c.isupper())):
        res.append({"type": "upper", "message": "Must contains one uppercase"})
        res[0] = False

    if not(any(c for c in pwd if c.islower())):
        res.append({"type": "lower", "message": "Must contains one uppercase"})
        res[0] = False

    if any(word for word in blocked if word.lower() in pwd.lower()):
        res.append({"type": "common", "message": "Too common"})
        res[0] = False

    return res


class CheckPasswordServiceTest(unittest.TestCase):
    # We are searching by the error type status to check

    def test_password_valid(self):
        self.assertEqual(checkPwd("Daniel&1234"), [True])

    def test_password_length_not_valid(self):
        assert re.search(r"'type': 'len'", str(checkPwd("Dan&124")))

    def test_password_digit_not_valid(self):
        assert re.search(r"'type': 'digit'", str(checkPwd("Daniel&amiosm")))

    def test_password_special_char_not_valid(self):
        assert re.search(r"'type': 'special'", str(checkPwd("Daniel1234")))

    def test_password_upper_not_valid(self):
        assert re.search(r"'type': 'upper'", str(checkPwd("daniel&124")))

    def test_password_lower_not_valid(self):
        assert re.search(r"'type': 'lower'", str(checkPwd("DANIEL&1234")))

    def test_password_common_not_valid(self):
        assert re.search(r"'type': 'common'", str(checkPwd("abcdefg34")))

    def test_password_length_not_valid_AND_lower_not_valid(self):
        res = str(checkPwd("DAR&124"))
        assert re.search(r"'type': 'len'", res)
        assert re.search(r"'type': 'lower'", res)


if __name__ == '__main__':
    unittest.main()