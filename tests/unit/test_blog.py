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



