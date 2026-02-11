from fastapi import APIRouter, HTTPException, status
from typing import List

# Import your schemas and models
from ..schema.blogs import BlogCreate, BlogUpdate, BlogResponse
from ..models.blogs import BlogStore

# Create router
router = APIRouter(prefix="/blogs", tags=["blogs"])

# Create storage instance
blog_store = BlogStore()


@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
async def create_blog(blog_data: BlogCreate):
    """Create a new blog post"""
    blog = blog_store.create(
        title=blog_data.title,
        content=blog_data.content,
        published=blog_data.published,
    )
    return blog.to_dict()


@router.get("/", response_model=List[BlogResponse])
async def get_all_blogs():
    """Get all blog posts"""
    return [blog.to_dict() for blog in blog_store.get_all()]


@router.get("/{blog_id}", response_model=BlogResponse)
async def get_blog(blog_id: int):
    """Get specific blog post by ID"""
    blog = blog_store.get_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog.to_dict()


@router.put("/{blog_id}", response_model=BlogResponse)
async def update_blog(blog_id: int, blog_data: BlogUpdate):
    """Update blog post"""
    blog = blog_store.update(
        blog_id,
        title=blog_data.title,
        content=blog_data.content,
        published=blog_data.published,
    )
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog.to_dict()


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int):
    """Delete blog post"""
    deleted = blog_store.delete(blog_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return None