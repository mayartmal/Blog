class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content


    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }

    def __repr__(self):
        return f"A {self.title} post record with {self.content} content"
