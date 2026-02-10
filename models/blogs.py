from datetime import datetime
from typing import Dict, List, Optional


class Blog:
    """In-memory blog model"""
    
    def __init__(
        self,
        id: int,
        title: str,
        content: str,
        published: bool = False,
        created_at: datetime = None,
        updated_at: datetime = None
    ):
        self.id = id
        self.title = title
        self.content = content
        self.published = published
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at
    
    def to_dict(self) -> Dict:
        """Convert Blog instance to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "published": self.published,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def update(self, **kwargs):
        """Update blog attributes"""
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()


class BlogStore:
    """In-memory storage for blogs"""
    
    def __init__(self):
        self.blogs: Dict[int, Blog] = {}
        self.next_id: int = 1
    
    def create(self, title: str, content: str, published: bool = False) -> Blog:
        """Create a new blog post"""
        blog = Blog(
            id=self.next_id,
            title=title,
            content=content,
            published=published
        )
        self.blogs[self.next_id] = blog
        self.next_id += 1
        return blog
    
    def get_all(self) -> List[Blog]:
        """Get all blog posts"""
        return list(self.blogs.values())
    
    def get_by_id(self, blog_id: int) -> Optional[Blog]:
        """Get blog post by ID"""
        return self.blogs.get(blog_id)
    
    def update(self, blog_id: int, **kwargs) -> Optional[Blog]:
        """Update blog post"""
        blog = self.get_by_id(blog_id)
        if blog:
            blog.update(**kwargs)
        return blog
    
    def delete(self, blog_id: int) -> bool:
        """Delete blog post"""
        if blog_id in self.blogs:
            del self.blogs[blog_id]
            return True
        return False