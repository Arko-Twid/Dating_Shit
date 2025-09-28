"""
Pydantic schemas for the Dating Conversation Assistant API
"""

from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

# Conversation Analysis Schemas
class ConversationAnalysisRequest(BaseModel):
    conversation_id: str
    messages: List[Dict[str, Any]]
    user_context: Optional[Dict[str, Any]] = None
    partner_context: Optional[Dict[str, Any]] = None

class ConversationAnalysisResponse(BaseModel):
    conversation_id: str
    analysis: Dict[str, Any]
    timestamp: datetime

# Suggestion Schemas
class SuggestionRequest(BaseModel):
    conversation_id: str
    conversation_context: Dict[str, Any]
    user_preferences: Optional[Dict[str, Any]] = None
    suggestion_type: str = "general"

class SuggestionResponse(BaseModel):
    conversation_id: str
    suggestions: List[Dict[str, Any]]
    timestamp: datetime

# Profile Optimization Schemas
class ProfileOptimizationRequest(BaseModel):
    user_id: str
    photos: List[str]
    bio: str
    preferences: Dict[str, Any]
    region: str

class ProfileOptimizationResponse(BaseModel):
    user_id: str
    optimization: Dict[str, Any]
    timestamp: datetime

# Trend Analysis Schemas
class TrendAnalysisRequest(BaseModel):
    region: str
    age_range: Optional[tuple] = None
    preferences: Optional[Dict[str, Any]] = None

class TrendAnalysisResponse(BaseModel):
    region: str
    trends: Dict[str, Any]
    timestamp: datetime
