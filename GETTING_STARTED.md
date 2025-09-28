# Getting Started with Dating Conversation Assistant

## 🚀 Quick Start Guide

This guide will help you get the Dating Conversation Assistant app running locally for development and testing.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** - [Download Node.js](https://nodejs.org/)
- **PostgreSQL** - [Download PostgreSQL](https://www.postgresql.org/download/)
- **Redis** - [Download Redis](https://redis.io/download)

## 🔑 Getting Your OpenAI API Key

### Step 1: Create OpenAI Account
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up for an account or sign in
3. Complete email verification

### Step 2: Get API Access
1. Navigate to the API section
2. Request API access (may require approval)
3. Add a payment method (required for API usage)

### Step 3: Generate API Key
1. Go to [API Keys section](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Copy and securely store your key
4. **Important**: Never share this key publicly!

## 🛠️ Installation

### 1. Clone and Setup
```bash
# Clone the repository
git clone <your-repository-url>
cd dating-assistant-app

# Install dependencies
npm install
```

### 2. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
nano .env
```

### 3. Configure Environment Variables
Edit the `.env` file with your settings:

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

### 4. Database Setup
```bash
# Start PostgreSQL and Redis services
# On macOS with Homebrew:
brew services start postgresql
brew services start redis

# On Ubuntu/Debian:
sudo systemctl start postgresql
sudo systemctl start redis

# Create database
createdb dating_assistant
```

### 5. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 6. Install Frontend Dependencies
```bash
cd frontend
npm install
```

## 🚀 Running the Application

### Option 1: Run Everything Together
```bash
# From the root directory
npm run dev
```

### Option 2: Run Backend and Frontend Separately

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

## 🧪 Testing the Application

### 1. Check API Health
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00",
  "services": {
    "conversation_analyzer": "active",
    "suggestion_engine": "active",
    "profile_optimizer": "active",
    "trend_analyzer": "active"
  },
  "configuration": {
    "openai_configured": true,
    "debug_mode": true,
    "environment": "development"
  }
}
```

### 2. Test Conversation Analysis
```bash
curl -X POST "http://localhost:8000/analyze-conversation" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "test_123",
    "messages": [
      {
        "sender": "You",
        "content": "Hey! I love your profile photos",
        "timestamp": "2024-01-01T10:00:00"
      },
      {
        "sender": "Partner",
        "content": "Thank you! I took them on my recent trip to Japan",
        "timestamp": "2024-01-01T10:01:00"
      }
    ],
    "user_context": {
      "age": 28,
      "interests": ["travel", "photography"]
    }
  }'
```

### 3. Test Suggestion Generation
```bash
curl -X POST "http://localhost:8000/get-suggestions" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "test_123",
    "conversation_context": {
      "recent_messages": "Partner mentioned Japan trip",
      "stage": "getting_to_know"
    },
    "suggestion_type": "response"
  }'
```

## 🌐 Accessing the Application

- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000 (when running)

## 🔧 Development Commands

```bash
# Run tests
npm test

# Lint code
npm run lint

# Build for production
npm run build

# Run backend only
npm run backend:dev

# Run frontend only
npm run frontend:dev
```

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Not Working**
   - Verify your API key is correct
   - Check if you have sufficient credits
   - Ensure the key has the necessary permissions

2. **Database Connection Issues**
   - Verify PostgreSQL is running
   - Check database credentials in `.env`
   - Ensure the database exists

3. **Port Already in Use**
   - Change the port in `.env` file
   - Kill processes using the port: `lsof -ti:8000 | xargs kill -9`

4. **CORS Issues**
   - Check `ALLOWED_ORIGINS` in `.env`
   - Ensure frontend URL is included

### Getting Help

- Check the logs for detailed error messages
- Verify all environment variables are set correctly
- Ensure all dependencies are installed
- Check that all services (PostgreSQL, Redis) are running

## 📚 Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs for interactive API documentation
2. **Test Features**: Try the conversation analyzer and suggestion engine
3. **Customize**: Modify the AI prompts and suggestions to fit your needs
4. **Deploy**: Follow the deployment guide when ready for production

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and private
- Use strong passwords for database connections
- Enable HTTPS in production environments

## 💡 Tips for Development

- Use the mock responses when OpenAI is not configured
- Test with different conversation scenarios
- Experiment with different suggestion types
- Monitor API usage and costs
- Use the health check endpoint to verify services

Happy coding! 🚀