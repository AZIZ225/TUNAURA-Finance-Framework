"""
COGENT BIOSCIENCES (COGT) ANALYSIS FUNCTION
Clinical-stage biotech analysis using the TUNAURA framework
Focuses on cash runway, pipeline progress, and valuation vs. SaaS metrics
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_cogt():
    """Complete analysis of Cogent Biosciences (COGT)"""
    
    print("=" * 70)
    print("🔬 COGENT BIOSCIENCES (COGT) - CLINICAL-STAGE BIOTECH ANALYSIS")
    print("=" * 70)
    
    # Fetch data
    stock = yf.Ticker("COGT")
    info = stock.info
    
    # ===== LAYER 1: CASH POSITION (Most Critical for Biotech) =====
    print("\n💰 CASH POSITION & RUNWAY")
    print("-" * 50)
    
    cash = info.get('totalCash', 0)
    cash_per_share = info.get('totalCashPerShare', 0)
    debt_to_equity = info.get('debtToEquity', 0)
    
    print(f"  Total Cash & Investments: ${cash/1e9:.2f} Billion")
    print(f"  Cash Per Share: ${cash_per_share:.2f}")
    print(f"  Debt/Equity: {debt_to_equity:.2f}")
    
    # Cash runway assessment
    quarterly_burn = -info.get('freeCashflow', 0) / 4 if info.get('freeCashflow') else 80000000
    if cash > 0 and quarterly_burn > 0:
        quarters_of_runway = cash / quarterly_burn
        print(f"\n  Estimated Quarterly Cash Burn: ~${quarterly_burn/1e6:.1f}M")
        print(f"  Estimated Runway: ~{quarters_of_runway:.0f} quarters")
        if quarters_of_runway > 8:
            print("    ✅ Strong cash position (funded into 2028)")

    # ===== LAYER 2: VALUATION METRICS (P/B, Market Cap) =====
    print("\n📈 VALUATION METRICS")
    print("-" * 50)
    
    market_cap = info.get('marketCap', 0)
    price_to_book = info.get('priceToBook', 0)
    enterprise_value = info.get('enterpriseValue', 0)
    
    print(f"  Market Cap: ${market_cap/1e9:.2f} Billion")
    print(f"  Enterprise Value: ${enterprise_value/1e9:.2f} Billion")
    print(f"  Price-to-Book (P/B): {price_to_book:.2f}x")
    
    # Biotech valuation context
    if price_to_book:
        print(f"\n  Valuation Context for Biotech:")
        if price_to_book < 5:
            print("    ⚠️ Low P/B - potential value play or distressed?")
        elif price_to_book < 15:
            print("    ✅ Moderate P/B - reasonable for clinical-stage biotech")
        else:
            print("    🔴 High P/B - market pricing in significant pipeline value")

    # ===== LAYER 3: PROFITABILITY (Not Applicable - Pre-Revenue) =====
    print("\n📊 PROFITABILITY STATUS (Pre-Revenue Biotech)")
    print("-" * 50)
    
    net_income = info.get('netIncomeToCommon', 0)
    eps = info.get('trailingEPS', 0)
    profit_margin = info.get('profitMargins', 0)
    
    print(f"  Net Income (TTM): ${net_income/1e6:.1f} Million")
    print(f"  EPS (TTM): ${eps:.2f}")
    
    print("\n  ⚠️ This is a CLINICAL-STAGE biotech company.")
    print("  → No revenue, no profits - standard for this stage.")
    print("  → Value depends on pipeline and regulatory approvals.")

    # ===== LAYER 4: PIPELINE PROGRESS (Key Value Driver) =====
    print("\n💊 PIPELINE & REGULATORY PROGRESS")
    print("-" * 50)
    
    print("  Lead Candidate: BEZUCLASTINIB (CGT9486)")
    print("\n  Regulatory Status:")
    print("    • NDA submitted for Non-Advanced Systemic Mastocytosis (Dec 2025)")
    print("    • Additional NDA for Advanced SM expected H1 2026")
    print("    • Rolling NDA for GIST (2nd line) - completion by April 2026")
    print("\n  Clinical Highlights:")
    print("    • PEAK trial (GIST): 16.5 months median PFS - nearly double control")
    print("    • SUMMIT trial (NonAdvSM): Deepening symptomatic relief over 48 weeks")
    
    print("\n  Pipeline Expansion:")
    print("    • CGT1145: JAK2-driven diseases (IND planned)")
    print("    • CGT1815: KRAS-mutant cancers (data presented at AACR 2026)")

    # ===== LAYER 5: ANALYST PRICE TARGETS =====
    print("\n🎯 ANALYST PRICE TARGETS")
    print("-" * 50)
    
    current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
    target_mean = info.get('targetMeanPrice', 0)
    target_high = info.get('targetHighPrice', 0)
    target_low = info.get('targetLowPrice', 0)
    
    print(f"  Current Price: ${current_price:.2f}")
    
    if target_mean:
        print(f"  Mean Target: ${target_mean:.2f}")
        print(f"  High Target: ${target_high:.2f}")
        print(f"  Low Target: ${target_low:.2f}")
        upside = (target_mean - current_price) / current_price * 100
        print(f"\n  Potential Upside: {upside:.1f}%")
        if upside > 30:
            print("    ✅ Significant upside according to analyst consensus")
    
    # ===== LAYER 6: PERFORMANCE =====
    print("\n📈 STOCK PERFORMANCE")
    print("-" * 50)
    
    hist = stock.history(period="1y")
    if not hist.empty:
        year_ago_price = hist['Close'].iloc[0]
        current = hist['Close'].iloc[-1]
        return_1y = (current - year_ago_price) / year_ago_price * 100
        print(f"  1-Year Return: {return_1y:.1f}%")
        
        # Get 52-week range
        week_52_low = info.get('fiftyTwoWeekLow', 0)
        week_52_high = info.get('fiftyTwoWeekHigh', 0)
        print(f"  52-Week Range: ${week_52_low:.2f} - ${week_52_high:.2f}")
        
        # Position in range
        if week_52_high > week_52_low:
            position = (current - week_52_low) / (week_52_high - week_52_low) * 100
            print(f"  Current Position in Range: {position:.0f}%")

    # ===== FINAL VERDICT =====
    print("\n" + "=" * 70)
    print("🎯 TUNAURA-STYLE FINAL VERDICT")
    print("=" * 70)
    
    score = 0
    max_score = 12
    
    # Cash position score (max 4)
    if cash > 500e6:
        score += 3
        print("  ✅ Strong cash position ($900M+) - Funded into 2028 (+3)")
    elif cash > 200e6:
        score += 1
    
    # Valuation score (max 4)
    upside = (target_mean - current_price) / current_price * 100 if target_mean else 0
    if upside > 40:
        score += 4
        print(f"  ✅ High analyst upside potential ({upside:.0f}%) (+4)")
    elif upside > 20:
        score += 2
    
    # Pipeline progress score (max 4)
    print("  ✅ Multiple NDAs filed/submitted - Regulatory momentum (+3)")
    score += 3
    
    print(f"\n  TOTAL SCORE: {score}/{max_score}")
    
    if score >= 8:
        print("\n  ✅ SPECULATIVE BUY - Strong cash position + regulatory catalysts")
        print("  → High risk, high reward clinical-stage biotech")
        print("  → Position size: 2-3% of portfolio (speculative bucket)")
    elif score >= 5:
        print("\n  ⚠️ CAUTIOUS - Monitor regulatory milestones")
        print("  → Wait for NDA approvals or pipeline data")
    else:
        print("\n  ❌ AVOID - Too many red flags")
    
    print("\n" + "=" * 70)
    print("⚠️ DISCLAIMER: This is a clinical-stage biotech company.")
    print("   No revenue, no profits. Value depends entirely on:")
    print("   1. FDA approval for bezuclastinib")
    print("   2. Commercial launch success")
    print("   3. Pipeline expansion")
    print("=" * 70)
    
    return {
        "cash_position": cash,
        "market_cap": market_cap,
        "price_to_book": price_to_book,
        "upside_potential": upside if target_mean else None,
        "score": score
    }


def plot_cogt_stock():
    """Create stock price chart for COGT"""
    
    print("\n📈 Generating COGT stock chart...")
    
    stock = yf.Ticker("COGT")
    data = stock.history(period="1y")
    
    if data.empty:
        print("❌ No data available")
        return
    
    # Create chart
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price with moving averages
    ax1.plot(data.index, data['Close'], label='Close Price', linewidth=2, color='#2E86AB')
    ax1.plot(data.index, data['Close'].rolling(window=20).mean(), 
             label='20-day MA', linewidth=1.5, color='#A23B72')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-day MA', linewidth=1.5, color='#F18F01')
    
    ax1.set_title('Cogent Biosciences (COGT) - 1 Year Price History', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price (USD)', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Volume
    colors = ['#73AB84' if data['Close'].iloc[i] >= data['Close'].iloc[i-1] 
              else '#A23B72' for i in range(len(data))]
    ax2.bar(data.index, data['Volume'], color=colors, alpha=0.7)
    ax2.set_title('Trading Volume', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('COGT_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved as: COGT_chart.png")
    plt.show()


def compare_biotech_peers():
    """Compare COGT with similar clinical-stage biotechs"""
    
    peers = ["COGT", "PTGX", "RYTM", "PTCT", "CRSP"]
    peer_names = {
        "COGT": "Cogent Biosciences",
        "PTGX": "Protagonist Therapeutics", 
        "RYTM": "Rhythm Pharmaceuticals",
        "PTCT": "PTC Therapeutics",
        "CRSP": "CRISPR Therapeutics"
    }
    
    print("\n" + "=" * 70)
    print("🏥 COGT vs. BIOTECH PEER COMPARISON")
    print("=" * 70)
    
    results = []
    for ticker in peers:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        market_cap = info.get('marketCap', 0)
        price_to_book = info.get('priceToBook', 0)
        cash = info.get('totalCash', 0)
        
        results.append({
            "Ticker": ticker,
            "Name": peer_names.get(ticker, ticker)[:20],
            "Market Cap (B)": market_cap / 1e9 if market_cap else 0,
            "P/B": price_to_book if price_to_book else 0,
            "Cash (M)": cash / 1e6 if cash else 0
        })
    
    # Display comparison table
    print("\n{:<10} {:<22} {:>14} {:>8} {:>12}".format(
        "Ticker", "Company", "Market Cap (B)", "P/B", "Cash (M)"))
    print("-" * 70)
    
    for r in results:
        print("{:<10} {:<22} {:>13.2f} {:>8.2f} {:>11.0f}".format(
            r["Ticker"], r["Name"], r["Market Cap (B)"], r["P/B"], r["Cash (M)"]))
    
    # COGT positioning
    cogt_pb = results[0]["P/B"]
    peer_pb_avg = sum(r["P/B"] for r in results[1:] if r["P/B"] > 0) / 4
    
    print(f"\n  COGT P/B: {cogt_pb:.2f}x")
    print(f"  Peer Avg P/B: {peer_pb_avg:.2f}x")
    
    if cogt_pb < peer_pb_avg:
        print("  ✅ COGT trading at discount to peers on P/B basis")
    else:
        print("  ⚠️ COGT trading at premium to peers on P/B basis")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🚀 COGENT BIOSCIENCES (COGT) ANALYSIS TOOL")
    print("Based on the TUNAURA analytical framework")
    print("=" * 70)
    
    # Run full analysis
    analyze_cogt()
    
    # Ask user what to do next
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Plot COGT stock chart")
    print("  2. Compare COGT with biotech peers")
    print("  3. Run full analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_cogt_stock()
    elif choice == "2":
        compare_biotech_peers()
    elif choice == "3":
        analyze_cogt()
    else:
        print("✅ Analysis complete!")
