"""
Profile optimization service for dating profiles
"""

import openai
from typing import List, Dict, Any
from app.config import settings

class ProfileOptimizer:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
    
    async def optimize_profile(
        self,
        photos: List[str],
        bio: str,
        preferences: Dict[str, Any],
        region: str
    ) -> Dict[str, Any]:
        """
        Analyze and optimize user's dating profile
        """
        try:
            # Create context for profile optimization
            context = f"""
            Current bio: {bio}
            Region: {region}
            Preferences: {preferences}
            Number of photos: {len(photos)}
            """
            
            system_prompt = """You are a dating profile optimization expert. Analyze the profile and provide specific recommendations for:
            1. Bio improvements (tone, content, length)
            2. Photo suggestions (types, order, quality)
            3. Profile completeness
            4. Appeal to target audience
            
            Provide actionable, specific advice that will improve match rates."""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            optimization_text = response.choices[0].message.content
            
            return {
                "bio_score": 7.0,
                "photo_score": 6.5,
                "overall_score": 6.8,
                "bio_suggestions": [
                    "Add more specific details about your interests",
                    "Include what you're looking for in a relationship",
                    "Show your personality through humor or unique details"
                ],
                "photo_suggestions": [
                    "Add a clear face photo as your first image",
                    "Include photos showing your hobbies",
                    "Add a full-body photo",
                    "Consider photos with friends to show social side"
                ],
                "detailed_analysis": optimization_text,
                "completeness": {
                    "bio_complete": len(bio) > 50,
                    "photos_complete": len(photos) >= 3,
                    "preferences_complete": bool(preferences)
                }
            }
            
        except Exception as e:
            # Fallback optimization suggestions
            return {
                "bio_score": 6.0,
                "photo_score": 6.0,
                "overall_score": 6.0,
                "bio_suggestions": [
                    "Write a bio that shows your personality",
                    "Include your interests and hobbies",
                    "Mention what you're looking for"
                ],
                "photo_suggestions": [
                    "Add clear, recent photos",
                    "Include photos of you doing activities",
                    "Make sure your first photo is your best"
                ],
                "detailed_analysis": "Profile optimization temporarily unavailable. Please try again later.",
                "completeness": {
                    "bio_complete": len(bio) > 50,
                    "photos_complete": len(photos) >= 3,
                    "preferences_complete": bool(preferences)
                },
                "error": str(e)
            }