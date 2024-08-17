import unittest
from unittest.mock import patch

from User.Repository.user_repository import User
from User.Service.user_service import UserService


class TestUserService(unittest.TestCase):

    @patch('User.Repository.user_repository.UserRepository')
    def test_get_user_by_id(self, MockUserRepository):
        mock_user = User(user_id=1, username='testuser', password_hash='hashedpassword', email='testuser@example.com')
        MockUserRepository.get_by_id.return_value = mock_user

        user_id = 1
        result = UserService.get_user_by_id(user_id)

        self.assertEqual(result.user_id, mock_user.user_id)
        MockUserRepository.get_by_id.assert_called_once_with(user_id)

    @patch('User.Repository.user_repository.UserRepository')
    def test_get_user_by_username(self, MockUserRepository):
        mock_user = User(user_id=1, username='testuser', password_hash='hashedpassword', email='testuser@example.com')
        MockUserRepository.get_by_username.return_value = mock_user

        username = 'testuser'
        result = UserService.get_user_by_username(username)

        self.assertEqual(result.username, mock_user.username)
        MockUserRepository.get_by_username.assert_called_once_with(username)

    @patch('User.Repository.user_repository.UserRepository')
    def test_create_user(self, MockUserRepository):
        username = 'testuser'
        password_hash = 'hashedpassword'
        email = 'testuser@example.com'

        mock_user = User(user_id=1, username=username, password_hash=password_hash, email=email)
        MockUserRepository.create.return_value = mock_user

        result = UserService.create_user(username, password_hash, email)

        self.assertEqual(result.username, username)
        self.assertEqual(result.email, email)
        MockUserRepository.create.assert_called_once()

    @patch('User.Repository.user_repository.UserRepository')
    def test_update_user(self, MockUserRepository):
        mock_user = User(user_id=1, username='testuser', password_hash='hashedpassword', email='testuser@example.com')
        MockUserRepository.update.return_value = mock_user

        result = UserService.update_user(mock_user)

        self.assertEqual(result.user_id, mock_user.user_id)
        MockUserRepository.update.assert_called_once_with(mock_user)

    @patch('User.Repository.user_repository.UserRepository')
    def test_delete_user(self, MockUserRepository):
        mock_user = User(user_id=1, username='testuser', password_hash='hashedpassword', email='testuser@example.com')

        UserService.delete_user(mock_user)

        MockUserRepository.delete.assert_called_once_with(mock_user)

    @patch('User.Repository.user_repository.UserRepository')
    def test_get_all_users(self, MockUserRepository):
        mock_user1 = User(user_id=1, username='user1', password_hash='hashed1', email='user1@example.com')
        mock_user2 = User(user_id=2, username='user2', password_hash='hashed2', email='user2@example.com')
        MockUserRepository.get_all_users.return_value = [mock_user1, mock_user2]

        result = UserService.get_all_users()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].username, mock_user1.username)
        self.assertEqual(result[1].email, mock_user2.email)
        MockUserRepository.get_all_users.assert_called_once()


if __name__ == '__main__':
    unittest.main()
