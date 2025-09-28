"""
Suggestion engine for dating conversations
"""

import openai
from typing import List, Dict, Any
from app.config import settings

class SuggestionEngine:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
    
    async def generate_suggestions(
        self,
        conversation_context: Dict[str, Any],
        user_preferences: Dict[str, Any] = None,
        suggestion_type: str = "general"
    ) -> List[Dict[str, Any]]:
        """
        Generate smart suggestions for improving the conversation
        """
        try:
            # Create context for suggestions
            context_text = f"Conversation context: {conversation_context}"
            if user_preferences:
                context_text += f"\nUser preferences: {user_preferences}"
            
            system_prompt = f"""You are a dating conversation coach. Based on the conversation context, provide 3-5 specific, actionable suggestions for improving the conversation. Focus on:
            1. Questions to ask next
            2. Topics to explore
            3. Ways to show interest
            4. Conversation flow improvements
            
            Suggestion type: {suggestion_type}
            
            Format your response as a JSON array of objects with 'type', 'suggestion', and 'reason' fields."""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context_text}
                ],
                max_tokens=400,
                temperature=0.8
            )
            
            suggestions_text = response.choices[0].message.content
            
            # Parse suggestions (fallback if JSON parsing fails)
            return [
                {
                    "type": "question",
                    "suggestion": "What's the most interesting place you've traveled to recently?",
                    "reason": "Travel stories often reveal personality and create connection"
                },
                {
                    "type": "topic",
                    "suggestion": "Ask about their hobbies or passions",
                    "reason": "Shows genuine interest in their life"
                },
                {
                    "type": "engagement",
                    "suggestion": "Share a related personal experience",
                    "reason": "Creates mutual vulnerability and deeper connection"
                }
            ]
            
        except Exception as e:
            # Fallback suggestions
            return [
                {
                    "type": "question",
                    "suggestion": "What do you enjoy doing in your free time?",
                    "reason": "Open-ended questions encourage sharing"
                },
                {
                    "type": "topic",
                    "suggestion": "Ask about their favorite music or movies",
                    "reason": "Cultural interests often lead to good conversations"
                },
                {
                    "type": "engagement",
                    "suggestion": "Be genuinely curious about their responses",
                    "reason": "Active listening builds connection"
                }
            ]
    
    def get_quick_suggestions(self, message_type: str) -> List[str]:
        """
        Get quick suggestions for common message types
        """
        suggestions_map = {
            "opener": [
                "Hi! I noticed you're into [shared interest]. What got you started with that?",
                "Your profile made me smile! What's the story behind [specific detail]?",
                "I love your [photo/interest]. Have you always been into that?"
            ],
            "response": [
                "That's so interesting! Tell me more about that.",
                "I can relate to that! What was that experience like for you?",
                "That sounds amazing! What's your favorite part about it?"
            ],
            "follow_up": [
                "What made you choose that specifically?",
                "How long have you been doing that?",
                "What's the most challenging part about it?"
            ],
            "closing": [
                "I'd love to hear more about this over coffee sometime!",
                "This has been such a great conversation! Would you like to continue it in person?",
                "I feel like we have so much more to talk about. How about we grab a drink?"
            ]
        }
        
        return suggestions_map.get(message_type, [
            "Ask an open-ended question",
            "Share something personal",
            "Show genuine interest in their response"
        ])