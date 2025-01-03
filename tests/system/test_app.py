import builtins
from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog



class TestApp(TestCase):
    def test_menu__prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'):
                app.menu()
                mocked_print_blogs.assert_called()


    def test_print_blogs(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- A Test Blog blog by Test Author with 0 posts')


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test Blog'))


    def test_ask_read_blog(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test Blog', 'Test Author')
        blog.create_post("Test Post", "Test Content")
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        blog = Blog('Test Blog', 'Test Author')
        blog.create_post("Test Post", "Test Content")
        app.blogs = {'Test': blog}

        with patch('builtins.print') as mocked_print:
            app.print_post(blog.posts[0])
            mocked_print.assert_called_with(app.POST_TEMPLATE.format("Test Post", "Test Content"))
