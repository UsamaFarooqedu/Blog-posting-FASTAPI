from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class BlogBase(BaseModel):
    """Base schema with common fields"""
    title: str
    content: str
    published: bool = False


class BlogCreate(BlogBase):
    """Schema for creating a new blog post"""
    # For now, same as BlogBase
    # Add any creation-specific fields here later
    pass


class BlogUpdate(BaseModel):
    """Schema for updating a blog post"""
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None


class BlogResponse(BlogBase):
    """Schema for API responses"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True  # Allows ORM mode if using SQLAlchemy later