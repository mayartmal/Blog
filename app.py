from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post'
POST_TEMPLATE = '''
--- {} ---

{}

'''



blogs = dict() #blog_name: Block object



def menu():
    #show the user the available blogs
    #let the user make a choise
    #do something with the choise
    #eventuallu exit

    print_blogs()
    selection =input(MENU_PROMPT)
    while selection != 'q':
        if selection  == 'c':
            ask_create_blog()
        elif selection  == 'l':
            print_blogs()
        elif selection  == 'r':
            ask_read_blog()
        elif selection  == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    #print available blogs
    for key, blog in blogs.items(): #[(blog_name: Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

def ask_create_blog():
    blog_title = input("Input Blog Title: ")
    blog_author = input("Input Blog Author: ")
    blogs[blog_title] = Blog(blog_title, blog_author)

def ask_read_blog():
    blog_title = input("Input Blog Title: ")
    print_posts(blogs[blog_title])

def print_posts(blog):
    print(blog)
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    pass

