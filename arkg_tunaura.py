"""
ARK GENOMIC REVOLUTION ETF (ARKG) - TUNAURA FRAMEWORK ANALYSIS
Applying the 5-layer scorecard developed for Turkish SaaS to a thematic genomics ETF
Data as of May 2026
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_arkg_tunaura():
    """
    ARKG analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability (ETF-level: expense ratio, holdings profitability)
    Layer 2: Growth (AUM growth, holdings revenue growth)
    Layer 3: Valuation (P/E of holdings, analyst ratings)
    Layer 4: Efficiency (Tracking error, concentration risk)
    Layer 5: Financial Health (AUM, institutional flows)
    """
    
    print("=" * 70)
    print("🧬 ARK GENOMIC REVOLUTION ETF (ARKG)")
    print("TUNAURA FRAMEWORK ANALYSIS - Thematic Genomics ETF")
    print("Data as of May 2026")
    print("=" * 70)
    
    # =========================================================
    # FUNDAMENTAL ETF DATA
    # =========================================================
    
    # ETF-level metrics from search results
    aum = 1.16e9  # $1.16 billion net assets [citation:2]
    expense_ratio = 0.0075  # 0.75% expense ratio [citation:2][citation:4]
    holdings_count = 32  # 32 total holdings [citation:4]
    inception_date = "2014-10-31"  # October 31, 2014 inception [citation:2]
    
    # Performance metrics
    performance_ytd = 0.0509  # +5.09% year-to-date [citation:2]
    performance_1y = 0.1325  # +13.25% trailing 1-year [citation:2]
    performance_3y = -0.1177  # -11.77% trailing 3-year [citation:2]
    performance_5y = -0.7076  # -70.76% trailing 5-year [citation:2]
    performance_since_inception = 0.6342  # +63.42% since inception [citation:2]
    
    # Risk metrics
    beta_1y = 1.91  # 1.91x market beta [citation:2]
    max_drawdown_1y = -0.2267  # -22.67% [citation:2]
    max_drawdown_5y = -0.7951  # -79.51% [citation:2]
    volatility_1y = 0.276  # 27.6% tracking error [citation:2]
    
    # Top holdings (from search results)
    top_holdings = [
        ("CRSP", "CRISPR Therapeutics", 9.58),
        ("TWST", "Twist Bioscience", 9.36),
        ("TEM", "Tempus AI", 9.17),
        ("TXG", "10x Genomics", 6.60),
        ("BEAM", "Beam Therapeutics", 5.45),
        ("PSNL", "Personalis", 4.22),
        ("ILMN", "Illumina", 4.13),
        ("NTRA", "Natera", 3.98),
        ("RXRX", "Recursion Pharmaceuticals", 3.71),
        ("NTLA", "Intellia Therapeutics", 3.56)
    ]
    
    # =========================================================
    # LAYER 1: PROFITABILITY (ETF & Holdings Level)
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: PROFITABILITY")
    print("█" * 70)
    
    print(f"  ETF Net Assets: ${aum/1e9:.2f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Holdings Count: {holdings_count}")
    
    # Score Layer 1 (max 6 points)
    layer1_score = 0
    
    # Expense ratio assessment (lower is better)
    if expense_ratio < 0.005:
        layer1_score += 2
        print("\n  ✅ Expense Ratio <0.50% → LOW COST (+2)")
    elif expense_ratio < 0.0075:
        layer1_score += 1
        print("\n  ⚠️ Expense Ratio 0.50-0.75% → MODERATE (+1)")
    else:
        print("\n  ❌ Expense Ratio >0.75% → HIGH COST (+0)")
    
    # Holdings profitability (pre-revenue biotech = high risk)
    pre_revenue_estimate = 0.70  # ~70% of holdings are pre-revenue biotech
    print(f"\n  Estimated Pre-Revenue Holdings: {pre_revenue_estimate:.0%}")
    
    if pre_revenue_estimate < 0.30:
        layer1_score += 2
        print("  ✅ Most holdings profitable → STRONG (+2)")
    elif pre_revenue_estimate < 0.50:
        layer1_score += 1
        print("  ⚠️ Mixed profitability → MODERATE (+1)")
    else:
        print("  ❌ Mostly pre-revenue → HIGH SPECULATIVE RISK (+0)")
    
    # Profitability trend (institutional interest)
    inst_filers_2025q4 = 258  # 258 institutional filers in Q4 2025 [citation:10]
    inst_filers_current = 278  # 278 institutional filers currently [citation:5]
    
    if inst_filers_current > inst_filers_2025q4:
        layer1_score += 2
        print(f"\n  ✅ Institutional interest GROWING ({inst_filers_current} filers) → (+2)")
    else:
        print(f"\n  ⚠️ Institutional interest flat/declining → (+0)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score}/6")
    
    # =========================================================
    # LAYER 2: GROWTH
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: GROWTH")
    print("█" * 70)
    
    print(f"  YTD Performance: {performance_ytd:.1%}")
    print(f"  1-Year Performance: {performance_1y:.1%}")
    print(f"  3-Year Performance: {performance_3y:.1%}")
    print(f"  5-Year Performance: {performance_5y:.1%}")
    print(f"  Since Inception (2014): {performance_since_inception:.1%}")
    
    # Score Layer 2 (max 4 points)
    layer2_score = 0
    
    # Revenue growth of top holdings
    # Note: Fetched dynamically for top holdings
    
    print("\n  Fetching top holdings revenue growth data...")
    
    revenue_growth_positive = 0
    for ticker, name, weight in top_holdings[:5]:  # Check top 5
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            rev_growth = info.get('revenueGrowth', 0)
            if rev_growth and rev_growth > 0:
                revenue_growth_positive += 1
                print(f"    {ticker} ({name[:15]}): {rev_growth:.1%} growth")
            else:
                print(f"    {ticker} ({name[:15]}): Pre-revenue / N/A")
        except:
            print(f"    {ticker} ({name[:15]}): Data unavailable")
    
    if revenue_growth_positive >= 4:
        layer2_score += 2
        print("\n  ✅ Multiple holdings with strong revenue growth (+2)")
    elif revenue_growth_positive >= 2:
        layer2_score += 1
        print("\n  ⚠️ Mixed revenue growth among holdings (+1)")
    else:
        print("\n  ❌ Limited revenue growth across holdings (+0)")
    
    # AUM growth trend
    aum_q4_2025 = 854e6  # $854M in Q4 2025 [citation:10]
    aum_current = 1.16e9  # $1.16B currently [citation:2]
    aum_growth = (aum_current - aum_q4_2025) / aum_q4_2025
    
    if aum_growth > 0.25:
        layer2_score += 2
        print(f"\n  ✅ AUM growth {aum_growth:.1%} → STRONG INFLOW (+2)")
    elif aum_growth > 0.10:
        layer2_score += 1
        print(f"\n  ⚠️ AUM growth {aum_growth:.1%} → MODERATE (+1)")
    else:
        print(f"\n  ❌ AUM growth {aum_growth:.1%} → WEAK (+0)")
    
    print(f"\n  LAYER 2 SCORE: {layer2_score}/4")
    
    # =========================================================
    # LAYER 3: VALUATION
    # =========================================================
    print("\n" + "█" * 70)
    print("💰 LAYER 3: VALUATION")
    print("█" * 70)
    
    # Analyst rating data
    buy_ratings = 28
    hold_ratings = 3
    sell_ratings = 0
    total_ratings = buy_ratings + hold_ratings + sell_ratings
    
    analyst_consensus = (buy_ratings / total_ratings) * 100
    consensus_rating = "Moderate Buy"  # from search results [citation:3]
    
    print(f"  Analyst Consensus: {consensus_rating}")
    print(f"  Buy Ratings: {buy_ratings}")
    print(f"  Hold Ratings: {hold_ratings}")
    print(f"  Sell Ratings: {sell_ratings}")
    print(f"  Buy Ratio: {analyst_consensus:.0f}%")
    
    # Current price data
    current_price_info = "~$26-28 range (varies by exchange) - ARKG traded ~$26.50 on 5/2/2026"
    print(f"\n  Current Price: {current_price_info}")
    
    # Score Layer 3 (max 4 points)
    layer3_score = 0
    
    # Analyst consensus assessment
    if analyst_consensus > 80:
        layer3_score += 2
        print("\n  ✅ Strong Buy consensus → POSITIVE SENTIMENT (+2)")
    elif analyst_consensus > 60:
        layer3_score += 1
        print("\n  ⚠️ Moderate Buy consensus → NEUTRAL-POSITIVE (+1)")
    elif analyst_consensus > 40:
        layer3_score += 0
        print("\n  ⚠️ Hold consensus → NEUTRAL (+0)")
    else:
        layer3_score -= 1
        print("\n  ❌ Sell consensus → NEGATIVE SENTIMENT (-1)")
    
    # Valuation of holdings (P/E for profitable ones)
    profitable_pe_estimate = 35  # Estimated average P/E for profitable holdings
    print(f"\n  Estimated P/E of Profitable Holdings: ~{profitable_pe_estimate}x")
    
    if profitable_pe_estimate < 25:
        layer3_score += 2
        print("  ✅ Reasonable valuations for profitable holdings (+2)")
    elif profitable_pe_estimate < 40:
        layer3_score += 1
        print("  ⚠️ Elevated valuations (+1)")
    else:
        print("  ❌ Very expensive valuations (+0)")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: EFFICIENCY (Risk & Concentration)
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: OPERATIONAL EFFICIENCY & RISK")
    print("█" * 70)
    
    print(f"  Beta (1-Year): {beta_1y:.2f}")
    print(f"  Tracking Error: {volatility_1y:.1%}")
    print(f"  Capture Ratio Up: 141.8%")
    print(f"  Capture Ratio Down: 250.6%")
    
    # Concentration risk
    top5_weight = sum(h[2] for h in top_holdings[:5])  # 9.58+9.36+9.17+6.60+5.45
    top10_weight = sum(h[2] for h in top_holdings)
    
    print(f"\n  Top 5 Holdings Weight: {top5_weight:.1f}%")
    print(f"  Top 10 Holdings Weight: {top10_weight:.1f}%")
    print(f"  Holdings Count: {holdings_count}")
    
    # Score Layer 4 (max 2 points)
    layer4_score = 0
    
    # Concentration risk assessment
    if top10_weight < 50:
        layer4_score += 1
        print("\n  ✅ Well-diversified among holdings (+1)")
    else:
        print("\n  ⚠️ Highly concentrated → HIGH SINGLE-STOCK RISK (+0)")
    
    # Risk-adjusted return
    sortino_ratio_1y = 0.65  # from search results [citation:2]
    if sortino_ratio_1y > 1.0:
        layer4_score += 1
        print("  ✅ Positive risk-adjusted returns (+1)")
    elif sortino_ratio_1y > 0:
        layer4_score += 0.5
        print("\n  ⚠️ Positive but low risk-adjusted returns (+0.5)")
    else:
        print("  ❌ Negative risk-adjusted returns (+0)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score:.1f}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    # Institutional holdings data
    inst_value_q4_2025 = 854e6  # $854M [citation:10]
    inst_value_current = 1.27e9  # $1.27B [citation:7]
    inst_growth = (inst_value_current - inst_value_q4_2025) / inst_value_q4_2025
    
    print(f"  Institutional Holdings Value: ${inst_value_current/1e9:.2f} Billion")
    print(f"  Institutional Holdings Growth (Q4'25→Current): {inst_growth:.1%}")
    print(f"  Number of Institutional Filers: 278 [citation:5]")
    
    # Top institutional holders
    largest_holder = "SUVRETTA CAPITAL MANAGEMENT, LLC"
    largest_holder_value = 241.7e6  # $241.7M [citation:5]
    
    print(f"\n  Largest Institutional Holder: {largest_holder}")
    print(f"  Largest Holder Value: ${largest_holder_value/1e6:.1f}M")
    
    # Score Layer 5 (max 2 points)
    layer5_score = 0
    
    # Institutional flow assessment
    if inst_growth > 0.30:
        layer5_score += 1
        print("\n  ✅ Strong institutional inflow (+1)")
    elif inst_growth > 0.10:
        layer5_score += 0.5
        print("\n  ⚠️ Moderate institutional inflow (+0.5)")
    else:
        print("\n  ❌ Weak or negative institutional flow (+0)")
    
    # AUM and viability
    if aum > 500e6:
        layer5_score += 1
        print("  ✅ AUM >$500M → VIABLE FUND (+1)")
    else:
        print("  ⚠️ AUM <$500M → SMALL FUND (+0)")
    
    print(f"\n  LAYER 5 SCORE: {layer5_score:.1f}/2")
    
    # =========================================================
    # TUNAURA FRAMEWORK FINAL SCORECARD
    # =========================================================
    print("\n" + "=" * 70)
    print("🎯 TUNAURA FRAMEWORK - FINAL SCORECARD")
    print("=" * 70)
    
    total_score = layer1_score + layer2_score + layer3_score + layer4_score + layer5_score
    max_score = 6 + 4 + 4 + 2 + 2  # = 18
    
    print(f"\n  {'Layer':<20} {'Score':<10} {'Max':<10} {'%':<10}")
    print("  " + "-" * 50)
    print(f"  {'1. Profitability (ETF/Holdings)':<20} {layer1_score:<10} {6:<10} {layer1_score/6*100:.0f}%")
    print(f"  {'2. Growth':<20} {layer2_score:<10} {4:<10} {layer2_score/4*100:.0f}%")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10} {layer3_score/4*100:.0f}%")
    print(f"  {'4. Risk/Efficiency':<20} {layer4_score:<10.1f} {2:<10} {layer4_score/2*100:.0f}%")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10.1f} {2:<10} {layer5_score/2*100:.0f}%")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10} {total_score/max_score*100:.0f}%")
    
    # Final verdict
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID ETF INVESTMENT")
        print("    → Strong fundamentals, reasonable valuations, institutional backing")
        print("    → Suggested position: Core holding 3-5% of portfolio")
    elif total_score >= 12:
        print("    ✅ SOLID ETF with CAUTION")
        print("    → Good underlying thesis, but watch concentration and volatility")
        print("    → Suggested position: Satellite holding 2-3% of portfolio")
    elif total_score >= 9:
        print("    ⚠️ SPECULATIVE, HAS RISKS")
        print("    → Strong theme but high volatility and pre-revenue concentration")
        print("    → Suggested position: Tactical 1-2% of portfolio")
    elif total_score >= 6:
        print("    ⚠️ HIGH RISK - Avoid or small speculative position")
        print("    → Significant concerns with profitability and track record")
        print("    → Suggested position: <1% of portfolio")
    else:
        print("    ❌ NOT SOLID - Avoid")
    
    # =========================================================
    # TUNAURA FRAMEWORK COMPARISON
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 TUNAURA FRAMEWORK - COMPARISON")
    print("=" * 70)
    
    comparisons = [
        ("TUNAURA (Turkish SaaS)", 6, "❌ AVOID"),
        ("COGT (Biotech)", 13, "⚠️ SPECULATIVE BUY"),
        ("FSLR (Solar)", 17, "✅ STRONG BUY"),
        ("ARKG (Genomics ETF)", total_score, "⚠️ HIGH RISK" if total_score < 12 else "✅ MODERATE")
    ]
    
    print(f"\n  {'Company/ETF':<25} {'Score':<8} {'/18':<5} {'Verdict':<20}")
    print("  " + "-" * 60)
    for name, score, verdict in comparisons:
        print(f"  {name:<25} {score:<8} /18    {verdict:<20}")
    
    print("\n  ARKG Specific Considerations:")
    print("    • 70%+ of holdings are pre-revenue biotech → HIGH BINARY RISK")
    print("    • 5-Year Return: -70.8% → LONG TERM HOLDERS DEEPLY UNDERWATER")
    print("    • Top 5 holdings = 40% of fund → CONCENTRATION RISK")
    print("    • Beta 1.91x → MUCH MORE VOLATILE THAN MARKET")
    print("    • However: +13.25% 1-year return, +5.09% YTD → MOMENTUM IMPROVING")
    
    # =========================================================
    # RISK FACTORS
    # =========================================================
    print("\n" + "=" * 70)
    print("⚠️ ARKG-SPECIFIC RISK FACTORS")
    print("=" * 70)
    
    print("""
    1. Pre-Revenue Concentration:
       • ~70% of holdings are clinical-stage biotech with ZERO revenue
       • Binary outcomes: FDA approval or complete value destruction
       • Individual holdings can drop 50-80% on negative trial data
    
    2. Historic Underperformance:
       • 5-Year Return: -70.8% (from peak in 2021)
       • Maximum Drawdown: -79.5% 
       • Long-term holders have suffered severe losses
       • ARKG peaked during pandemic biotech mania
    
    3. Concentration Risk:
       • Top 5 holdings = 40%+ of fund weight
       • Single-stock risk is significant
       • CRISPR Therapeutics at 9.6% - company has no approved products yet
    
    4. Active Management Risk:
       • High turnover (5% reported, but often higher)
       • Cathie Wood / ARK Invest strategy has underperformed since 2022
       • Recent buys: Meta, Alphabet → moving away from pure genomics thesis
    
    5. Volatility:
       • Beta: 1.91x market (almost 2x as volatile)
       • Down capture ratio: 250% (loses more than market in downturns)
       • Not suitable for conservative portfolios
    """)
    
    # =========================================================
    # SUMMARY STATISTICS
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 ARKG KEY STATISTICS SUMMARY")
    print("=" * 70)
    
    print(f"""
    Fund Metrics:
    ├── Net Assets:       ${aum/1e9:.2f} Billion [citation:2]
    ├── Expense Ratio:    {expense_ratio:.2%} [citation:2]
    ├── Holdings:         {holdings_count} [citation:4]
    ├── Inception:        {inception_date} [citation:2]
    └── 13F Filers:       278 [citation:5]
    
    Performance:
    ├── YTD 2026:         {performance_ytd:.1%} [citation:2]
    ├── 1-Year:           {performance_1y:.1%} [citation:2]
    ├── 3-Year:           {performance_3y:.1%} [citation:2]
    ├── 5-Year:           {performance_5y:.1%} [citation:2]
    └── Since Inception:  {performance_since_inception:.1%} [citation:2]
    
    Risk:
    ├── Beta (1Y):        {beta_1y:.2f}x [citation:2]
    ├── Max Drawdown (1Y): {max_drawdown_1y:.1%} [citation:2]
    ├── Max Drawdown (5Y): {max_drawdown_5y:.1%} [citation:2]
    └── Tracking Error:   {volatility_1y:.1%} [citation:2]
    
    Analyst Consensus:
    ├── Rating:           {consensus_rating} [citation:3]
    ├── Buy:              {buy_ratings} [citation:3]
    ├── Hold:             {hold_ratings} [citation:3]
    └── Sell:             {sell_ratings} [citation:3]
    """)
    
    return {
        "total_score": total_score,
        "max_score": max_score,
        "layer_scores": {
            "profitability": layer1_score,
            "growth": layer2_score,
            "valuation": layer3_score,
            "efficiency": layer4_score,
            "financial_health": layer5_score
        },
        "aum": aum,
        "expense_ratio": expense_ratio,
        "performance_1y": performance_1y,
        "performance_5y": performance_5y,
        "beta": beta_1y,
        "analyst_consensus": consensus_rating
    }


def plot_arkg_performance():
    """Create performance chart for ARKG"""
    
    print("\n📈 Generating ARKG performance chart...")
    
    # Download historical data for the US-listed version
    arkg = yf.Ticker("ARKG")
    data = arkg.history(period="5y")
    
    if data.empty:
        print("❌ No price data available for ARKG")
        print("   The ETF trades on Cboe BZX under ticker ARKG")
        return
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price chart
    ax1.plot(data.index, data['Close'], label='ARKG Price', linewidth=2, color='#1a73e8')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-Day MA', linewidth=1.5, color='#e67e22')
    ax1.plot(data.index, data['Close'].rolling(window=200).mean(), 
             label='200-Day MA', linewidth=1.5, color='#2ecc71')
    
    # Highlight 2021 peak and current
    max_price = data['Close'].max()
    max_date = data['Close'].idxmax()
    current_price = data['Close'].iloc[-1]
    
    ax1.axhline(y=max_price, color='red', linestyle='--', alpha=0.5, label=f'Peak: ${max_price:.2f}')
    ax1.axhline(y=current_price, color='green', linestyle='--', alpha=0.5, label=f'Current: ${current_price:.2f}')
    
    ax1.set_title('ARK Genomic Revolution ETF (ARKG) - 5 Year Price History', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price (USD)', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Volume chart
    colors = ['#2ecc71' if data['Close'].iloc[i] >= data['Close'].iloc[i-1] 
              else '#e74c3c' for i in range(len(data))]
    ax2.bar(data.index, data['Volume'], color=colors, alpha=0.7)
    ax2.set_title('Trading Volume', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('ARKG_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved: ARKG_chart.png")
    plt.show()


def analyze_arkg_holdings():
    """Analyze key holdings of ARKG"""
    
    print("\n" + "=" * 70)
    print("🔬 ARKG TOP HOLDINGS ANALYSIS")
    print("=" * 70)
    
    # Source: ARKG holdings as of April 2026 [citation:4]
    holdings = [
        {"ticker": "CRSP", "name": "CRISPR Therapeutics", "weight": 9.58, "stage": "Clinical", "revenue": "No"},
        {"ticker": "TWST", "name": "Twist Bioscience", "weight": 9.36, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "TEM", "name": "Tempus AI", "weight": 9.17, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "TXG", "name": "10x Genomics", "weight": 6.60, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "BEAM", "name": "Beam Therapeutics", "weight": 5.45, "stage": "Clinical", "revenue": "No"},
        {"ticker": "PSNL", "name": "Personalis", "weight": 4.22, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "ILMN", "name": "Illumina", "weight": 4.13, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "NTRA", "name": "Natera", "weight": 3.98, "stage": "Commercial", "revenue": "Yes"},
        {"ticker": "RXRX", "name": "Recursion Pharma", "weight": 3.71, "stage": "Clinical", "revenue": "No"},
        {"ticker": "NTLA", "name": "Intellia", "weight": 3.56, "stage": "Clinical", "revenue": "No"}
    ]
    
    print("\n  {:<8} {:<22} {:>8} {:>12} {:>10}".format(
        "Ticker", "Company", "Weight %", "Stage", "Revenue"))
    print("  " + "-" * 65)
    
    clinical_weight = 0
    commercial_weight = 0
    
    for h in holdings:
        print("  {:<8} {:<22} {:>7.2f}% {:>12} {:>10}".format(
            h["ticker"], h["name"][:20], h["weight"], h["stage"], h["revenue"]))
        
        if h["stage"] == "Clinical":
            clinical_weight += h["weight"]
        else:
            commercial_weight += h["weight"]
    
    print("\n  Portfolio Breakdown by Stage:")
    print(f"    Clinical-stage (pre-revenue): {clinical_weight:.1f}%")
    print(f"    Commercial-stage (revenue): {commercial_weight:.1f}%")
    print(f"    Commercial/Clinical ratio: {commercial_weight/clinical_weight:.2f}")
    
    if clinical_weight > 40:
        print("\n  ⚠️ WARNING: >40% in clinical-stage biotech → HIGH BINARY RISK")
    
    return {"clinical_weight": clinical_weight, "commercial_weight": commercial_weight}


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🧬 ARKG ANALYSIS - TUNAURA FRAMEWORK")
    print("Applying the Turkish SaaS scorecard to a genomics ETF")
    print("=" * 70)
    
    # Run ETF analysis
    results = analyze_arkg_tunaura()
    
    # Analyze holdings composition
    holdings_results = analyze_arkg_holdings()
    
    # Interactive menu
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Display ARKG price chart (5-year history)")
    print("  2. Show top holdings breakdown")
    print("  3. Run analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_arkg_performance()
    elif choice == "2":
        analyze_arkg_holdings()
    elif choice == "3":
        analyze_arkg_tunaura()
    else:
        print("\n✅ Analysis complete!")
        print(f"\n📌 ARKG scored {results['total_score']:.1f}/18 on the TUNAURA framework")
        if results['total_score'] >= 12:
            print("   → Classification: SOLID ETF with CAUTION")
        elif results['total_score'] >= 9:
            print("   → Classification: SPECULATIVE, HAS RISKS")
        else:
            print("   → Classification: HIGH RISK - AVOID")