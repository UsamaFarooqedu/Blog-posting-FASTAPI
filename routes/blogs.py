from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

# Import your schemas and models
from ..schema.blogs import BlogCreate, BlogUpdate, BlogResponse
from  ..models.blogs import BlogStore

# Create router
router = APIRouter(prefix="/blogs", tags=["blogs"])

# Create storage instance
blog_store = BlogStore()


@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
async def create_blog(blog_data: BlogCreate):
    """Create a new blog post"""
    # 1. Extract data from blog_data
    # 2. Use blog_store.create() to create new blog
    # 3. Return the created blog using .to_dict()


@router.get("/", response_model=List[BlogResponse])
async def get_all_blogs():
    """Get all blog posts"""
    # 1. Get all blogs from blog_store
    # 2. Convert each blog to dictionary
    # 3. Return list of blogs


@router.get("/{blog_id}", response_model=BlogResponse)
async def get_blog(blog_id: int):
    """Get specific blog post by ID"""
    # 1. Get blog from blog_store
    # 2. If not found, raise HTTPException 404
    # 3. Return blog as dictionary


@router.put("/{blog_id}", response_model=BlogResponse)
async def update_blog(blog_id: int, blog_data: BlogUpdate):
    """Update blog post"""
    # 1. Get blog from blog_store
    # 2. If not found, raise HTTPException 404
    # 3. Update blog using blog_store.update()
    # 4. Return updated blog as dictionary


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int):
    """Delete blog post"""
    # 1. Try to delete blog using blog_store.delete()
    # 2. If False returned, raise HTTPException 404
    # 3. Return no content (status 204)