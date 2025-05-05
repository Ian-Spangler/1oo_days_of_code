import requests

class Post:
    def __init__(self):
        self.url="https://api.npoint.io/c790b4d5cab58020d391"
    
    def get_blogs(self):
        blog_response = requests.get(url=self.url)
        blog_data = blog_response.json()
        return blog_data
    
    def get_choosen_blog(self, n):
        blogs = self.get_blogs()
        for blog in blogs:
            if blog["id"] == n:
                return blog