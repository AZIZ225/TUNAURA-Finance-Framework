"""
RBOT FULL ANALYSIS - NO INTERACTIVE MENU
Complete analysis then exits automatically
"""

import yfinance as yf
import matplotlib.pyplot as plt

def get_rbot_data():
    """Fetch real-time data for RBOT"""
    try:
        rbot = yf.Ticker("RBOT")
        info = rbot.info
        
        # Current price
        price = info.get('currentPrice', info.get('regularMarketPrice', 'N/A'))
        
        # 52-week range
        week_high = info.get('fiftyTwoWeekHigh', 'N/A')
        week_low = info.get('fiftyTwoWeekLow', 'N/A')
        
        # Market cap
        market_cap = info.get('marketCap', 'N/A')
        
        return price, week_high, week_low, market_cap
    except:
        return "N/A", "N/A", "N/A", "N/A"

def analyze_rbot():
    print("=" * 70)
    print("🤖 ISHARES AUTOMATION & ROBOTICS ETF (RBOT)")
    print("TUNAURA FRAMEWORK ANALYSIS - FULL VERSION")
    print("=" * 70)
    
    # Get real-time data
    price, week_high, week_low, market_cap = get_rbot_data()
    
    # Fixed metrics
    expense_ratio = 0.40
    holdings = 135
    one_year_return = 38.39
    three_year_return = 63.62
    since_inception = 240.11
    top10_weight = 42.6
    
    print("\n📊 FUND METRICS")
    print("-" * 50)
    print(f"  Expense Ratio: {expense_ratio}%")
    print(f"  Holdings: {holdings}")
    print(f"  Top 10 Weight: {top10_weight}%")
    print(f"  Current Price: ${price}" if price != "N/A" else "  Current Price: N/A")
    
    print("\n📈 PERFORMANCE")
    print("-" * 50)
    print(f"  1-Year Return: +{one_year_return}%")
    print(f"  3-Year Cumulative: +{three_year_return}%")
    print(f"  Since Inception (2016): +{since_inception}%")
    
    print("\n📊 LAYER SCORES")
    print("-" * 50)
    print("  Layer 1 (Fee Efficiency): 2.5/6")
    print("  Layer 2 (Performance): 2.5/4")
    print("  Layer 3 (Valuation): 2.5/4")
    print("  Layer 4 (Diversification): 2/2")
    print("  Layer 5 (Financial Health): 1.5/2")
    print("  " + "-" * 50)
    print("  TOTAL: 11/18")
    
    print("\n🎯 FINAL VERDICT")
    print("-" * 50)
    print("  ✅ SOLID ETF - THEMATIC AUTOMATION & ROBOTICS")
    print("  → Reasonable fees for thematic exposure")
    print("  → Strong long-term track record")
    print("  → Good diversification with 135 holdings")
    print("  → BlackRock iShares provider stability")
    
    print("\n⚠️ KEY RISKS")
    print("-" * 50)
    print("  • Semiconductor-heavy portfolio")
    print("  • YTD underperformance vs tech sector")
    print("  • No dividend (accumulating structure)")
    print("  • Higher volatility than broad market")
    
    print("\n" + "=" * 70)
    print("📌 Bottom Line: SOLID ETF for automation & robotics exposure")
    print("=" * 70)

# Run the analysis
analyze_rbot()
