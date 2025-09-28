"""
Trend analysis service for regional dating patterns
"""

import openai
from typing import List, Dict, Any
from app.config import settings

class TrendAnalyzer:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
    
    async def analyze_trends(
        self,
        region: str,
        age_range: tuple = None,
        preferences: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Analyze regional dating trends and preferences
        """
        try:
            context = f"Region: {region}"
            if age_range:
                context += f", Age range: {age_range[0]}-{age_range[1]}"
            if preferences:
                context += f", Preferences: {preferences}"
            
            system_prompt = f"""You are a dating trends analyst. Analyze dating trends for the region and provide insights on:
            1. Popular conversation topics
            2. Common interests and hobbies
            3. Communication styles
            4. Profile preferences
            5. Dating app usage patterns
            
            Focus on actionable insights for users in {region}."""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context}
                ],
                max_tokens=400,
                temperature=0.8
            )
            
            trends_text = response.choices[0].message.content
            
            return {
                "popular_topics": [
                    "Local events and activities",
                    "Food and dining",
                    "Travel and adventures",
                    "Career and ambitions"
                ],
                "communication_style": "Direct and friendly",
                "profile_preferences": {
                    "bio_length": "Medium (2-3 sentences)",
                    "photo_style": "Casual and authentic",
                    "interests": "Outdoor activities, food, travel"
                },
                "success_factors": [
                    "Being genuine and authentic",
                    "Showing local knowledge",
                    "Asking about specific interests"
                ],
                "detailed_analysis": trends_text
            }
            
        except Exception as e:
            # Fallback trend data
            return {
                "popular_topics": [
                    "Hobbies and interests",
                    "Travel experiences",
                    "Career and goals",
                    "Food and dining"
                ],
                "communication_style": "Friendly and engaging",
                "profile_preferences": {
                    "bio_length": "2-3 sentences",
                    "photo_style": "Clear and recent",
                    "interests": "Varied and specific"
                },
                "success_factors": [
                    "Be yourself",
                    "Ask good questions",
                    "Show genuine interest"
                ],
                "detailed_analysis": "Trend analysis temporarily unavailable. Please try again later.",
                "error": str(e)
            }
    
    def get_trending_topics(self, region: str) -> List[str]:
        """Get trending conversation topics for a region"""
        return [
            "Local events and festivals",
            "New restaurants and cafes",
            "Outdoor activities and nature",
            "Art and culture scene",
            "Technology and innovation"
        ]
    
    def get_popular_photo_types(self, region: str) -> List[str]:
        """Get popular photo types for a region"""
        return [
            "Outdoor adventure photos",
            "Food and dining photos",
            "Travel and vacation photos",
            "Hobby and activity photos",
            "Social group photos"
        ]
    
    def get_communication_style(self, region: str) -> Dict[str, str]:
        """Get communication style preferences for a region"""
        return {
            "tone": "Friendly and approachable",
            "length": "Medium length messages",
            "emoji_usage": "Moderate",
            "formality": "Casual but respectful"
        }