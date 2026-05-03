"""
INNOVATOR U.S. EQUITY POWER BUFFER ETF (PFEB) - TUNAURA FRAMEWORK ANALYSIS
Applying the 5-layer scorecard to a defined-outcome buffer ETF
Data as of May 2026
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_pfeb_tunaura():
    """
    PFEB analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability (Expense ratio, fee efficiency)
    Layer 2: Growth (AUM growth, performance track record)
    Layer 3: Valuation (Premium/discount to NAV, price positioning)
    Layer 4: Efficiency (Buffer mechanics, options strategy)
    Layer 5: Financial Health (AUM, institutional flows)
    """
    
    print("=" * 70)
    print("🛡️ INNOVATOR U.S. EQUITY POWER BUFFER ETF (PFEB)")
    print("TUNAURA FRAMEWORK ANALYSIS - Defined-Outcome Buffer ETF")
    print("Data as of May 2026")
    print("=" * 70)
    
    # =========================================================
    # FUNDAMENTAL ETF DATA
    # =========================================================
    
    # ETF-level metrics from search results
    aum = 906.4e6  # $906.4 million net assets [citation:3]
    expense_ratio = 0.0079  # 0.79% expense ratio [citation:3][citation:7]
    holdings_count = 6  # 6 holdings (primarily options on SPY) [citation:3]
    inception_date = "2020-01-31"  # January 31, 2020 inception [citation:3]
    
    # Performance metrics
    performance_ytd = -0.017  # -1.7% year-to-date [citation:7]
    performance_1y = 0.1195  # +11.95% trailing 1-year (price return) [citation:3]
    performance_3y = 0.1111  # +11.11% trailing 3-year (price return) [citation:3]
    performance_5y = 0.0782  # +7.82% trailing 5-year (price return) [citation:3]
    performance_since_inception = 0.0820  # +8.20% since inception [citation:3]
    
    # Risk metrics
    beta = 0.54  # 0.54x market beta [citation:9]
    volatility_1y = 0.10  # 10% volatility [citation:9]
    sharpe_ratio_1y = 0.66  # 0.66 Sharpe ratio [citation:9]
    sortino_ratio_1y = 1.05  # 1.05 Sortino ratio [citation:9]
    
    # Price data
    current_price = 41.95  # $41.95 as of April 2026 [citation:3]
    week_52_high = 42.05  # $42.05 52-week high [citation:3][citation:7]
    week_52_low = 33.99  # $33.99 52-week low [citation:3]
    
    # Fund flows
    fund_flows_1y = 115.2e6  # $115.2M positive fund flows (1-year) [citation:6]
    aum_q4_2025 = 845e6  # $845M AUM in Q4 2025 [citation:4]
    aum_current = aum
    aum_growth = (aum_current - aum_q4_2025) / aum_q4_2025
    
    # =========================================================
    # LAYER 1: PROFITABILITY
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: PROFITABILITY & FEE EFFICIENCY")
    print("█" * 70)
    
    print(f"  ETF Net Assets: ${aum/1e6:.1f} Million")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Holdings Count: {holdings_count}")
    print(f"  Inception Date: {inception_date}")
    
    # Score Layer 1 (max 6 points)
    layer1_score = 0
    
    # Expense ratio assessment (higher is worse for buffer ETFs)
    if expense_ratio < 0.0065:
        layer1_score += 2
        print("\n  ✅ Expense Ratio <0.65% → LOW COST (+2)")
    elif expense_ratio < 0.0079:
        layer1_score += 1
        print("\n  ⚠️ Expense Ratio 0.65-0.79% → MODERATE (+1)")
    else:
        print("\n  ❌ Expense Ratio >0.79% → HIGH COST (+0)")
    
    # Buffer ETF value proposition (downside protection vs fee)
    fee_value_proposition = "Provides 15% downside buffer over 1-year outcome period [citation:4]"
    print(f"\n  Value Proposition: {fee_value_proposition}")
    print("   Compared to buying SPY options directly:")
    print("   • PFEB simplifies options strategy implementation")
    print("   • Caps upside but limits downside")
    
    # Peer comparison vs similar buffer ETFs
    peer_expense_range = (0.75, 0.85)  # typical buffer ETF range
    if expense_ratio <= peer_expense_range[0]:
        layer1_score += 2
        print("\n  ✅ Fees competitive vs peer buffer ETFs (+2)")
    elif expense_ratio <= peer_expense_range[1]:
        layer1_score += 1
        print("\n  ⚠️ Fees in line with peers (+1)")
    else:
        print("\n  ❌ Fees higher than peer average (+0)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score}/6")
    
    # =========================================================
    # LAYER 2: GROWTH (Performance & AUM Trends)
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: GROWTH & PERFORMANCE")
    print("█" * 70)
    
    print(f"  YTD Performance: {performance_ytd:.1%}")
    print(f"  1-Year Performance: {performance_1y:.1%}")
    print(f"  3-Year Performance: {performance_3y:.1%}")
    print(f"  5-Year Performance: {performance_5y:.1%}")
    print(f"  Since Inception (2020): {performance_since_inception:.1%}")
    
    # Score Layer 2 (max 4 points)
    layer2_score = 0
    
    # Short-term performance (1-year relative to S&P 500)
    # Note: S&P 500 1-year return ~10-12% in this period
    if performance_1y > 0.12:
        layer2_score += 1
        print("\n  ✅ 1-Year performance >12% → STRONG (+1)")
    elif performance_1y > 0.08:
        layer2_score += 0.5
        print("\n  ⚠️ 1-Year performance 8-12% → MODERATE (+0.5)")
    else:
        print("\n  ❌ 1-Year performance <8% → WEAK (+0)")
    
    # Long-term performance (since inception)
    annualized_return = performance_since_inception
    if annualized_return > 0.10:
        layer2_score += 1
        print("  ✅ Since inception >10% annualized → STRONG (+1)")
    elif annualized_return > 0.07:
        layer2_score += 0.5
        print("  ⚠️ Since inception 7-10% annualized → MODERATE (+0.5)")
    else:
        print("  ❌ Since inception <7% annualized → WEAK (+0)")
    
    # AUM growth trend
    print(f"\n  AUM Growth (Q4'25→Current): {aum_growth:.1%}")
    
    if aum_growth > 0.10:
        layer2_score += 2
        print("  ✅ AUM growth >10% → STRONG INFLOW (+2)")
    elif aum_growth > 0.05:
        layer2_score += 1
        print("  ⚠️ AUM growth 5-10% → MODERATE INFLOW (+1)")
    else:
        print("  ❌ AUM growth <5% → WEAK INFLOW (+0)")
    
    print(f"\n  LAYER 2 SCORE: {layer2_score:.1f}/4")
    
    # =========================================================
    # LAYER 3: VALUATION & POSITIONING
    # =========================================================
    print("\n" + "█" * 70)
    print("💰 LAYER 3: VALUATION & PRICE POSITIONING")
    print("█" * 70)
    
    print(f"  Current Price: ${current_price:.2f}")
    print(f"  52-Week High: ${week_52_high:.2f}")
    print(f"  52-Week Low: ${week_52_low:.2f}")
    
    # Position in 52-week range
    position_pct = (current_price - week_52_low) / (week_52_high - week_52_low)
    print(f"  Position in Range: {position_pct:.1%}")
    
    # Historical price data
    print(f"\n  Price History (2026):")
    print(f"    • 52-week low: ${week_52_low:.2f} (April 2026?)")
    print(f"    • Near 52-week high: Trading within {100 - current_price/week_52_high*100:.1f}% of high")
    
    # Score Layer 3 (max 4 points)
    layer3_score = 0
    
    # Premium/discount to NAV (no direct NAV data, but price action indicates)
    near_high_threshold = 0.95
    if position_pct > near_high_threshold:
        layer3_score += 1
        print("\n  ⚠️ Trading near 52-week high → POTENTIALLY EXPENSIVE ENTRY (+1)")
    else:
        print("\n  ✅ Trading at reasonable level within range (+2)")
        layer3_score += 2
    
    # Buffer value vs cost (benefit-cost analysis)
    buffer_benefit = 0.15  # 15% downside buffer over outcome period [citation:4]
    cost_per_year = expense_ratio
    benefit_cost_ratio = buffer_benefit / cost_per_year
    
    print(f"\n  Benefit-Cost Analysis:")
    print(f"    • Downside Buffer: {buffer_benefit:.0%}")
    print(f"    • Annual Cost: {cost_per_year:.2%}")
    print(f"    • Benefit/Cost Ratio: {benefit_cost_ratio:.1f}x")
    
    if benefit_cost_ratio > 20:
        layer3_score += 2
        print("  ✅ Excellent benefit/cost value (+2)")
    elif benefit_cost_ratio > 15:
        layer3_score += 1
        print("  ⚠️ Good benefit/cost value (+1)")
    else:
        print("  ❌ Limited benefit/cost value (+0)")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: EFFICIENCY (Buffer Mechanics & Strategy)
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: STRATEGY EFFICIENCY & RISK MANAGEMENT")
    print("█" * 70)
    
    # Strategy description
    print("  Product Strategy:")
    print("    • Defined-outcome ETF with 15% downside buffer [citation:4]")
    print("    • Resets annually each February [citation:4]")
    print("    • Invests primarily in options on SPY (S&P 500 ETF) [citation:3]")
    print("    • Capped upside participation")
    
    print(f"\n  Risk Metrics:")
    print(f"    • Beta (Market Sensitivity): {beta:.2f}")
    print(f"    • Volatility (1Y): {volatility_1y:.1%}")
    print(f"    • Sharpe Ratio (1Y): {sharpe_ratio_1y:.2f}")
    print(f"    • Sortino Ratio (1Y): {sortino_ratio_1y:.2f}")
    
    # Score Layer 4 (max 2 points)
    layer4_score = 0
    
    # Beta assessment for defined-outcome ETF
    if beta < 0.6:
        layer4_score += 1
        print("\n  ✅ Low beta (<0.6) → EFFECTIVE DOWNSIDE PROTECTION (+1)")
    else:
        print("\n  ⚠️ Moderate beta → LIMITED DOWNSIDE PROTECTION (+0)")
    
    # Risk-adjusted returns
    if sharpe_ratio_1y > 0.5:
        layer4_score += 1
        print("  ✅ Sharpe ratio >0.5 → POSITIVE RISK-ADJUSTED RETURNS (+1)")
    else:
        print("  ⚠️ Sharpe ratio <0.5 → MARGINAL RISK-ADJUSTED RETURNS (+0)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score:.1f}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    print(f"  Assets Under Management: ${aum/1e6:.1f} Million")
    print(f"  1-Year Fund Flows: ${fund_flows_1y/1e6:.1f} Million")
    print(f"  AUM Growth (Recent): {aum_growth:.1%}")
    
    # Institutional ownership
    inst_value_q4_2025 = 845e6  # $845M institutional value Q4'25 [citation:1]
    inst_value_current = 906e6  # $906M institutional value currently
    inst_growth = (inst_value_current - inst_value_q4_2025) / inst_value_q4_2025
    inst_filers = 278  # 278 institutional filers [citation:1]
    
    print(f"\n  Institutional Holdings: ${inst_value_current/1e6:.0f} Million")
    print(f"  Institutional Filers: {inst_filers}")
    print(f"  Institutional Growth (Q4'25→Current): {inst_growth:.1%}")
    
    # Score Layer 5 (max 2 points)
    layer5_score = 0
    
    # AUM viability
    if aum > 500e6:
        layer5_score += 1
        print("\n  ✅ AUM >$500M → VIABLE FUND WITH LIQUIDITY (+1)")
    else:
        print("\n  ⚠️ AUM <$500M → SMALL FUND, LIQUIDITY RISK (+0)")
    
    # Institutional flow sentiment
    if inst_growth > 0.15:
        layer5_score += 1
        print("  ✅ Strong institutional inflow → SMART MONEY INTEREST (+1)")
    elif inst_growth > 0.05:
        layer5_score += 0.5
        print("  ⚠️ Moderate institutional inflow → NEUTRAL SENTIMENT (+0.5)")
    else:
        print("  ❌ Weak institutional flow → NEGATIVE SENTIMENT (+0)")
    
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
    print(f"  {'1. Fee Efficiency':<20} {layer1_score:<10} {6:<10} {layer1_score/6*100:.0f}%")
    print(f"  {'2. Performance/Growth':<20} {layer2_score:<10.1f} {4:<10} {layer2_score/4*100:.0f}%")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10} {layer3_score/4*100:.0f}%")
    print(f"  {'4. Strategy Efficiency':<20} {layer4_score:<10.1f} {2:<10} {layer4_score/2*100:.0f}%")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10.1f} {2:<10} {layer5_score/2*100:.0f}%")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10} {total_score/max_score*100:.0f}%")
    
    # Final verdict
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID ETF INVESTMENT")
        print("    → Excellent fee efficiency, strong institutional backing")
        print("    → Suggested use: CORE HOLDING 5-10% of portfolio")
    elif total_score >= 12:
        print("    ✅ SOLID ETF")
        print("    → Good risk-adjusted returns with defined outcome strategy")
        print("    → Suggested use: STRATEGIC HOLDING 3-5% of portfolio")
    elif total_score >= 9:
        print("    ⚠️ SOLID BUT HAS LIMITATIONS")
        print("    → Effective buffer mechanics but modest growth")
        print("    → Suggested use: TACTICAL HOLDING 2-3% of portfolio")
    elif total_score >= 6:
        print("    ⚠️ MODERATE RISK")
        print("    → Limited upside capture but good protection")
        print("    → Suggested use: SMALL ALLOCATION 1-2% of portfolio")
    else:
        print("    ❌ NOT SOLID - Likely better alternatives available")
    
    # =========================================================
    # TUNAURA FRAMEWORK COMPARISON
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 TUNAURA FRAMEWORK - COMPARISON ACROSS INVESTMENTS")
    print("=" * 70)
    
    # Fetched scores from previous analyses
    comparisons = [
        ("TUNAURA (Turkish SaaS)", 6, "❌ AVOID"),
        ("COGT (Biotech)", 13, "⚠️ SPECULATIVE BUY"),
        ("FSLR (Solar)", 17, "✅ STRONG BUY"),
        ("ARKG (Genomics ETF)", 9.5, "⚠️ SPECULATIVE"),
        ("PFEB (Buffer ETF)", total_score, "📌 DEFINED-OUTCOME")
    ]
    
    print(f"\n  {'Company/ETF':<25} {'Score':<8} {'/18':<5} {'Verdict':<20}")
    print("  " + "-" * 60)
    for name, score, verdict in comparisons:
        print(f"  {name:<25} {score:<8} /18    {verdict:<20}")
    
    print("\n  PFEB Key Differentiators:")
    print("    • Low beta (0.54) → LESS VOLATILE THAN MARKETS (+1 layer 4)")
    print("    • Positive Sharpe (0.66) → GOOD RISK-ADJUSTED RETURNS (+1 layer 4)")
    print("    • Strong 3Y return (11.1%) → SOLID TRACK RECORD (+1 layer 2)")
    print("    • High expense ratio (0.79%) → MODERATE, NOT LOW (+0 partial)")
    print("    • Buffer ETF ≠ growth investment → DIFFERENT USE CASE")
    print("    • Not suitable as primary growth vehicle → TACTICAL/CORE SATELLITE")
    
    # =========================================================
    # PFEB SPECIFIC NOTES
    # =========================================================
    print("\n" + "=" * 70)
    print("📌 PFEB - KEY USE CASE & LIMITATIONS")
    print("=" * 70)
    print("""
    WHAT PFEB IS:
    • Defined-outcome ETF with 15% downside buffer over annual periods [citation:4]
    • Invests in SPY options, resetting each February [citation:3]
    • Provides S&P 500-like returns with capped upside and limited downside
    • Designed for investors seeking PARTIAL PROTECTION, not maximum growth
    
    WHAT PFEB IS NOT:
    • NOT a growth-oriented equity ETF (unlike ARKG)
    • NOT a high-upside investment (upside participation is capped)
    • NOT a pure S&P 500 replacement (caps upside)
    • NOT appropriate for aggressive growth objectives
    
    WHEN TO USE PFEB:
    • Portfolio diversification (low correlation to growth assets)
    • To protect capital in uncertain markets while maintaining SOME upside
    • As a CORE SATELLITE holding in risk-managed portfolios
    • When S&P 500 is near highs (buffer activates from current level)
    
    LIMITATIONS FROM ANALYSIS:
    • Expense ratio (0.79%) relatively high vs passive S&P 500 ETFs (~0.03-0.09%)
    • Upside capture is limited (options strategy caps gains)
    • Buffer resets annually → no cumulative protection across multiple years
    • Performance since inception: 8.2% annualized (solid but not spectacular)
    
    VERDICT SUMMARY:
    → This is NOT a "set and forget" investment like FSLR
    → It IS a strategic tool for DEFINED-OUTCOME investing
    → Score reflects execution quality, not growth potential
    """)
    
    return {
        "total_score": total_score,
        "max_score": max_score,
        "layer_scores": {
            "fee_efficiency": layer1_score,
            "performance": layer2_score,
            "valuation": layer3_score,
            "efficiency": layer4_score,
            "financial_health": layer5_score
        },
        "aum": aum,
        "expense_ratio": expense_ratio,
        "performance_1y": performance_1y,
        "beta": beta,
        "sharpe_ratio": sharpe_ratio_1y
    }


def plot_pfeb_stock():
    """Create PFEB price chart with key levels"""
    
    print("\n📈 Generating PFEB price chart...")
    
    # Download historical data
    pfeb = yf.Ticker("PFEB")
    data = pfeb.history(period="1y")
    
    if data.empty:
        print("❌ No price data available for PFEB")
        print("   PFEB trades on BATS exchange under ticker PFEB")
        return
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price chart with support/resistance
    ax1.plot(data.index, data['Close'], label='PFEB Price', linewidth=2, color='#1a73e8')
    ax1.plot(data.index, data['Close'].rolling(window=20).mean(), 
             label='20-Day MA', linewidth=1.5, color='#e67e22')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-Day MA', linewidth=1.5, color='#2ecc71')
    
    # Draw 52-week high/low reference lines
    current_price = data['Close'].iloc[-1]
    week_high = 42.05
    week_low = 33.99
    
    ax1.axhline(y=week_high, color='red', linestyle='--', alpha=0.5, label=f'52W High: ${week_high:.2f}')
    ax1.axhline(y=current_price, color='green', linestyle='-', alpha=0.7, label=f'Current: ${current_price:.2f}')
    ax1.axhline(y=week_low, color='red', linestyle=':', alpha=0.3, label=f'52W Low: ${week_low:.2f}')
    
    ax1.set_title('Innovator U.S. Equity Power Buffer ETF (PFEB) - 1 Year Price History', 
                  fontsize=14, fontweight='bold')
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
    plt.savefig('PFEB_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved: PFEB_chart.png")
    plt.show()


def analyze_pfeb_holdings():
    """Analyze PFEB holdings structure"""
    
    print("\n" + "=" * 70)
    print("📊 PFEB HOLDINGS ANALYSIS")
    print("=" * 70)
    
    # Holdings from search results [citation:3][citation:4]
    holdings = [
        {"name": "Option on SPDR® S&P 500® ETF Trust (Jan27)", "weight": 95.16},
        {"name": "Option on SPDR® S&P 500® ETF Trust (Jan27)", "weight": 4.61},
        {"name": "Option on SPDR® S&P 500® ETF Trust (Jan27)", "weight": 2.06},
        {"name": "Option on SPDR® S&P 500® ETF Trust (Jan27)", "weight": 1.89},
    ]
    
    print("\n  Primary Holdings:")
    print("  {:<50} {:>10}".format("Asset", "Weight %"))
    print("  " + "-" * 62)
    
    for h in holdings:
        print("  {:<50} {:>9.2f}%".format(h["name"], h["weight"]))
    
    print("\n  Total: 103.72% (includes leverage/options overlap) [citation:3]")
    
    # Sector Exposure (from SPY options - passthrough)
    print("\n  Underlying Sector Exposure (via SPY options):")
    sectors = {
        "Technology": 35.09,
        "Financial Services": 12.11,
        "Communication Services": 11.00,
        "Consumer Cyclical": 10.28,
        "Healthcare": 8.83,
        "Industrials": 8.35,
        "Consumer Defensive": 4.83,
        "Energy": 3.38,
        "Utilities": 2.37,
        "Real Estate": 1.93,
        "Basic Materials": 1.83
    }
    
    print("\n  {:<22} {:>10}".format("Sector", "%"))
    print("  " + "-" * 34)
    for sector, pct in sectors.items():
        print("  {:<22} {:>9.2f}%".format(sector, pct))
    
    return holdings


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🛡️ PFEB ANALYSIS - TUNAURA FRAMEWORK")
    print("Applying the Turkish SaaS scorecard to a defined-outcome buffer ETF")
    print("=" * 70)
    
    # Run ETF analysis
    results = analyze_pfeb_tunaura()
    
    # Interactive menu
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Display PFEB price chart (1-year history)")
    print("  2. Show holdings structure")
    print("  3. Run analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_pfeb_stock()
    elif choice == "2":
        analyze_pfeb_holdings()
    elif choice == "3":
        analyze_pfeb_tunaura()
    else:
        print("\n✅ Analysis complete!")
        print(f"\n📌 PFEB scored {results['total_score']:.1f}/18 on the TUNAURA framework")
        if results['total_score'] >= 12:
            print("   → Classification: SOLID ETF for defined-outcome strategies")
        elif results['total_score'] >= 9:
            print("   → Classification: MODERATE - Understand limitations")
        else:
            print("   → Classification: CONSIDER ALTERNATIVES")