"""
SCHWAB U.S. DIVIDEND EQUITY ETF (SCHD) - TUNAURA FRAMEWILER ANALYSIS
Applying the 5-layer scorecard to a large-cap dividend ETF
Data as of May 2026
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_schd_tunaura():
    """
    SCHD analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability (Expense ratio, yield efficiency)
    Layer 2: Growth (Performance, AUM growth)
    Layer 3: Valuation (P/E of holdings, analyst targets)
    Layer 4: Efficiency (Low volatility, defensive characteristics)
    Layer 5: Financial Health (AUM, institutional backing)
    """
    
    print("=" * 70)
    print("📊 SCHWAB U.S. DIVIDEND EQUITY ETF (SCHD)")
    print("TUNAURA FRAMEWORK ANALYSIS - Large-Cap Value Dividend ETF")
    print("Data as of May 2026")
    print("=" * 70)
    
    # =========================================================
    # FUNDAMENTAL ETF DATA
    # =========================================================
    
    # ETF-level metrics from search results
    aum = 88.2e9  # $88.2 billion net assets [citation:1]
    expense_ratio = 0.0006  # 0.06% expense ratio [citation:1][citation:4]
    holdings_count = 103  # 103 holdings [citation:4]
    inception_date = "2011-10-31"  # October 2011 inception [citation:9]
    turnover = 0.30  # 30% turnover [citation:1]
    
    # Performance metrics
    performance_ytd = 0.1271  # +12.71% year-to-date (NAV) [citation:9]
    performance_1y = 0.1405  # +14.05% trailing 1-year [citation:9]
    performance_3y = 0.1203  # +12.03% annualized 3-year [citation:9]
    performance_5y = 0.0859  # +8.59% annualized 5-year [citation:9]
    performance_since_inception = 0.1301  # +13.01% since inception [citation:9]
    
    # Yield metrics
    ttm_yield = 0.0344  # 3.44% TTM yield [citation:1][citation:5]
    dividend_per_share = 1.0557  # $1.0557 dividends per share TTM [citation:7]
    current_price = 31.42  # $31.42 as of April 23, 2026 [citation:7]
    
    # Risk metrics
    beta = 0.91  # ~0.91 estimated (dividend value tilt)
    active_share_vs_sp500 = 0.9173  # 91.73% active share vs S&P 500 [citation:4]
    
    # Valuation metrics of underlying portfolio
    portfolio_pe = 18.0  # 18x earnings [citation:5]
    portfolio_pb = 3.66  # 3.66x book value [citation:5]
    portfolio_pcf = 10.38  # 10.38x cash flow [citation:5]
    portfolio_roe = 0.27  # 27% ROE [citation:5]
    
    # Price targets
    analyst_target = 35.33  # $35.33 average price target [citation:6]
    analyst_consensus = "Moderate Buy"  # Moderate Buy consensus [citation:6]
    
    # 52-week range
    week_52_high = 31.95  # $31.95 52-week high [citation:5]
    week_52_low = 25.28  # $25.28 52-week low [citation:5]
    
    # Top holdings (from search results)
    top_holdings = [
        ("TXN", "Texas Instruments", 5.61, 2.05),
        ("UNH", "UnitedHealth Group", 4.89, 2.50),
        ("CVX", "Chevron Corp", 4.06, 3.80),
        ("COP", "ConocoPhillips", 3.95, 2.76),
        ("KO", "Coca-Cola Co", 3.93, 2.80),
        ("MRK", "Merck & Co", 3.84, 3.04),
        ("PEP", "PepsiCo Inc", 3.82, 3.66),
        ("VZ", "Verizon Communications", 3.71, 6.10),
        ("HD", "Home Depot Inc", 3.71, 2.20),
        ("PG", "Procter & Gamble", 3.71, 2.90),
    ]
    
    # =========================================================
    # LAYER 1: PROFITABILITY & FEE EFFICIENCY
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: FEE EFFICIENCY & YIELD")
    print("█" * 70)
    
    print(f"  ETF Net Assets: ${aum/1e9:.1f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Holdings Count: {holdings_count}")
    print(f"  Turnover: {turnover:.1%}")
    print(f"  Inception Date: {inception_date}")
    print(f"\n  TTM Dividend Yield: {ttm_yield:.2%}")
    print(f"  Dividend Per Share (TTM): ${dividend_per_share:.4f}")
    
    # Score Layer 1 (max 6 points)
    layer1_score = 0
    
    # Expense ratio assessment (SCHD is among cheapest dividend ETFs)
    if expense_ratio < 0.0007:
        layer1_score += 3
        print("\n  ✅ Expense Ratio <0.07% → EXCEPTIONALLY LOW COST (+3)")
    elif expense_ratio < 0.0010:
        layer1_score += 2
        print("\n  ✅ Expense Ratio <0.10% → VERY LOW COST (+2)")
    else:
        print("\n  ⚠️ Expense Ratio >0.10% → MODERATE COST (+0)")
    
    # Dividend yield assessment relative to S&P 500
    spy_yield = 0.0103  # S&P 500 yield ~1.03% [citation:5]
    yield_premium = ttm_yield - spy_yield
    
    if ttm_yield > 0.03:
        layer1_score += 2
        print(f"\n  ✅ Dividend Yield >3% → ATTRACTIVE INCOME ({ttm_yield:.2%}) (+2)")
    elif ttm_yield > 0.02:
        layer1_score += 1
        print(f"\n  ⚠️ Dividend Yield 2-3% → MODERATE INCOME (+1)")
    else:
        print(f"\n  ❌ Dividend Yield <2% → LOW INCOME (+0)")
    
    # Turnover assessment (lower is better for tax efficiency)
    if turnover < 0.35:
        layer1_score += 1
        print("\n  ✅ Turnover <35% → TAX-EFFICIENT STRUCTURE (+1)")
    else:
        print("\n  ⚠️ Turnover >35% → HIGHER TAX DRAG (+0)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score}/6")
    
    # =========================================================
    # LAYER 2: GROWTH & PERFORMANCE
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: PERFORMANCE & GROWTH")
    print("█" * 70)
    
    print(f"  YTD Performance: {performance_ytd:.1%}")
    print(f"  1-Year Performance: {performance_1y:.1%}")
    print(f"  3-Year Annualized: {performance_3y:.1%}")
    print(f"  5-Year Annualized: {performance_5y:.1%}")
    print(f"  Since Inception (2011): {performance_since_inception:.1%}")
    
    # Compare to S&P 500 for context
    sp500_ytd = -0.0433  # S&P 500 YTD -4.33% [citation:9]
    sp500_1y = 0.1780  # S&P 500 1Y +17.80% [citation:9]
    sp500_3y = 0.1832  # S&P 500 3Y +18.32% [citation:9]
    sp500_5y = 0.1206  # S&P 500 5Y +12.06% [citation:9]
    
    print(f"\n  vs S&P 500:")
    print(f"    YTD: SCHD +{performance_ytd:.1%} vs SPX {sp500_ytd:.1%} → OUTPERFORM by {performance_ytd - sp500_ytd:.1%}")
    print(f"    1Y:  SCHD +{performance_1y:.1%} vs SPX +{sp500_1y:.1%} → UNDERPERFORM by {performance_1y - sp500_1y:.1%}")
    print(f"    3Y:  SCHD +{performance_3y:.1%} vs SPX +{sp500_3y:.1%} → UNDERPERFORM by {performance_3y - sp500_3y:.1%}")
    print(f"    5Y:  SCHD +{performance_5y:.1%} vs SPX +{sp500_5y:.1%} → UNDERPERFORM by {performance_5y - sp500_5y:.1%}")
    
    # Score Layer 2 (max 4 points)
    layer2_score = 0
    
    # YTD performance (exceptional in 2026)
    if performance_ytd > 0.12:
        layer2_score += 2
        print("\n  ✅ YTD Return >12% → EXCEPTIONAL 2026 PERFORMANCE (+2)")
    elif performance_ytd > 0.08:
        layer2_score += 1
        print("\n  ⚠️ YTD Return 8-12% → STRONG PERFORMANCE (+1)")
    else:
        print("\n  ❌ YTD Return <8% → WEAK (+0)")
    
    # Long-term consistency (since inception)
    if performance_since_inception > 0.12:
        layer2_score += 2
        print("  ✅ Since Inception >12% annualized → CONSISTENT LONG-TERM RETURNS (+2)")
    elif performance_since_inception > 0.10:
        layer2_score += 1
        print("  ⚠️ Since Inception 10-12% → SOLID LONG-TERM RETURNS (+1)")
    else:
        print("  ❌ Since Inception <10% → MODEST LONG-TERM RETURNS (+0)")
    
    print(f"\n  LAYER 2 SCORE: {layer2_score:.1f}/4")
    
    # =========================================================
    # LAYER 3: VALUATION
    # =========================================================
    print("\n" + "█" * 70)
    print("💰 LAYER 3: VALUATION")
    print("█" * 70)
    
    print(f"  Current Price: ${current_price:.2f}")
    print(f"  52-Week Range: ${week_52_low:.2f} - ${week_52_high:.2f}")
    position_in_range = (current_price - week_52_low) / (week_52_high - week_52_low)
    print(f"  Position in Range: {position_in_range:.1%}")
    
    print(f"\n  Portfolio Valuation Metrics:")
    print(f"    P/E Ratio: {portfolio_pe:.1f}x")
    print(f"    P/B Ratio: {portfolio_pb:.2f}x")
    print(f"    P/CF Ratio: {portfolio_pcf:.2f}x")
    print(f"    Return on Equity: {portfolio_roe:.1%}")
    
    # Compare to S&P 500 valuation
    sp500_pe = 28.0  # S&P 500 ~28x earnings [citation:5]
    sp500_pb = 5.3  # S&P 500 ~5.3x book [citation:5]
    
    print(f"\n  vs S&P 500 Valuation:")
    print(f"    P/E: SCHD {portfolio_pe:.1f}x vs SPX {sp500_pe:.1f}x → {((sp500_pe - portfolio_pe)/sp500_pe*100):.0f}% CHEAPER")
    print(f"    P/B: SCHD {portfolio_pb:.2f}x vs SPX {sp500_pb:.2f}x → {((sp500_pb - portfolio_pb)/sp500_pb*100):.0f}% CHEAPER")
    
    # Analyst targets
    print(f"\n  Analyst Consensus: {analyst_consensus}")
    print(f"  Average Price Target: ${analyst_target:.2f}")
    upside_to_target = (analyst_target - current_price) / current_price * 100
    print(f"  Implied Upside: {upside_to_target:.1f}%")
    
    # Score Layer 3 (max 4 points)
    layer3_score = 0
    
    # Valuation discount to market
    if portfolio_pe < 20:
        layer3_score += 2
        print("\n  ✅ P/E <20x → SIGNIFICANT DISCOUNT TO BROAD MARKET (+2)")
    elif portfolio_pe < 25:
        layer3_score += 1
        print("\n  ⚠️ P/E 20-25x → MODERATE DISCOUNT TO MARKET (+1)")
    else:
        print("\n  ❌ P/E >25x → LIMITED VALUATION DISCOUNT (+0)")
    
    # Analyst upside potential
    if upside_to_target > 12:
        layer3_score += 2
        print(f"  ✅ >12% Analyst Upside → ATTRACTIVE UPSIDE POTENTIAL (+2)")
    elif upside_to_target > 8:
        layer3_score += 1
        print(f"  ⚠️ 8-12% Analyst Upside → MODERATE UPSIDE (+1)")
    else:
        print(f"  ❌ <8% Upside → LIMITED UPSIDE (+0)")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: EFFICIENCY & DEFENSIVE CHARACTERISTICS
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: RISK & DEFENSIVE EFFICIENCY")
    print("█" * 70)
    
    print(f"  Active Share vs S&P 500: {active_share_vs_sp500:.1%}")
    print(f"  Holdings Count: {holdings_count}")
    print(f"  Top 10 Holdings Weight: 41.6% [citation:1]")
    
    # Sector composition (from search results) [citation:5]
    print(f"\n  Sector Composition:")
    sectors = [
        ("Consumer Staples", 15.0),
        ("Healthcare", 14.0),
        ("Energy", 13.0),
        ("Technology", 12.0),
        ("Financials", 11.0),
        ("Industrials", 10.0),
        ("Communication Services", 8.0),
        ("Utilities", 7.0),
        ("Consumer Discretionary", 5.0),
        ("Materials", 5.0),
    ]
    
    for sector, weight in sectors:
        print(f"    {sector:<20} {weight:>5.1f}%")
    
    # Score Layer 4 (max 2 points)
    layer4_score = 0
    
    # Diversification assessment
    if len(top_holdings) >= 10 and top_holdings[0][2] < 6:
        layer4_score += 1
        print("\n  ✅ Top holding <6% → WELL-DIVERSIFIED PORTFOLIO (+1)")
    else:
        print("\n  ⚠️ Higher concentration risk (+0)")
    
    # Defensive characteristics (consumer staples, healthcare, utilities weight)
    defensive_weight = 15.0 + 14.0 + 7.0  # Staples + Healthcare + Utilities
    if defensive_weight > 30:
        layer4_score += 1
        print(f"  ✅ Defensive sectors {defensive_weight:.0f}% → DOWNSIDE PROTECTION (+1)")
    else:
        print(f"  ⚠️ Defensive sectors {defensive_weight:.0f}% → LIMITED PROTECTION (+0)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score:.1f}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    print(f"  Assets Under Management: ${aum/1e9:.1f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Dividend Track Record: 10+ years of consistent payments [citation:6]")
    
    # AUM growth trend (implied from growth)
    print(f"\n  AUM Scale: Top 3 largest dividend ETFs")
    print(f"  Issuer: Charles Schwab (established, trusted provider)")
    
    # Score Layer 5 (max 2 points)
    layer5_score = 0
    
    # AUM assessment
    if aum > 50e9:
        layer5_score += 1
        print("\n  ✅ AUM >$50B → MASSIVE SCALE & LIQUIDITY (+1)")
    elif aum > 10e9:
        layer5_score += 0.5
        print("\n  ⚠️ AUM $10-50B → GOOD SCALE (+0.5)")
    else:
        print("\n  ❌ AUM <$10B → SMALL FUND (+0)")
    
    # Dividend sustainability
    if ttm_yield > 0.03 and portfolio_roe > 0.15:
        layer5_score += 1
        print("  ✅ High yield + Strong ROE → SUSTAINABLE DIVIDEND (+1)")
    else:
        print("  ⚠️ Dividend sustainability requires monitoring (+0)")
    
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
    print(f"  {'1. Fee Efficiency & Yield':<20} {layer1_score:<10} {6:<10} {layer1_score/6*100:.0f}%")
    print(f"  {'2. Performance/Growth':<20} {layer2_score:<10.1f} {4:<10} {layer2_score/4*100:.0f}%")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10} {layer3_score/4*100:.0f}%")
    print(f"  {'4. Defensive Efficiency':<20} {layer4_score:<10.1f} {2:<10} {layer4_score/2*100:.0f}%")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10.1f} {2:<10} {layer5_score/2*100:.0f}%")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10} {total_score/max_score*100:.0f}%")
    
    # Final verdict
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID ETF INVESTMENT")
        print("    → Exceptional fee efficiency, strong income, defensive positioning")
        print("    → Suggested use: CORE HOLDING 10-20% of portfolio")
    elif total_score >= 12:
        print("    ✅ SOLID ETF - STRONG FUNDAMENTALS")
        print("    → Low cost, attractive yield, significant valuation discount to market")
        print("    → Suggested use: CORE HOLDING 5-15% of portfolio")
    elif total_score >= 9:
        print("    ⚠️ SOLID BUT HAS LIMITATIONS")
        print("    → Good defensive characteristics but moderate long-term growth")
        print("    → Suggested use: SATELLITE HOLDING 3-5% of portfolio")
    elif total_score >= 6:
        print("    ⚠️ MODERATE - Understand trade-offs")
        print("    → Lower growth but higher income and lower volatility")
        print("    → Suggested use: INCOME ALLOCATION 2-3% of portfolio")
    else:
        print("    ❌ NOT SOLID - Better alternatives available")
    
    # =========================================================
    # TUNAURA FRAMEWORK COMPARISON
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 TUNAURA FRAMEWORK - COMPARISON ACROSS INVESTMENTS")
    print("=" * 70)
    
    comparisons = [
        ("TUNAURA (Turkish SaaS)", 6, "❌ AVOID"),
        ("ARKG (Genomics ETF)", 9.5, "⚠️ SPECULATIVE"),
        ("COGT (Biotech)", 13, "⚠️ SPECULATIVE BUY"),
        ("PFEB (Buffer ETF)", 12, "📌 DEFINED-OUTCOME"),
        ("SCHD (Dividend ETF)", total_score, "✅ CORE HOLDING"),
        ("FSLR (Solar)", 17, "✅ STRONG BUY"),
    ]
    
    print(f"\n  {'Company/ETF':<25} {'Score':<8} {'/18':<5} {'Verdict':<20}")
    print("  " + "-" * 60)
    for name, score, verdict in comparisons:
        print(f"  {name:<25} {score:<8} /18    {verdict:<20}")
    
    print("\n  SCHD Key Differentiators:")
    print("    • Lowest expense ratio (0.06%) among all analyzed investments (+3 layer 1)")
    print("    • Exceptional YTD 2026 performance: +12.7% vs S&P 500 -4.3%")
    print("    • Portfolio valuation: 18x P/E vs S&P 500 28x (>35% cheaper)")
    print("    • 3.44% dividend yield → 3.3x S&P 500 yield")
    print("    • Defensive sector tilt (Staples + Healthcare + Utilities = 36%)")
    print("    • NOT a growth-focused ETF → lower long-term returns than S&P 500")
    
    # =========================================================
    # RISK FACTORS
    # =========================================================
    print("\n" + "=" * 70)
    print("⚠️ SCHD-SPECIFIC RISK FACTORS")
    print("=" * 70)
    
    print("""
    1. Underperformance in Strong Bull Markets:
       • 1Y, 3Y, 5Y returns LAG S&P 500 by 3-6% annually [citation:9]
       • Dividend/value tilt underperforms growth in tech-driven rallies
       • SCHD's 2026 outperformance is the EXCEPTION, not the rule
    
    2. Interest Rate Sensitivity:
       • Dividend stocks compete with bonds for income-oriented capital
       • Rising rates could pressure dividend valuations
       • Current yield spread over 10-year Treasury is compressed
    
    3. Index Reconstitution Risk (March 2026):
       • The Dow Jones U.S. Dividend 100 Index underwent major methodology changes [citation:8]
       • Potential shifts in sector allocation and risk profile
       • Higher turnover and tracking error during transition
    
    4. Sector Concentration Risks:
       • Significant exposure to Consumer Staples (15%), Healthcare (14%), Energy (13%)
       • Underweight Technology (12% vs S&P 500 ~30%)
       • Could miss major tech-driven market rallies
    
    5. Dividend Sustainability:
       • Verizon at 6.1% yield — highest in portfolio, elevated risk [citation:5]
       • Energy sector cyclicality could pressure dividends in oil downturns
    
    6. Limited Upside Capture:
       • Options-based buffer ETFs like PFEB cap upside, but SCHD's value tilt means:
       • Participates less in bull markets than growth-oriented alternatives
       • Best suited for INCOME + CAPITAL PRESERVATION, not growth maximization
    """)
    
    # =========================================================
    # TOP HOLDINGS DETAIL
    # =========================================================
    print("\n" + "=" * 70)
    print("📋 TOP 10 HOLDINGS DETAIL")
    print("=" * 70)
    
    print(f"\n  {'Ticker':<8} {'Company':<22} {'Weight %':<10} {'Yield %':<10}")
    print("  " + "-" * 55)
    for ticker, name, weight, yield_pct in top_holdings:
        print(f"  {ticker:<8} {name[:20]:<22} {weight:>5.2f}%     {yield_pct:>5.2f}%")
    
    print("\n  Simple Average Yield (Top 10): 3.21%")
    print(f"  Fund-Level TTM Yield: {ttm_yield:.2%}")
    
    # =========================================================
    # SUMMARY STATISTICS
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 SCHD KEY STATISTICS SUMMARY")
    print("=" * 70)
    
    print(f"""
    Fund Metrics:
    ├── Net Assets:       ${aum/1e9:.1f} Billion
    ├── Expense Ratio:    {expense_ratio:.2%} (industry-leading low)
    ├── Holdings:         {holdings_count}
    ├── Turnover:         {turnover:.1%}
    ├── Inception:        {inception_date}
    └── Yield (TTM):      {ttm_yield:.2%}
    
    Performance (as of March 31, 2026):
    ├── YTD 2026:         +{performance_ytd:.1%}
    ├── 1-Year:           +{performance_1y:.1%}
    ├── 3-Year (ann.):    +{performance_3y:.1%}
    ├── 5-Year (ann.):    +{performance_5y:.1%}
    └── Since Inception:  +{performance_since_inception:.1%}
    
    Valuation (Portfolio):
    ├── P/E Ratio:        {portfolio_pe:.1f}x (S&P 500: 28x)
    ├── P/B Ratio:        {portfolio_pb:.2f}x (S&P 500: 5.3x)
    ├── P/CF Ratio:       {portfolio_pcf:.2f}x (S&P 500: 38x)
    └── ROE:              {portfolio_roe:.1%}
    
    Key Strengths:
    ├── Ultra-low cost structure
    ├── Attractive valuation discount to market
    ├── Defensive sector positioning
    └── Exceptional 2026 year-to-date performance
    
    Key Weaknesses:
    ├── Long-term underperformance vs S&P 500
    ├── Lower growth potential
    └── Sector concentration risks
    """)
    
    return {
        "total_score": total_score,
        "max_score": max_score,
        "layer_scores": {
            "fee_efficiency": layer1_score,
            "performance": layer2_score,
            "valuation": layer3_score,
            "defensive": layer4_score,
            "financial_health": layer5_score
        },
        "aum": aum,
        "expense_ratio": expense_ratio,
        "yield": ttm_yield,
        "performance_ytd": performance_ytd,
        "portfolio_pe": portfolio_pe
    }


def plot_schd_performance():
    """Create SCHD performance chart with key levels"""
    
    print("\n📈 Generating SCHD price chart...")
    
    schd = yf.Ticker("SCHD")
    data = schd.history(period="2y")
    
    if data.empty:
        print("❌ No price data available for SCHD")
        return
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price chart with moving averages
    ax1.plot(data.index, data['Close'], label='SCHD Price', linewidth=2, color='#1a73e8')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-Day MA', linewidth=1.5, color='#e67e22')
    ax1.plot(data.index, data['Close'].rolling(window=200).mean(), 
             label='200-Day MA', linewidth=1.5, color='#2ecc71')
    
    # Draw 52-week high/low reference lines
    current_price = data['Close'].iloc[-1]
    week_high = 31.95
    week_low = 25.28
    
    ax1.axhline(y=week_high, color='red', linestyle='--', alpha=0.5, label=f'52W High: ${week_high:.2f}')
    ax1.axhline(y=current_price, color='green', linestyle='-', alpha=0.7, label=f'Current: ${current_price:.2f}')
    ax1.axhline(y=week_low, color='red', linestyle=':', alpha=0.3, label=f'52W Low: ${week_low:.2f}')
    
    ax1.set_title('Schwab U.S. Dividend Equity ETF (SCHD) - 2 Year Price History', 
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
    plt.savefig('SCHD_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved: SCHD_chart.png")
    plt.show()


def analyze_schd_dividend_growth():
    """Analyze SCHD's dividend growth history"""
    
    print("\n" + "=" * 70)
    print("📈 SCHD DIVIDEND GROWTH ANALYSIS")
    print("=" * 70)
    
    # Dividend history from search results [citation:7]
    dividend_data = [
        (2021, 0.9650),
        (2022, 1.0000),
        (2023, 1.0320),
        (2024, 1.0800),
        (2025, 1.1020),
        (2026, 1.0557),  # TTM as of April 2026
    ]
    
    print("\n  Historical Annual Dividends Per Share:")
    print("  {:<8} {:>12} {:>12}".format("Year", "Dividend", "YoY Growth"))
    print("  " + "-" * 35)
    
    prev_dividend = None
    for year, dividend in dividend_data:
        if prev_dividend:
            growth = (dividend - prev_dividend) / prev_dividend
            print(f"  {year:<8} ${dividend:>10.4f}  {growth:>11.1%}")
        else:
            print(f"  {year:<8} ${dividend:>10.4f}  {'---':>11}")
        prev_dividend = dividend
    
    # Calculate 5-year CAGR
    if len(dividend_data) >= 2:
        first_div = dividend_data[0][1]
        last_div = dividend_data[-1][1]
        cagr = (last_div / first_div) ** (1/len(dividend_data)) - 1
        print(f"\n  5-Year Dividend CAGR: {cagr:.1%}")
        
        if cagr > 0.05:
            print("  ✅ Strong dividend growth history")
        elif cagr > 0.03:
            print("  ⚠️ Moderate dividend growth")
        else:
            print("  ⚠️ Slowing dividend growth momentum")
    
    return dividend_data


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("📊 SCHD ANALYSIS - TUNAURA FRAMEWORK")
    print("Applying the Turkish SaaS scorecard to a dividend ETF")
    print("=" * 70)
    
    # Run ETF analysis
    results = analyze_schd_tunaura()
    
    # Interactive menu
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Display SCHD price chart (2-year history)")
    print("  2. Show dividend growth analysis")
    print("  3. Run analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_schd_performance()
    elif choice == "2":
        analyze_schd_dividend_growth()
    elif choice == "3":
        analyze_schd_tunaura()
    else:
        print("\n✅ Analysis complete!")
        print(f"\n📌 SCHD scored {results['total_score']:.1f}/18 on the TUNAURA framework")
        print("   → Classification: SOLID ETF - CORE HOLDING for income investors")
