# 💕 Dating Conversation Assistant

An AI-powered dating conversation analyzer and profile optimizer that helps users improve their dating app success through intelligent conversation insights, smart suggestions, and profile optimization.

![Dating Assistant Interface](https://github.com/user-attachments/assets/faeb8d53-7142-41cc-8043-19e3e740c3a3)

## 🌟 Key Features

### 🤖 AI-Powered Conversation Analysis
- **Real-time Analysis**: Get instant insights into your dating conversations
- **Engagement Scoring**: Measure conversation quality and engagement levels
- **Flow Analysis**: Understand conversation dynamics and pacing
- **Sentiment Detection**: Analyze emotional tone and compatibility indicators

### 💡 Smart Suggestion Engine
- **Context-Aware Suggestions**: Get personalized conversation starters and responses
- **Quick Response Templates**: Access pre-built responses for common scenarios
- **Topic Recommendations**: Discover engaging topics based on conversation context
- **Timing Optimization**: Learn when and how to respond for maximum impact

### 📸 Profile Optimization
- **Bio Enhancement**: AI-powered bio writing and improvement suggestions
- **Photo Analysis**: Get feedback on photo selection and ordering
- **Appeal Optimization**: Tailor your profile to attract your ideal matches
- **Regional Customization**: Adapt your profile for local dating preferences

### 📊 Regional Trend Analysis
- **Location-Based Insights**: Understand dating trends in your area
- **Popular Topics**: Discover what's trending in your region
- **Communication Styles**: Learn preferred conversation styles by location
- **Success Patterns**: Analyze what works best in your demographic

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL
- Redis
- OpenAI API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arko-Twid/Dating_Shit.git
   cd Dating_Shit
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key and database credentials
   ```

3. **Install dependencies**
   ```bash
   # Backend dependencies
   cd backend
   pip install -r ../requirements.txt
   cd ..
   ```

4. **Start services**
   ```bash
   # Start PostgreSQL and Redis
   # On macOS with Homebrew:
   brew services start postgresql redis
   
   # Create database
   createdb dating_assistant
   ```

5. **Run the application**
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

**Note:** The application currently includes a frontend mockup (`frontend_mockup.html`) that demonstrates the user interface design. The backend API is fully functional and ready for frontend integration.

## 🔧 Configuration

Create a `.env` file with the following configuration:

```env
# OpenAI Configuration (REQUIRED)
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/dating_assistant
REDIS_URL=redis://localhost:6379

# Application Configuration
SECRET_KEY=your_secret_key_here
DEBUG=True
ENVIRONMENT=development

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
```

## 📚 API Documentation

### Core Endpoints

#### Conversation Analysis
```http
POST /analyze-conversation
```
Analyze a dating conversation and get detailed insights.

**Request Body:**
```json
{
  "messages": [
    {"role": "user", "content": "Hey, how's your day going?"},
    {"role": "partner", "content": "Great! Just finished a morning run."}
  ],
  "user_context": {"age": 25, "interests": ["fitness", "travel"]},
  "partner_context": {"age": 24, "interests": ["running", "photography"]}
}
```

**Response:**
```json
{
  "analysis": {
    "engagement_score": 8.5,
    "sentiment": "positive",
    "topics": ["lifestyle", "fitness"],
    "compatibility_indicators": ["shared_interests"],
    "suggestions": ["Ask about favorite running routes"]
  }
}
```

#### Get Suggestions
```http
POST /get-suggestions
```
Get AI-powered conversation suggestions.

**Request Body:**
```json
{
  "conversation_context": {
    "current_topic": "travel",
    "last_message": "I love exploring new places!"
  },
  "user_preferences": {
    "style": "casual",
    "interests": ["travel", "food"]
  },
  "suggestion_type": "follow_up"
}
```

#### Profile Optimization
```http
POST /optimize-profile
```
Get profile improvement recommendations.

**Request Body:**
```json
{
  "photos": ["photo1.jpg", "photo2.jpg"],
  "bio": "Love to travel and try new foods!",
  "preferences": {"age_range": [22, 30]},
  "region": "San Francisco"
}
```

#### Regional Trends
```http
GET /trends/{region}
```
Get dating trends for a specific region.

```http
POST /analyze-trends
```
Analyze detailed regional dating patterns.

#### Quick Suggestions
```http
GET /quick-suggestions/{message_type}
```
Get quick suggestions for common message types (`opening`, `follow_up`, `date_request`, etc.).

#### Health Check
```http
GET /health
```
Check API status and service availability.

## 🎯 Usage Examples

### Analyzing a Conversation

```python
import requests

# Analyze conversation
response = requests.post("http://localhost:8000/analyze-conversation", json={
    "messages": [
        {"role": "user", "content": "Hi! I saw you like hiking too!"},
        {"role": "partner", "content": "Yes! I actually just got back from Yosemite"}
    ]
})

analysis = response.json()
print(f"Engagement Score: {analysis['engagement_score']}")
print(f"Suggestions: {analysis['suggestions']}")
```

### Getting Quick Suggestions

```python
# Get opening message suggestions
response = requests.get("http://localhost:8000/quick-suggestions/opening")
suggestions = response.json()["suggestions"]

for suggestion in suggestions:
    print(f"• {suggestion}")
```

### Profile Optimization

```python
# Optimize dating profile
response = requests.post("http://localhost:8000/optimize-profile", json={
    "bio": "Love dogs and coffee ☕🐕",
    "photos": ["selfie.jpg", "dog_pic.jpg", "coffee_shop.jpg"],
    "region": "New York"
})

optimization = response.json()
print("Bio Suggestions:", optimization["bio_suggestions"])
print("Photo Tips:", optimization["photo_tips"])
```

## 🏗️ Project Status

**Current State:**
- ✅ **Backend API**: Fully functional with all core features
- ✅ **AI Services**: Complete conversation analysis, suggestions, profile optimization, and trend analysis
- ✅ **API Documentation**: Interactive Swagger UI available
- ✅ **Frontend Design**: Beautiful mockup showcasing the user interface
- 🚧 **Frontend Implementation**: Ready for development (mockup available as reference)

The backend is production-ready and the frontend mockup provides a clear vision for the user interface. Frontend developers can use the mockup and API documentation to build the complete user experience.

## 🏗️ Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.9+**: Core programming language
- **OpenAI GPT**: AI-powered conversation analysis and suggestions
- **PostgreSQL**: Primary database for user data and analytics
- **Redis**: Caching and session management
- **SQLAlchemy**: Database ORM
- **Pydantic**: Data validation and settings management

### AI & Machine Learning
- **OpenAI API**: GPT-3.5/GPT-4 for natural language processing
- **Custom Prompts**: Specialized prompts for dating conversation analysis
- **Sentiment Analysis**: Emotion and tone detection
- **Pattern Recognition**: Conversation flow and success pattern analysis

### Infrastructure
- **Uvicorn**: ASGI server for FastAPI
- **Docker**: Containerization support
- **CORS**: Cross-origin resource sharing configuration
- **Environment Configuration**: Secure config management

## 🔍 Core Services

### ConversationAnalyzer
Analyzes dating conversations to provide insights on:
- Engagement quality and flow
- Sentiment and emotional tone
- Topic relevance and progression
- Compatibility indicators
- Response timing optimization

### SuggestionEngine
Generates intelligent conversation suggestions:
- Context-aware responses
- Topic transitions
- Question recommendations
- Conversation starters
- Follow-up strategies

### ProfileOptimizer
Optimizes dating profiles for better results:
- Bio writing and enhancement
- Photo selection and ordering
- Profile completeness scoring
- Target audience appeal
- Regional customization

### TrendAnalyzer
Analyzes regional dating trends:
- Popular conversation topics
- Communication style preferences
- Photo and profile trends
- Success patterns by location
- Demographic insights

## 🧪 Testing

### Health Check
```bash
curl http://localhost:8000/health
```

### Test Conversation Analysis
```bash
curl -X POST http://localhost:8000/analyze-conversation \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hey there!"},
      {"role": "partner", "content": "Hi! How are you?"}
    ]
  }'
```

### Interactive API Testing
Visit http://localhost:8000/docs for Swagger UI with interactive API testing.

## 🔒 Security & Privacy

- **API Key Protection**: OpenAI API key securely stored in environment variables
- **Data Privacy**: User conversations are processed but not permanently stored
- **CORS Configuration**: Controlled cross-origin access
- **Input Validation**: All inputs validated using Pydantic models
- **Error Handling**: Comprehensive error handling without data leaks

## 📈 Performance

- **Async Operations**: Non-blocking conversation analysis
- **Caching**: Redis caching for improved response times
- **Database Optimization**: Efficient queries with SQLAlchemy
- **Rate Limiting**: Built-in protection against API abuse
- **Scalable Architecture**: Designed for horizontal scaling

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** for new functionality
5. **Ensure all tests pass**
6. **Submit a pull request**

### Development Setup
1. Follow the installation guide above
2. Install development dependencies
3. Run tests: `python -m pytest`
4. Check code style: `flake8`
5. Format code: `black .`

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write comprehensive docstrings
- Add tests for new features

## 🐛 Troubleshooting

### Common Issues

**OpenAI API Key Issues**
- Verify your API key is correct and has sufficient credits
- Check the key has necessary permissions
- Ensure it's properly set in the `.env` file

**Database Connection Problems**
- Verify PostgreSQL is running
- Check database credentials in `.env`
- Ensure the `dating_assistant` database exists

**Port Already in Use**
- Change the port in `.env` file
- Kill processes: `lsof -ti:8000 | xargs kill -9`

**CORS Issues**
- Check `ALLOWED_ORIGINS` in `.env`
- Ensure frontend URL is included

### Getting Help
- Check the [Issues](https://github.com/Arko-Twid/Dating_Shit/issues) page
- Review API logs for detailed error messages
- Verify all environment variables are set correctly
- Ensure all services (PostgreSQL, Redis) are running

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **FastAPI** community for the excellent framework
- **Contributors** who help improve this project
- **Dating app users** who inspired this solution

## 🔗 Links

- **Documentation**: http://localhost:8000/docs
- **Repository**: https://github.com/Arko-Twid/Dating_Shit
- **Issues**: https://github.com/Arko-Twid/Dating_Shit/issues
- **OpenAI API**: https://platform.openai.com/docs

---

Made with ❤️ to help people find meaningful connections through better conversations.