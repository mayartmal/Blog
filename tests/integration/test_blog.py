from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_repr_multiple_posts(self):
        blog = Blog("Test Blog", "Test Author")
        expected0 = f"A Test Blog blog by Test Author with 0 posts"
        self.assertEqual(blog.__repr__(), expected0)

        blog.create_post("Test Title 1", "Test Content 1")
        expected1 = f"A Test Blog blog by Test Author with 1 posts"
        self.assertEqual(blog.__repr__(), expected1)

        blog.create_post("Test Title 2", "Test Content 2")
        expected2 = f"A Test Blog blog by Test Author with 2 posts"
        self.assertEqual(blog.__repr__(), expected2)


    def test_create_post(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Post", "Test Content")

        self.assertEqual(1, len(blog.posts))
        self.assertEqual(blog.posts[0].title, "Test Post")
        self.assertEqual(blog.posts[0].content, "Test Content")


    def test_json(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Title 1", "Test Content 1")
        blog.create_post("Test Title 2", "Test Content 2")
        expected = {
            "title": "Test Blog",
            "author": "Test Author",
            "posts number": 2,
            "Test Title 1": "Test Content 1",
            "Test Title 2": "Test Content 2"
        }
        self.assertDictEqual(expected, blog.json())