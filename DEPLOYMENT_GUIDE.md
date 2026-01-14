# Flight Search AI Agent - Deployment Guide

## 🚀 **CHEAPEST HOSTING OPTION: Railway.app**

**Cost: FREE tier available, then ~$5/month**
- Free 500 hours/month (enough for testing)
- $5/month for hobby tier (unlimited)
- Auto-deploys from GitHub
- Built-in environment variables
- Easiest setup

---

## 📋 Prerequisites

1. **Anthropic API Key** (FREE $5 credit to start)
   - Sign up at: https://console.anthropic.com
   - Get API key from dashboard
   - Cost: ~$0.003 per itinerary request

2. **SerpAPI Key** (100 free searches/month)
   - Sign up at: https://serpapi.com
   - Get free API key
   - Upgrade to $50/month for 5,000 searches if needed

---

## 🎯 Quick Deploy to Railway (RECOMMENDED)

### Step 1: Prepare Your Code
```bash
# Create a new GitHub repository and push this code
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy on Railway
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect the Dockerfile

### Step 3: Add Environment Variables
In Railway dashboard:
1. Go to your project → Variables
2. Add:
   - `ANTHROPIC_API_KEY`: your_key_here
   - `SERPAPI_KEY`: your_key_here
   - `PORT`: 8080

### Step 4: Deploy
- Railway will automatically build and deploy
- You'll get a URL like: `your-app.railway.app`

**Total Cost: FREE for testing, $5/month for production**

---

## 🔧 Alternative Hosting Options

### Option 2: Google Cloud Run (Pay-per-use)
**Cost: FREE tier (2 million requests/month), then ~$0.40 per million requests**

```bash
# Install Google Cloud SDK
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy flight-agent \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --set-env-vars ANTHROPIC_API_KEY=xxx,SERPAPI_KEY=xxx
```

**Pros**: Only pay when used, extremely cheap
**Cons**: Requires Google Cloud account setup

---

### Option 3: Render.com (Free tier)
**Cost: FREE tier available, $7/month for always-on**

1. Go to https://render.com
2. Connect GitHub repository
3. Create "Web Service"
4. Set environment variables
5. Deploy

**Pros**: Simple, free tier available
**Cons**: Free tier spins down after 15 mins of inactivity

---

### Option 4: Fly.io (Very cheap)
**Cost: FREE for 3 small VMs, ~$2/month beyond that**

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Launch app
flyctl launch
flyctl secrets set ANTHROPIC_API_KEY=xxx SERPAPI_KEY=xxx
flyctl deploy
```

**Pros**: Extremely cheap, fast global deployment
**Cons**: Requires CLI setup

---

## 💰 Cost Breakdown (Monthly)

### Ultra-Budget Setup (FREE - $10/month)
- **Hosting**: Railway FREE tier or Render FREE tier
- **Anthropic API**: $0-5 (depending on usage)
- **SerpAPI**: FREE (100 searches) or $50 (5,000 searches)
- **Total**: $0-10/month for light usage

### Production Setup ($50-60/month)
- **Hosting**: Railway Hobby $5
- **Anthropic API**: $5-10
- **SerpAPI**: $50/month (5,000 searches)
- **Total**: $60-65/month

---

## 📱 API Usage Examples

### 1. Search for Best Value Flights
```bash
curl -X POST https://your-app.railway.app/search \
  -H "Content-Type: application/json" \
  -d '{
    "origin": "LHR",
    "destination": "BCN",
    "start_date": "2025-03-01",
    "flexible_days": 14,
    "max_price": 200
  }'
```

**Response:**
```json
{
  "origin": "LHR",
  "destination": "BCN",
  "total_options_found": 45,
  "best_value_flights": [
    {
      "date": "2025-03-05",
      "price": 89,
      "duration": 140,
      "airline": "Ryanair"
    }
  ],
  "average_price": 134.50,
  "price_range": {
    "min": 89,
    "max": 245
  }
}
```

### 2. Create AI-Powered Itinerary
```bash
curl -X POST https://your-app.railway.app/itinerary \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Barcelona",
    "keywords": ["food", "architecture", "beach", "nightlife"],
    "budget": 1000,
    "duration_days": 5,
    "origin": "LHR",
    "start_date": "2025-03-01"
  }'
```

**Response:**
```json
{
  "destination": "Barcelona",
  "keywords": ["food", "architecture", "beach", "nightlife"],
  "total_budget": 1000,
  "flight_options": [...],
  "recommended_flight_cost": 89,
  "remaining_budget": 911,
  "itinerary": "Day 1: Arrive in Barcelona... [full AI-generated itinerary]"
}
```

---

## 🎨 Frontend Integration Ideas

### Simple HTML Form
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flight Search AI</title>
</head>
<body>
    <h1>Find Your Perfect Trip</h1>
    <form id="searchForm">
        <input type="text" name="origin" placeholder="From (e.g., LHR)" required>
        <input type="text" name="destination" placeholder="To (e.g., BCN)" required>
        <input type="date" name="start_date" required>
        <input type="number" name="budget" placeholder="Budget (£)" required>
        <input type="text" name="keywords" placeholder="Keywords: food, beach, culture">
        <button type="submit">Search</button>
    </form>
    
    <div id="results"></div>
    
    <script>
        document.getElementById('searchForm').onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                origin: formData.get('origin'),
                destination: formData.get('destination'),
                start_date: formData.get('start_date'),
                budget: parseInt(formData.get('budget')),
                keywords: formData.get('keywords').split(',').map(k => k.trim()),
                duration_days: 5
            };
            
            const response = await fetch('https://your-app.railway.app/itinerary', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            document.getElementById('results').innerHTML = 
                `<pre>${JSON.stringify(result, null, 2)}</pre>`;
        };
    </script>
</body>
</html>
```

---

## 🔐 Security Notes

1. **Never commit API keys** - Use environment variables
2. **Add rate limiting** for production use
3. **Consider adding authentication** if needed
4. **Monitor API usage** to avoid surprise costs

---

## 📈 Scaling Tips

1. **Cache results**: Add Redis for frequently searched routes
2. **Background jobs**: Use Celery for async flight searches
3. **Database**: Add PostgreSQL to store historical price data
4. **Monitoring**: Use Railway metrics or add Sentry

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "API key not found"
- Check environment variables are set correctly
- Verify .env file exists (for local testing)

### "No flights found"
- Verify airport codes (use IATA codes: LHR, JFK, etc.)
- Check date format is YYYY-MM-DD
- Ensure SerpAPI key is valid

---

## 🎯 Next Steps for Your Business

Given your tenant referencing background, you could:

1. **MVP Testing Phase (Month 1-2)**
   - Deploy on Railway FREE tier
   - Share with 10-20 friends for feedback
   - Cost: £0-5/month

2. **Lean Launch (Month 3)**
   - Upgrade to Railway Hobby ($5)
   - Add simple landing page (Carrd - $19/year)
   - Start small marketing
   - Cost: £10-15/month

3. **Growth Phase (Month 4+)**
   - Scale to Google Cloud Run (pay-per-use)
   - Add email notifications
   - Build simple frontend
   - Cost: £20-50/month depending on traffic

This follows the same lean validation approach you're using for tenant referencing - start manual/simple, validate demand, then automate!
