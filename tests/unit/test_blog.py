from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_create_blog(self):
        blog = Blog("Test", "Test Author")

        self.assertEqual("Test", blog.title)
        self.assertEqual("Test Author", blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr_empty_posts(self):
        blog = Blog("Test Blog", "Test Author")
        expected = f"A Test Blog blog by {blog.author} with {len(blog.posts)} posts"

        self.assertEqual(blog.__repr__(), expected)

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