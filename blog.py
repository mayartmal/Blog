class Blog:
    def __init__(self, title,  author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"A {self.title} blog by {self.author} with {len(self.posts)} posts"

    def create_post(self, title, content):
        self.posts.append({title: content})

    def json(self):
        pass
