from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
# TDD (User 관련 test code)
# TDD : Test Driven Development
class UserTestCase(TestCase):
    
    # usual user create test
    def test_create_user(self):
        email = 'mik@gmail.com'
        password = 'password123'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 정상적으로 잘 만들어졌는지 확인.
        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        # self.assertEqual(user.is_superuser, False)
        self.assertFalse(user.is_superuser)

    # super user create test
    def test_create_superuser(self):
        email = 'mjk_super@gmail.com'
        password = 'password123'

        super_user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)

