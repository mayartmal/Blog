MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post'



blogs = dict() #blog_name: Block object



def menu():
    #show the user the available blogs
    #let the user make a choise
    #do something with the choise
    #eventuallu exit

    print_blogs()
    selection =input(MENU_PROMPT)


def print_blogs():
    #print available blogs
    for key, blog in blogs.items(): #[(blog_name: Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

