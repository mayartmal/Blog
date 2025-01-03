blogs = dict() #blog_name: Block object



def menu():
    #show the user the available blogs
    #let the user make a choise
    #do something with the choise
    #eventuallu exit
    print_blogs()
def print_blogs():
    #print available blogs
    for key, blog in blogs.items(): #[(blog_name: Blog), (blog_name, Blog)]
        print('-{}'.format(blog))

