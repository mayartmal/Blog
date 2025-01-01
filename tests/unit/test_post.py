from unittest import TestCase
from post import Post

class TestPost(TestCase):
    def test_create_post(self):
        post = Post("Test", "Test Content")

        self.assertEqual("Test", post.title)
        self.assertEqual("Test Content", post.content)

    def test_json(self):
        post = Post("Test", "Test Content")
        expected_dict = {"title": "Test", "content": "Test Content"}

        self.assertDictEqual(expected_dict, post.json())

    def test_repr(self):
        post = Post("Test", "Test Content")
        expected_string = "A Test post record with Test Content content"
        self.assertEqual(expected_string, post.__repr__())