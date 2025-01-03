import builtins
from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog



class TestApp(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c',
                                        'Test Blog Title',
                                        'Test Blog Author',
                                        'q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Blog Title'])

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l','q')
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_read_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_read_blog:
                mocked_input.side_effect = ('r','q')
                app.menu()
                mocked_read_blog.assert_called()

    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_create_post:
                mocked_input.side_effect = ('p','q')
                app.menu()
                mocked_create_post.assert_called()


    def test_menu_prints_prompt(self):
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

    def test_ask_create_post(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test Blog': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog',
                                        'Test Post',
                                        'Test Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Test Post')
            self.assertEqual(blog.posts[0].content, 'Test Content')