"""
FIRST SOLAR (FSLR) - TUNAURA FRAMEWORK ANALYSIS
Applying the 5-layer scorecard developed for Turkish SaaS to a profitable solar manufacturer
Based on Q1 2026 earnings data (released April 30, 2026)
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_fslr_tunaura():
    """
    FSLR analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability (Gross Margin, Net Margin, EBITDA Margin)
    Layer 2: Growth (Revenue Growth, Volume Growth, Backlog)
    Layer 3: Valuation (P/E, PEG, Analyst Targets)
    Layer 4: Efficiency (Manufacturing Utilization, Cost Control)
    Layer 5: Financial Health (Debt, Cash Position, Liquidity)
    """
    
    print("=" * 70)
    print("🔆 FIRST SOLAR (FSLR)")
    print("TUNAURA FRAMEWORK ANALYSIS - Solar Manufacturing")
    print("Q1 2026 Data | Report Date: April 30, 2026")
    print("=" * 70)
    
    # Fetch data
    stock = yf.Ticker("FSLR")
    info = stock.info
    
    # =========================================================
    # LAYER 1: PROFITABILITY
    # FSLR is highly profitable with expansion momentum
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: PROFITABILITY")
    print("█" * 70)
    
    # Key profitability metrics from Q1 2026 earnings
    gross_margin = 0.47  # 47% from Q1 2026 earnings
    net_margin = 0.3073  # 30.73% net margin [citation:5]
    ebitda_margin = 0.50  # 50% adjusted EBITDA margin [citation:1][citation:2]
    
    print(f"  Gross Margin (Q1 2026): {gross_margin:.1%}")
    print(f"  Net Margin (TTM): {net_margin:.1%}")
    print(f"  Adjusted EBITDA Margin: {ebitda_margin:.1%}")
    
    # Score Layer 1 (max 6 points)
    layer1_score = 0
    
    # Gross margin assessment
    if gross_margin > 0.40:
        layer1_score += 2
        print("\n  ✅ Gross Margin >40% → EXCELLENT manufacturing profitability (+2)")
    elif gross_margin > 0.30:
        layer1_score += 1
        print("\n  ⚠️ Gross Margin 30-40% → GOOD (+1)")
    else:
        print("\n  ❌ Gross Margin <30% → WEAK (+0)")
    
    # Net margin assessment
    if net_margin > 0.20:
        layer1_score += 2
        print("  ✅ Net Margin >20% → EXCELLENT bottom line (+2)")
    elif net_margin > 0.10:
        layer1_score += 1
        print("  ⚠️ Net Margin 10-20% → GOOD (+1)")
    else:
        print("  ❌ Net Margin <10% → WEAK (+0)")
    
    # EBITDA margin assessment
    if ebitda_margin > 0.40:
        layer1_score += 2
        print("  ✅ EBITDA Margin >40% → STRONG cash generation (+2)")
    elif ebitda_margin > 0.25:
        layer1_score += 1
        print("  ⚠️ EBITDA Margin 25-40% → ADEQUATE (+1)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score}/6")
    
    # =========================================================
    # LAYER 2: GROWTH
    # FSLR showing strong volume growth with massive contracted backlog
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: GROWTH")
    print("█" * 70)
    
    # Growth metrics from Q1 2026 earnings
    revenue_growth_yoy = 0.24  # 24% YoY revenue growth [citation:1][citation:2]
    volume_growth_yoy = 0.31   # 31% increase in module volume [citation:1]
    eps_growth_yoy = 0.65      # 65% EPS growth [citation:2]
    
    contracted_backlog_gw = 47.9  # 47.9 GW contracted backlog [citation:1][citation:2]
    backlog_value_billion = 14.4  # $14.4 billion aggregate transaction price [citation:1]
    
    print(f"  Revenue Growth (YoY): {revenue_growth_yoy:.1%}")
    print(f"  Volume Growth (YoY): {volume_growth_yoy:.1%}")
    print(f"  EPS Growth (YoY): {eps_growth_yoy:.1%}")
    print(f"\n  Contracted Backlog: {contracted_backlog_gw:.1f} GW")
    print(f"  Backlog Value: ${backlog_value_billion:.1f} Billion")
    print(f"  Backlog Visibility: Through 2030")
    
    # Score Layer 2 (max 4 points)
    layer2_score = 0
    
    # Revenue growth assessment
    if revenue_growth_yoy > 0.20:
        layer2_score += 2
        print("\n  ✅ Revenue Growth >20% → STRONG (+2)")
    elif revenue_growth_yoy > 0.10:
        layer2_score += 1
        print("\n  ⚠️ Revenue Growth 10-20% → MODERATE (+1)")
    else:
        print("\n  ❌ Revenue Growth <10% → WEAK (+0)")
    
    # Backlog visibility (multi-year contracted revenue)
    if contracted_backlog_gw > 30:
        layer2_score += 2
        print("  ✅ Contracted Backlog >30 GW → EXCELLENT VISIBILITY (+2)")
    elif contracted_backlog_gw > 15:
        layer2_score += 1
        print("  ⚠️ Contracted Backlog 15-30 GW → GOOD (+1)")
    
    print(f"\n  LAYER 2 SCORE: {layer2_score}/4")
    
    # =========================================================
    # LAYER 3: VALUATION
    # P/E, P/B, Analyst targets
    # =========================================================
    print("\n" + "█" * 70)
    print("💰 LAYER 3: VALUATION")
    print("█" * 70)
    
    current_price = info.get('currentPrice', info.get('regularMarketPrice', 211.71))
    market_cap = info.get('marketCap', 22.75e9)
    pe_ratio_ttm = info.get('trailingPE', 13.66)
    pe_ratio_forward = info.get('forwardPE', 0)
    peg_ratio = info.get('pegRatio', 0.46)
    price_to_book = info.get('priceToBook', 2.30)
    
    # Analyst targets from Q1 earnings reactions [citation:5]
    target_mean = 245.47
    target_high = 310.00  # Goldman Sachs raised to $310 [citation:5]
    target_low = 213.00   # Barclays lowered to $213 [citation:5]
    
    print(f"  Current Price: ${current_price:.2f}")
    print(f"  Market Cap: ${market_cap/1e9:.2f} Billion")
    print(f"  P/E (TTM): {pe_ratio_ttm:.2f}x")
    print(f"  PEG Ratio: {peg_ratio:.2f}x")
    print(f"  Price-to-Book (P/B): {price_to_book:.2f}x")
    print(f"\n  Analyst Mean Target: ${target_mean:.2f}")
    print(f"  Analyst High Target: ${target_high:.2f}")
    print(f"  Analyst Low Target: ${target_low:.2f}")
    
    # Score Layer 3 (max 4 points)
    layer3_score = 0
    
    # Upside calculation
    upside_to_mean = (target_mean - current_price) / current_price * 100
    print(f"\n  Upside to Mean Target: {upside_to_mean:.1f}%")
    
    # P/E assessment (comparing to market and growth)
    if pe_ratio_ttm < 15 and eps_growth_yoy > 0.20:
        layer3_score += 2
        print("  ✅ P/E <15x with >20% EPS growth → ATTRACTIVE PEG (+2)")
    elif pe_ratio_ttm < 20:
        layer3_score += 1
        print("  ⚠️ P/E <20x → REASONABLE (+1)")
    else:
        print("  ❌ P/E >20x → EXPENSIVE (+0)")
    
    # Analyst upside assessment
    if upside_to_mean > 30:
        layer3_score += 2
        print(f"  ✅ >30% Analyst Upside → SIGNIFICANT UPSIDE POTENTIAL (+2)")
    elif upside_to_mean > 15:
        layer3_score += 1
        print(f"  ⚠️ 15-30% Analyst Upside → MODERATE UPSIDE (+1)")
    else:
        print(f"  ❌ <15% Upside → LIMITED UPSIDE (+0)")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: EFFICIENCY
    # Manufacturing utilization, cost control, operating leverage
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: OPERATIONAL EFFICIENCY")
    print("█" * 70)
    
    # Efficiency metrics from Q1 2026 earnings
    us_utilization = 0.96  # 96% utilization at U.S. facilities [citation:1]
    quarterly_production_gw = 4.3  # 4.3 GW produced in Q1 [citation:1]
    sales_freight_cost_per_watt = 0.017  # $0.017 per watt, down 50% YoY [citation:1]
    
    print(f"  U.S. Facility Utilization: {us_utilization:.1%}")
    print(f"  Quarterly Production: {quarterly_production_gw:.1f} GW")
    print(f"  Sales Freight Cost: ${sales_freight_cost_per_watt:.3f}/watt (↓50% YoY)")
    
    # Score Layer 4 (max 2 points)
    layer4_score = 0
    
    # Utilization assessment
    if us_utilization > 0.90:
        layer4_score += 1
        print("\n  ✅ Utilization >90% → HIGH MANUFACTURING EFFICIENCY (+1)")
    else:
        print("\n  ⚠️ Utilization <90% → ROOM FOR IMPROVEMENT (+0)")
    
    # Cost reduction trend
    print("  Cost Reduction Drivers:")
    print("    • Sales freight costs reduced 50% YoY")
    print("    • Warehouse costs: $22M sequential reduction")
    print("    • On track for $100M warehouse cost rationalization by 2027")
    layer4_score += 1
    print("\n  ✅ Demonstrated Cost Reduction Momentum (+1)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # Cash position, debt, liquidity
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    # Financial health metrics from Q1 2026 and year-end 2025 [citation:1][citation:4][citation:8]
    gross_cash = 2.4e9  # $2.4 billion gross cash [citation:1]
    net_cash = 2.0e9   # $2.0 billion net cash [citation:1]
    total_debt = 655e6  # $655 million total debt [citation:4]
    debt_to_equity = 0.03  # 0.03 debt-to-equity [citation:5]
    current_ratio = 2.67  # 2.67 current ratio [citation:5]
    quick_ratio = 2.35    # 2.35 quick ratio [citation:5]
    
    print(f"  Gross Cash Balance: ${gross_cash/1e9:.1f} Billion")
    print(f"  Net Cash Position: ${net_cash/1e9:.1f} Billion")
    print(f"  Total Debt: ${total_debt/1e6:.0f} Million")
    print(f"  Debt-to-Equity: {debt_to_equity:.2f}")
    print(f"  Current Ratio: {current_ratio:.2f}")
    print(f"  Quick Ratio: {quick_ratio:.2f}")
    
    # Score Layer 5 (max 2 points)
    layer5_score = 0
    
    # Debt assessment
    if debt_to_equity < 0.1:
        layer5_score += 1
        print("\n  ✅ Minimal Debt (<0.1 D/E) → CONSERVATIVE CAPITAL STRUCTURE (+1)")
    elif debt_to_equity < 0.5:
        layer5_score += 0.5
        print("\n  ⚠️ Moderate Debt → MANAGEABLE (+0.5)")
    else:
        print("\n  ❌ High Debt → LEVERAGED (+0)")
    
    # Liquidity assessment
    if current_ratio > 2.0:
        layer5_score += 1
        print("  ✅ Current Ratio >2.0 → STRONG LIQUIDITY (+1)")
    elif current_ratio > 1.5:
        layer5_score += 0.5
        print("  ⚠️ Current Ratio 1.5-2.0 → ADEQUATE LIQUIDITY (+0.5)")
    
    print(f"\n  LAYER 5 SCORE: {layer5_score}/2")
    
    # =========================================================
    # TUNAURA FRAMEWORK FINAL SCORECARD
    # =========================================================
    print("\n" + "=" * 70)
    print("🎯 TUNAURA FRAMEWORK - FINAL SCORECARD")
    print("=" * 70)
    
    total_score = layer1_score + layer2_score + layer3_score + layer4_score + layer5_score
    max_score = 6 + 4 + 4 + 2 + 2  # = 18 (same as original TUNAURA)
    
    print(f"\n  {'Layer':<20} {'Score':<10} {'Max':<10} {'%':<10}")
    print("  " + "-" * 50)
    print(f"  {'1. Profitability':<20} {layer1_score:<10} {6:<10} {layer1_score/6*100:.0f}%")
    print(f"  {'2. Growth':<20} {layer2_score:<10} {4:<10} {layer2_score/4*100:.0f}%")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10} {layer3_score/4*100:.0f}%")
    print(f"  {'4. Operational Efficiency':<20} {layer4_score:<10} {2:<10} {layer4_score/2*100:.0f}%")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10} {2:<10} {layer5_score/2*100:.0f}%")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10} {total_score/max_score*100:.0f}%")
    
    # Final verdict (same classification as TUNAURA)
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID BUSINESS (TUNAURA equivalent)")
        print("    → Exceptional profitability, strong growth, minimal debt")
        print("    → Suggested position: 4-5% of portfolio for core holdings")
    elif total_score >= 12:
        print("    ✅ SOLID BUSINESS")
        print("    → Strong fundamentals with clear growth catalysts")
        print("    → Suggested position: 3-4% of portfolio")
    elif total_score >= 9:
        print("    ⚠️ SOLID BUT HAS RISKS")
        print("    → Watch policy/trade developments and margin sustainability")
        print("    → Suggested position: 2-3% of portfolio")
    elif total_score >= 6:
        print("    ⚠️ WEAK - High Risk")
        print("    → Speculative only, small position")
        print("    → Suggested position: 1-2% of portfolio")
    else:
        print("    ❌ NOT SOLID - Avoid")
    
    # =========================================================
    # TUNAURA FRAMEWORK COMPARISON TABLE
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 TUNAURA FRAMEWORK - COMPANY COMPARISON")
    print("=" * 70)
    
    # Stored scores from previous analyses (approximate)
    companies = [
        ("TUNAURA (Turkish SaaS)", 6, "AVOID - Fake employees, no growth"),
        ("COGT (Biotech)", 13, "SPECULATIVE BUY - Strong cash, pipeline catalysts"),
        ("FSLR (Solar)", total_score, "SOLID BUY" if total_score >= 12 else "MONITOR")
    ]
    
    print(f"\n  {'Company':<25} {'Score':<8} {'/18':<5} {'Verdict':<30}")
    print("  " + "-" * 70)
    for name, score, verdict in companies:
        print(f"  {name:<25} {score:<8} /18    {verdict:<30}")
    
    print("\n  Key Differentiators for FSLR:")
    print("    • TUNAURA failed on Growth (0/4) and fake employee data")
    print("    • COGT is pre-revenue biotech with binary risk")
    print("    • FSLR is PROFITABLE GROWTH with 47% gross margins & 47.9 GW backlog")
    
    # =========================================================
    # RISK FACTORS (Specific to FSLR)
    # =========================================================
    print("\n" + "=" * 70)
    print("⚠️ FSLR-SPECIFIC RISK FACTORS")
    print("=" * 70)
    print("""
    1. Policy & Trade Risks:
       • Pending 232 polysilicon derivatives tariff decision
       • Proposed FEOP regulations could impact module sales
       • Section 337 investigation on TOPCon IP (initial determination ~11 months)
    
    2. Section 45X Tax Credit Dependency:
       • Gross margin includes significant 45X benefits
       • 2026 guidance assumes current U.S. policy environment persists
    
    3. International Operations Headwinds:
       • Malaysia/Vietnam facilities at reduced utilization
       • Lower ASP expectations for internationally produced modules
    
    4. Competitive Dynamics:
       • Chinese crystalline silicon supply chain increasingly constrained
       • But creates opportunity for differentiated CdTe technology
    
    5. Insider Activity:
       • $14.7M in insider selling over past 3 months [citation:7]
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
        "key_metrics": {
            "gross_margin": gross_margin,
            "net_margin": net_margin,
            "revenue_growth": revenue_growth_yoy,
            "backlog_gw": contracted_backlog_gw,
            "pe_ratio": pe_ratio_ttm,
            "net_cash_billion": net_cash/1e9,
            "debt_to_equity": debt_to_equity
        }
    }


def plot_fslr_chart():
    """Create stock price chart for FSLR"""
    
    print("\n📈 Generating FSLR price chart...")
    
    stock = yf.Ticker("FSLR")
    data = stock.history(period="1y")
    
    if data.empty:
        print("❌ No price data available")
        return
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price chart with moving averages
    ax1.plot(data.index, data['Close'], label='Close Price', linewidth=2, color='#1a73e8')
    ax1.plot(data.index, data['Close'].rolling(window=20).mean(), 
             label='20-Day MA', linewidth=1.5, color='#e67e22')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-Day MA', linewidth=1.5, color='#2ecc71')
    
    ax1.set_title('First Solar (FSLR) - 1 Year Price History', fontsize=14, fontweight='bold')
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
    plt.savefig('FSLR_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved: FSLR_chart.png")
    plt.show()


def compare_peers():
    """Compare FSLR with solar industry peers"""
    
    peers = ["FSLR", "ENPH", "NXT", "RUN", "SPWR"]
    peer_names = {
        "FSLR": "First Solar",
        "ENPH": "Enphase Energy",
        "NXT": "Nextracker",
        "RUN": "Sunrun",
        "SPWR": "SunPower"
    }
    
    print("\n" + "=" * 70)
    print("☀️ FSLR vs. SOLAR INDUSTRY PEERS")
    print("=" * 70)
    
    results = []
    for ticker in peers:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        market_cap = info.get('marketCap', 0)
        pe_ratio = info.get('trailingPE', 0)
        gross_margin = info.get('grossMargins', 0)
        debt_to_equity = info.get('debtToEquity', 0)
        
        results.append({
            "Ticker": ticker,
            "Name": peer_names.get(ticker, ticker)[:12],
            "Market Cap (B)": market_cap / 1e9 if market_cap else 0,
            "P/E": pe_ratio if pe_ratio else 0,
            "Gross Margin": gross_margin if gross_margin else 0,
            "D/E": debt_to_equity if debt_to_equity else 0
        })
    
    print("\n{:<8} {:<14} {:>14} {:>10} {:>12} {:>10}".format(
        "Ticker", "Company", "Market Cap (B)", "P/E", "Gross Margin", "D/E"))
    print("-" * 75)
    
    for r in results:
        print("{:<8} {:<14} {:>13.2f} {:>10.1f} {:>11.1%} {:>10.2f}".format(
            r["Ticker"], r["Name"], r["Market Cap (B)"], r["P/E"], r["Gross Margin"], r["D/E"]))
    
    # FSLR positioning
    print("\n  FSLR differentiators:")
    print("    • Industry-leading gross margins (>45% vs peers 20-35%)")
    print("    • Minimal debt (D/E 0.03 vs industry average >0.5)")
    print("    • Vertically integrated U.S. manufacturing footprint")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🔆 FIRST SOLAR (FSLR) ANALYSIS - TUNAURA FRAMEWORK")
    print("Applying the Turkish SaaS scorecard to profitable solar manufacturing")
    print("=" * 70)
    
    # Run analysis
    results = analyze_fslr_tunaura()
    
    # Display key metrics summary
    print("\n" + "=" * 70)
    print("📊 KEY METRICS SUMMARY")
    print("=" * 70)
    metrics = results['key_metrics']
    print(f"""
    Gross Margin:        {metrics['gross_margin']:.1%}
    Net Margin:          {metrics['net_margin']:.1%}
    Revenue Growth:      {metrics['revenue_growth']:.1%}
    Contracted Backlog:  {metrics['backlog_gw']:.1f} GW (through 2030)
    P/E Ratio:           {metrics['pe_ratio']:.2f}x
    Net Cash:            ${metrics['net_cash_billion']:.1f} Billion
    Debt/Equity:         {metrics['debt_to_equity']:.2f}
    """)
    
    # Interactive menu
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Display FSLR price chart")
    print("  2. Compare with solar industry peers")
    print("  3. Run analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_fslr_chart()
    elif choice == "2":
        compare_peers()
    elif choice == "3":
        analyze_fslr_tunaura()
    else:
        print("\n✅ Analysis complete!")
        print(f"\n📌 FSLR scored {results['total_score']:.1f}/18 on the TUNAURA framework")
        print("   → Classification: SOLID BUSINESS - Strong fundamentals across all 5 layers")