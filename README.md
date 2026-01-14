# ✈️ AI Flight Search Agent

An intelligent flight search agent that finds the best value flights by analyzing price patterns across flexible dates, removing demand pricing influence, and creating personalized itineraries based on your interests.

## 🎯 Features

- **Smart Price Analysis**: Searches across multiple dates to find lowest prices
- **Demand Pricing Removal**: Identifies and filters out artificially inflated prices
- **AI-Powered Itineraries**: Creates detailed trip plans based on your keywords and budget
- **Flexible Date Search**: Automatically searches up to 14 days to find best deals
- **Budget Optimization**: Shows you exactly how much you have left after flights

## 🚀 Quickest Deploy (2 minutes)

### Railway.app (Recommended - FREE tier)

1. **Fork this repo** to your GitHub
2. Go to [Railway.app](https://railway.app) and sign up
3. Click "New Project" → "Deploy from GitHub"
4. Select this repository
5. Add environment variables:
   - `ANTHROPIC_API_KEY` - Get from [console.anthropic.com](https://console.anthropic.com)
   - `SERPAPI_KEY` - Get from [serpapi.com](https://serpapi.com) (100 free searches/month)
6. Deploy automatically starts!

**Cost: FREE** (500 hours/month), or $5/month for unlimited

## 💻 Local Testing

```bash
# Clone the repository
git clone <your-repo>
cd flight-agent

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your API keys

# Run locally
python flight_agent.py
```

Visit `http://localhost:8080`

## 📡 API Endpoints

### POST `/search` - Find Best Value Flights

Searches across flexible dates to find the best deals:

```bash
curl -X POST http://localhost:8080/search \
  -H "Content-Type: application/json" \
  -d '{
    "origin": "LHR",
    "destination": "BCN", 
    "start_date": "2025-03-01",
    "flexible_days": 14,
    "max_price": 200
  }'
```

**Returns:**
- All flight options found across date range
- Best value flights (below average price)
- Price analysis (average, min, max)
- Recommended travel dates

### POST `/itinerary` - Create AI Itinerary

Combines flight search with AI-powered trip planning:

```bash
curl -X POST http://localhost:8080/itinerary \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Barcelona",
    "keywords": ["food", "architecture", "beach"],
    "budget": 1000,
    "duration_days": 5,
    "origin": "LHR",
    "start_date": "2025-03-01"
  }'
```

**Returns:**
- Best flight options
- Recommended flight + cost
- Remaining budget after flights
- Day-by-day AI-generated itinerary based on your keywords
- Budget breakdown per activity

## 🎨 How It Works

### 1. Smart Price Analysis
The agent searches multiple dates (e.g., 14 days) and calculates:
- Average price across all dates
- Identifies flights below average (avoiding demand pricing spikes)
- Returns only the best value options

### 2. Demand Pricing Removal
Traditional search shows whatever's available on your chosen date (often expensive). This agent:
- Searches flexible dates automatically
- Filters out artificially high prices
- Shows you when to fly for best value

### 3. AI Itinerary Generation
Uses Claude AI to create personalized trip plans:
- Analyzes your keywords (food, adventure, culture, etc.)
- Matches activities to your interests
- Provides cost estimates for each activity
- Optimizes for your budget

## 💰 Cost Breakdown

### Development/Testing
- **Hosting**: FREE (Railway free tier)
- **Anthropic API**: ~$0.003 per itinerary (comes with $5 free credit)
- **SerpAPI**: FREE (100 searches/month)
- **Total**: $0/month

### Light Production Use
- **Hosting**: $5/month (Railway hobby tier)
- **Anthropic API**: ~$5-10/month
- **SerpAPI**: FREE (100 searches/month)
- **Total**: ~$10-15/month

### Heavy Production Use
- **Hosting**: $5/month (Railway) or $0.40 per million requests (Google Cloud Run)
- **Anthropic API**: ~$10-20/month
- **SerpAPI**: $50/month (5,000 searches)
- **Total**: ~$65-75/month

## 🔑 Getting API Keys

### Anthropic API (Claude AI)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up (get $5 free credit)
3. Create API key
4. Cost: ~$3 per 1,000 itinerary requests

### SerpAPI (Flight Data)
1. Go to [serpapi.com](https://serpapi.com)
2. Sign up for free account
3. Get API key (100 free searches/month)
4. Upgrade to $50/month for 5,000 searches if needed

## 📱 Example Use Cases

**Budget Backpacker**
```json
{
  "origin": "LHR",
  "destination": "Bangkok",
  "keywords": ["street food", "temples", "cheap accommodation"],
  "budget": 800,
  "duration_days": 10
}
```

**Foodie Weekend**
```json
{
  "origin": "LHR", 
  "destination": "Lyon",
  "keywords": ["michelin restaurants", "wine tasting", "local markets"],
  "budget": 600,
  "duration_days": 3
}
```

**Architecture Tour**
```json
{
  "origin": "LHR",
  "destination": "Barcelona", 
  "keywords": ["gaudi", "architecture", "modernism"],
  "budget": 900,
  "duration_days": 4
}
```

## 🎓 Learning from Your Tenant Referencing MVP

This follows the same lean principles:

**Phase 1 (Weeks 1-2): Manual Validation**
- Deploy on free tier
- Test with friends/family
- Manually verify results
- Gather feedback

**Phase 2 (Month 2): Lean Automation**
- Add result caching
- Improve price analysis algorithm
- Build simple frontend

**Phase 3 (Month 3+): Scale**
- Add database for price history
- Implement price alerts
- Build subscription model

Just like your tenant referencing service - validate demand before heavy investment!

## 📈 Potential Revenue Models

1. **Freemium**: 3 free searches/month, £5/month unlimited
2. **Pay-per-search**: £1 per complete itinerary
3. **Affiliate**: Earn commission on bookings (integrate booking.com API)
4. **B2B**: License to travel agencies

## 🔧 Tech Stack

- **Backend**: Python Flask
- **AI**: Anthropic Claude Sonnet 4
- **Flight Data**: SerpAPI (Google Flights)
- **Hosting**: Railway.app / Google Cloud Run / Fly.io
- **Container**: Docker

## 📝 License

MIT - Use it however you want!

## 🤝 Contributing

Pull requests welcome! Areas to improve:
- Add more flight data sources
- Implement price history tracking
- Build frontend interface
- Add email notifications for price drops

---

**Questions?** Open an issue or reach out!
