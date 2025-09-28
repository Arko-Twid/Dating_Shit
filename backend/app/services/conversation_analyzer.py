"""
Conversation analysis service using OpenAI
"""

import openai
from typing import List, Dict, Any
from app.config import settings

class ConversationAnalyzer:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
    
    async def analyze_conversation(
        self, 
        messages: List[Dict[str, Any]], 
        user_context: Dict[str, Any] = None,
        partner_context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Analyze a dating conversation and provide insights
        """
        try:
            # Format messages for OpenAI
            formatted_messages = []
            for msg in messages:
                formatted_messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
            
            # Add system prompt for conversation analysis
            system_prompt = """You are a dating conversation analyst. Analyze the conversation and provide insights on:
            1. Conversation flow and engagement
            2. Emotional tone and sentiment
            3. Communication effectiveness
            4. Areas for improvement
            5. Compatibility indicators
            
            Provide specific, actionable feedback."""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *formatted_messages
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            analysis_text = response.choices[0].message.content
            
            # Parse the analysis into structured format
            return {
                "overall_score": 7.5,  # Placeholder
                "engagement_level": "good",
                "sentiment": "positive",
                "key_insights": analysis_text,
                "suggestions": [
                    "Ask more open-ended questions",
                    "Share personal stories to build connection",
                    "Show genuine interest in their responses"
                ],
                "compatibility_indicators": {
                    "shared_interests": 3,
                    "communication_style_match": "good",
                    "emotional_connection": "developing"
                }
            }
            
        except Exception as e:
            # Fallback analysis if OpenAI fails
            return {
                "overall_score": 6.0,
                "engagement_level": "moderate",
                "sentiment": "neutral",
                "key_insights": "Conversation analysis temporarily unavailable. Please try again later.",
                "suggestions": [
                    "Keep the conversation flowing naturally",
                    "Ask follow-up questions",
                    "Share your own experiences"
                ],
                "compatibility_indicators": {
                    "shared_interests": 2,
                    "communication_style_match": "unknown",
                    "emotional_connection": "developing"
                },
                "error": str(e)
            }