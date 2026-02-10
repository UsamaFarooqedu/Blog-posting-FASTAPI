# posting/__init__.py
# Leave empty or add version
__version__ = "1.0.0"

# posting/models/__init__.py
from .models.blogs import Blog, BlogStore
__all__ = ["Blog", "BlogStore"]

# posting/schema/__init__.py
from .schema.blogs import BlogBase, BlogCreate, BlogUpdate, BlogResponse
__all__ = ["BlogBase", "BlogCreate", "BlogUpdate", "BlogResponse"]

# posting/routes/__init__.py
from .routes.blogs import router as posts_router
__all__ = ["posts_router"]