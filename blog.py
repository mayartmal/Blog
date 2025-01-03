from post import Post


class Blog:
    def __init__(self, title,  author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"A {self.title} blog by {self.author} with {len(self.posts)} posts"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        result_dict = {
            "title": self.title,
            "author": self.author,
            "posts number": len(self.posts),
            "posts": [post.json() for post in self.posts]

        }
        return result_dict
