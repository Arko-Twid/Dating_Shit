"""
Dating Conversation Assistant API
Main FastAPI application with core endpoints
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
from datetime import datetime
import logging

from app.services.conversation_analyzer import ConversationAnalyzer
from app.services.suggestion_engine import SuggestionEngine
from app.services.profile_optimizer import ProfileOptimizer
from app.services.trend_analyzer import TrendAnalyzer
from app.models.database import get_db
from app.models.schemas import (
    ConversationAnalysisRequest,
    ConversationAnalysisResponse,
    SuggestionRequest,
    SuggestionResponse,
    ProfileOptimizationRequest,
    ProfileOptimizationResponse,
    TrendAnalysisRequest,
    TrendAnalysisResponse
)
from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Dating Conversation Assistant API",
    description="AI-powered dating conversation and profile optimization",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
conversation_analyzer = ConversationAnalyzer()
suggestion_engine = SuggestionEngine()
profile_optimizer = ProfileOptimizer()
trend_analyzer = TrendAnalyzer()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Dating Conversation Assistant API", 
        "status": "healthy",
        "version": "1.0.0",
        "openai_configured": bool(settings.openai_api_key)
    }

@app.post("/analyze-conversation", response_model=ConversationAnalysisResponse)
async def analyze_conversation(
    request: ConversationAnalysisRequest,
    db = Depends(get_db)
):
    """
    Analyze a dating conversation and provide insights
    """
    try:
        analysis = await conversation_analyzer.analyze_conversation(
            messages=request.messages,
            user_context=request.user_context,
            partner_context=request.partner_context
        )
        
        return ConversationAnalysisResponse(
            conversation_id=request.conversation_id,
            analysis=analysis,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error analyzing conversation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get-suggestions", response_model=SuggestionResponse)
async def get_suggestions(
    request: SuggestionRequest,
    db = Depends(get_db)
):
    """
    Get smart suggestions for improving the conversation
    """
    try:
        suggestions = await suggestion_engine.generate_suggestions(
            conversation_context=request.conversation_context,
            user_preferences=request.user_preferences,
            suggestion_type=request.suggestion_type
        )
        
        return SuggestionResponse(
            conversation_id=request.conversation_id,
            suggestions=suggestions,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error generating suggestions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize-profile", response_model=ProfileOptimizationResponse)
async def optimize_profile(
    request: ProfileOptimizationRequest,
    db = Depends(get_db)
):
    """
    Analyze and optimize user's dating profile
    """
    try:
        optimization = await profile_optimizer.optimize_profile(
            photos=request.photos,
            bio=request.bio,
            preferences=request.preferences,
            region=request.region
        )
        
        return ProfileOptimizationResponse(
            user_id=request.user_id,
            optimization=optimization,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error optimizing profile: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-trends", response_model=TrendAnalysisResponse)
async def analyze_trends(
    request: TrendAnalysisRequest,
    db = Depends(get_db)
):
    """
    Analyze regional dating trends and preferences
    """
    try:
        trends = await trend_analyzer.analyze_trends(
            region=request.region,
            age_range=request.age_range,
            preferences=request.preferences
        )
        
        return TrendAnalysisResponse(
            region=request.region,
            trends=trends,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error analyzing trends: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "services": {
            "conversation_analyzer": "active",
            "suggestion_engine": "active",
            "profile_optimizer": "active",
            "trend_analyzer": "active"
        },
        "configuration": {
            "openai_configured": bool(settings.openai_api_key),
            "debug_mode": settings.debug,
            "environment": settings.environment
        }
    }

@app.get("/quick-suggestions/{message_type}")
async def get_quick_suggestions(message_type: str):
    """Get quick suggestions for common message types"""
    try:
        suggestions = suggestion_engine.get_quick_suggestions(message_type)
        return {
            "message_type": message_type,
            "suggestions": suggestions,
            "timestamp": datetime.utcnow()
        }
    except Exception as e:
        logger.error(f"Error getting quick suggestions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/trends/{region}")
async def get_region_trends(region: str):
    """Get trending topics for a specific region"""
    try:
        trending_topics = trend_analyzer.get_trending_topics(region)
        popular_photos = trend_analyzer.get_popular_photo_types(region)
        communication_style = trend_analyzer.get_communication_style(region)
        
        return {
            "region": region,
            "trending_topics": trending_topics,
            "popular_photo_types": popular_photos,
            "communication_style": communication_style,
            "timestamp": datetime.utcnow()
        }
    except Exception as e:
        logger.error(f"Error getting region trends: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)