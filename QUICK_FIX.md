# 🔧 QUICK FIX - Your Deployment Issue

## The Problem

Your files have wrong names:
- ❌ `index (2).html` (wrong)
- ❌ `Dockerfile (1)` (duplicate)
- ❌ `test_agent (1).py` (wrong)

These need to be:
- ✅ `index.html`
- ✅ `Dockerfile` (only one)
- ✅ `test_agent.py`

---

## 🚀 Fix It in 3 Steps

### Step 1: Rename Files in Your Folder

**On Windows:**
1. Open your project folder
2. Right-click `index (2).html` → Rename → `index.html`
3. Delete `Dockerfile (1)` (keep the original Dockerfile)
4. Right-click `test_agent (1).py` → Rename → `test_agent.py`

**On Mac:**
1. Open your project folder in Finder
2. Click on `index (2).html` once, press Enter, rename to `index.html`
3. Delete `Dockerfile (1)` (keep the original)
4. Click on `test_agent (1).py` once, press Enter, rename to `test_agent.py`

### Step 2: Replace flight_agent.py

1. Download the NEW `flight_agent.py` file I just created (above)
2. Replace your old `flight_agent.py` with this new one
3. This new version serves the HTML file automatically

### Step 3: Push to GitHub

**Using GitHub Desktop:**
1. Open GitHub Desktop
2. You'll see the changes
3. Write commit message: "Fix file names and add HTML serving"
4. Click "Commit to main"
5. Click "Push origin"

**Using Command Line:**
```bash
git add .
git commit -m "Fix file names and add HTML serving"
git push
```

Railway will automatically redeploy in ~30 seconds!

---

## ✅ What Should Work After Fix

1. Visit your Railway URL: `https://your-app.railway.app`
2. You should see the **beautiful purple form** (not JSON)
3. Fill it in and click "Find Best Flights"
4. Get results in 10-20 seconds!

---

## 📋 Your Final File List Should Be:

```
AI-Flight-checker-main/
├── .gitignore
├── DEPLOYMENT_GUIDE.md
├── Dockerfile                    ✅ (only one)
├── GITHUB_GUIDE.md
├── README.md
├── flight_agent.py              ✅ (NEW VERSION)
├── index.html                   ✅ (renamed from index (2).html)
├── requirements.txt
└── test_agent.py                ✅ (renamed from test_agent (1).py)
```

---

## 🐛 Still Not Working?

### Check Railway Logs:
1. Go to Railway dashboard
2. Click your project
3. Click "Logs" tab
4. Look for errors

### Common Issues:

**"Module not found"**
- Make sure `requirements.txt` is pushed
- Railway should auto-install packages

**"API key not found"**
- Check environment variables in Railway dashboard
- Make sure they're named exactly:
  - `ANTHROPIC_API_KEY`
  - `SERPAPI_KEY`

**Still seeing JSON response**
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Try in incognito/private mode
- Make sure `index.html` exists (check Railway logs)

---

## 💡 Quick Test

After you push, test the API directly:

```bash
# Replace YOUR_RAILWAY_URL with your actual URL
curl -X POST https://YOUR_RAILWAY_URL/itinerary \
  -H "Content-Type: application/json" \
  -d '{
    "origin": "LHR",
    "destination": "BCN",
    "start_date": "2025-03-15",
    "duration_days": 3,
    "budget": 500,
    "keywords": ["food", "beach"]
  }'
```

You should get a JSON response with flight options and an itinerary!

---

## 🎯 Summary

1. ✅ Rename `index (2).html` → `index.html`
2. ✅ Replace `flight_agent.py` with new version
3. ✅ Delete duplicate files
4. ✅ Git commit and push
5. ✅ Wait 30 seconds for Railway to redeploy
6. ✅ Visit your URL and see the form!

The issue is just file naming - once fixed, everything will work perfectly!
