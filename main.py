from blog import Blog

b = Blog("MyLife", "Artem")
print(b.__repr__(), '\n')

b.create_post("Day1", "All was not so good but in was new")
b.create_post("Day2", "Nothing new")
print(b.__repr__(), '\n')

print(b.json())