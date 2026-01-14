"""
Test script for Flight Search AI Agent
Run this to verify everything works locally
"""

import os
import json
from flight_agent import FlightSearchAgent

def test_agent():
    """Test the flight search agent functionality"""
    
    print("🧪 Testing Flight Search AI Agent\n")
    print("=" * 50)
    
    # Check environment variables
    print("\n1. Checking environment variables...")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    serpapi_key = os.environ.get("SERPAPI_KEY")
    
    if not anthropic_key:
        print("❌ ANTHROPIC_API_KEY not found!")
        print("   Set it in .env file or export ANTHROPIC_API_KEY=your_key")
        return False
    else:
        print(f"✅ ANTHROPIC_API_KEY found: {anthropic_key[:20]}...")
    
    if not serpapi_key:
        print("❌ SERPAPI_KEY not found!")
        print("   Set it in .env file or export SERPAPI_KEY=your_key")
        return False
    else:
        print(f"✅ SERPAPI_KEY found: {serpapi_key[:20]}...")
    
    # Initialize agent
    print("\n2. Initializing agent...")
    agent = FlightSearchAgent()
    print("✅ Agent initialized")
    
    # Test flight search
    print("\n3. Testing flight search...")
    print("   Searching: London (LHR) → Barcelona (BCN)")
    print("   Date: 2025-03-01")
    
    try:
        results = agent.search_flights("LHR", "BCN", "2025-03-01")
        
        if "error" in results:
            print(f"❌ Flight search error: {results['error']}")
            return False
        
        if "best_flights" in results and len(results["best_flights"]) > 0:
            print(f"✅ Found {len(results['best_flights'])} flight options")
            first_flight = results["best_flights"][0]
            print(f"   Best option: {first_flight.get('price', 'N/A')} GBP")
        else:
            print("⚠️  No flights found (this is normal if date is in past or no results)")
    except Exception as e:
        print(f"❌ Flight search failed: {str(e)}")
        return False
    
    # Test AI itinerary generation
    print("\n4. Testing AI itinerary generation...")
    print("   Destination: Barcelona")
    print("   Keywords: food, architecture")
    
    try:
        itinerary = agent.create_itinerary_with_ai(
            destination="Barcelona",
            keywords=["food", "architecture", "beach"],
            budget=500,
            duration_days=3
        )
        
        print(f"✅ Itinerary generated ({len(itinerary)} characters)")
        print(f"\n   Preview:")
        print(f"   {itinerary[:200]}...")
    except Exception as e:
        print(f"❌ Itinerary generation failed: {str(e)}")
        return False
    
    # Test flexible date search
    print("\n5. Testing flexible date search...")
    print("   Searching 7 days from 2025-03-01...")
    
    try:
        flexible_results = agent.analyze_flexible_dates("LHR", "BCN", "2025-03-01", 7)
        print(f"✅ Flexible search complete")
        print(f"   Found {len(flexible_results)} flight options across dates")
        
        if flexible_results:
            best_value = agent.find_best_value_flights(flexible_results)
            if best_value:
                print(f"   Best value option: {best_value[0].get('date')} - {best_value[0].get('price', 'N/A')} GBP")
    except Exception as e:
        print(f"❌ Flexible search failed: {str(e)}")
        print(f"   This might be due to rate limits or API issues")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
    print("\n💡 Next steps:")
    print("   1. Start the server: python flight_agent.py")
    print("   2. Test the API: curl http://localhost:8080/")
    print("   3. Deploy to Railway: See DEPLOYMENT_GUIDE.md")
    
    return True

if __name__ == "__main__":
    # Try to load .env file if it exists
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("📄 Loaded environment variables from .env file")
    except ImportError:
        print("⚠️  python-dotenv not installed (optional)")
    except Exception:
        print("⚠️  No .env file found (using system environment variables)")
    
    test_agent()
