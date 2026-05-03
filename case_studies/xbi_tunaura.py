"""
SPDR S&P BIOTECH ETF (XBI) - TUNAURA FRAMEWORK ANALYSIS
Applying the 5-layer scorecard to a passive equal-weight biotech ETF
Data as of May 2026
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_xbi_tunaura():
    """
    XBI analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability - Expense ratio, yield efficiency
    Layer 2: Growth - Performance, AUM growth, returns by period
    Layer 3: Valuation - P/E, P/B, analyst upside
    Layer 4: Efficiency - Equal-weight structure, diversification, volatility
    Layer 5: Financial Health - AUM, institutional backing, liquidity
    """
    
    print("=" * 70)
    print("🧬 SPDR S&P BIOTECH ETF (XBI)")
    print("TUNAURA FRAMEWORK ANALYSIS - Passive Equal-Weight Biotech ETF")
    print("Data as of May 2026")
    print("=" * 70)
    
    # =========================================================
    # FUNDAMENTAL ETF DATA
    # =========================================================
    
    # ETF-level metrics from search results
    aum = 8.75e9  # $8.75 billion net assets [citation:5]
    expense_ratio = 0.0035  # 0.35% expense ratio [citation:2][citation:5][citation:8]
    holdings_count = 153  # 153 holdings [citation:2][citation:10]
    inception_date = "2006-01-31"  # January 31, 2006 inception [citation:1][citation:2][citation:10]
    turnover = 0.43  # 43% turnover rate [citation:10]
    
    # Index methodology
    index_type = "S&P Biotechnology Select Industry Index"
    weighting = "Equal-weighted"  # Key differentiator [citation:4]
    
    # Performance metrics
    nav_price = 137.79  # $137.79 NAV price [citation:10]
    ytd_return = 0.1301  # +13.01% year-to-date total return [citation:7]
    ttm_return = 0.8315  # +83.15% trailing 12-month total return [citation:7]
    three_year_return = 0.7183  # +71.83% 3-year total return [citation:7]
    five_year_return = 0.0798  # +7.98% 5-year total return [citation:7]
    ten_year_return = 1.4817  # +148.17% 10-year total return [citation:7]
    twenty_year_return = 8.4877  # +848.77% 20-year total return [citation:7]
    
    # Annual returns by calendar year
    annual_returns = {
        2025: 0.3585,   # +35.85% [citation:10]
        2024: 0.0109,   # +1.09% [citation:10]
        2023: 0.0750,   # +7.50% [citation:10]
        2022: -0.2576,  # -25.76% [citation:10]
        2021: -0.2053,  # -20.53% [citation:10]
        2020: 0.4819,   # +48.19% [citation:10]
    }
    
    # Yield metrics
    dividend_yield = 0.0035  # 0.35% dividend yield TTM [citation:3]
    latest_dividend = 0.41  # $0.41 latest dividend [citation:1]
    
    # Risk metrics
    beta = 0.88  # 0.88 beta [citation:1]
    volatility = 0.1866  # 18.66% standard deviation [citation:1]
    max_drawdown = -0.6389  # -63.89% max drawdown since inception [citation:3][citation:6]
    
    # Volatility comparison vs ARKG
    # XBI volatility: 32.7% vs ARKG 39.3% over long term [citation:6]
    xbi_volatility_long = 0.327  # 32.7%
    arkg_volatility_long = 0.393  # 39.3%
    
    # Valuation metrics
    portfolio_pe = 18.21  # 18.21x P/E ratio [citation:1]
    portfolio_pb = 4.5  # 4.5x P/B ratio [citation:10]
    portfolio_roe = -0.13  # -13.0% Return on Equity (negative due to pre-revenue biotech) [citation:10]
    median_market_cap = 5.2e9  # $5.2 billion median market cap [citation:10]
    
    # Price metrics
    current_price = 138.67  # $138.67 [citation:1]
    week_52_high = 133.60  # $133.60 52-week high [citation:2]
    week_52_low = 73.94  # $73.94 52-week low [citation:2]
    
    # Analyst data
    analyst_rating = "Strong Buy"  # from TipRanks [citation:4]
    analyst_upside = 0.55  # ~55% implied upside [citation:4]
    analyst_count = 145  # across 145 underlying holdings [citation:4]
    
    # Top holdings concentration
    top10_weight = 0.157  # 15.70% top 10 holdings weight [citation:4]
    
    # =========================================================
    # LAYER 1: PROFITABILITY & FEE EFFICIENCY
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: FEE EFFICIENCY & YIELD")
    print("█" * 70)
    
    print(f"  ETF Net Assets: ${aum/1e9:.2f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Holdings Count: {holdings_count}")
    print(f"  Turnover: {turnover:.1%}")
    print(f"  Inception Date: {inception_date}")
    print(f"\n  Dividend Yield (TTM): {dividend_yield:.2%}")
    print(f"  Latest Dividend: ${latest_dividend:.2f}")
    
    # Score Layer 1 (max 6 points)
    layer1_score = 0
    
    # Expense ratio assessment (XBI is cheaper than ARKG's 0.75%)
    if expense_ratio < 0.0035:
        layer1_score += 3
        print("\n  ✅ Expense Ratio 0.35% → LOW COST FOR BIOTECH ETF (+3)")
    elif expense_ratio < 0.0050:
        layer1_score += 2
        print("\n  ✅ Expense Ratio <0.50% → REASONABLE COST (+2)")
    else:
        print("\n  ⚠️ Expense Ratio >0.50% → MODERATE COST (+0)")
    
    # Fee comparison to actively managed biotech ETFs
    print(f"\n  Fee Comparison:")
    print(f"    • XBI (passive): {expense_ratio:.2%}")
    print(f"    • ARKG (active): 0.75% → XBI is {0.75 - expense_ratio:.2%} cheaper")
    
    # Dividend yield assessment (small but consistent)
    if dividend_yield > 0.005:
        layer1_score += 1
        print(f"\n  ✅ Dividend Yield >0.5% → MODERATE INCOME (+1)")
    elif dividend_yield > 0.0025:
        layer1_score += 0.5
        print(f"\n  ⚠️ Dividend Yield 0.25-0.50% → MINIMAL INCOME (+0.5)")
    else:
        print(f"\n  ❌ Dividend Yield <0.25% → NEGLIGIBLE INCOME (+0)")
    
    # Turnover and tax efficiency
    if turnover < 0.50:
        layer1_score += 1
        print("\n  ✅ Turnover <50% → ACCEPTABLE TAX EFFICIENCY (+1)")
    else:
        print("\n  ⚠️ Turnover >50% → HIGHER TAX DRAG (+0)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score:.1f}/6")
    
    # =========================================================
    # LAYER 2: GROWTH & PERFORMANCE
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: PERFORMANCE & GROWTH")
    print("█" * 70)
    
    print(f"  YTD 2026: {ytd_return:.1%}")
    print(f"  TTM: {ttm_return:.1%}")
    print(f"  3-Year Cumulative: {three_year_return:.1%}")
    print(f"  5-Year Cumulative: {five_year_return:.1%}")
    print(f"  10-Year Cumulative: {ten_year_return:.1%}")
    print(f"  20-Year Cumulative: {twenty_year_return:.1%}")
    
    print(f"\n  Annual Returns History:")
    print(f"    2025: +{annual_returns[2025]:.1%}")
    print(f"    2024: +{annual_returns[2024]:.1%}")
    print(f"    2023: +{annual_returns[2023]:.1%}")
    print(f"    2022: {annual_returns[2022]:.1%}")
    print(f"    2021: {annual_returns[2021]:.1%}")
    print(f"    2020: +{annual_returns[2020]:.1%}")
    
    # Score Layer 2 (max 4 points)
    layer2_score = 0
    
    # TTM performance (exceptional 83% return)
    if ttm_return > 0.50:
        layer2_score += 2
        print("\n  ✅ TTM Return >50% → EXCEPTIONAL RECOVERY (+2)")
    elif ttm_return > 0.30:
        layer2_score += 1
        print("\n  ⚠️ TTM Return 30-50% → STRONG (+1)")
    else:
        print("\n  ❌ TTM Return <30% → WEAK (+0)")
    
    # Long-term track record (10-year returns)
    if ten_year_return > 1.0:
        layer2_score += 2
        print(f"  ✅ 10-Year Return +{ten_year_return:.1%} → STRONG LONG-TERM RECORD (+2)")
    elif ten_year_return > 0.50:
        layer2_score += 1
        print(f"  ⚠️ 10-Year Return +{ten_year_return:.1%} → MODERATE (+1)")
    else:
        print(f"  ❌ 10-Year Return <50% → WEAK (+0)")
    
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
    print(f"    P/E Ratio: {portfolio_pe:.2f}x")
    print(f"    P/B Ratio: {portfolio_pb:.2f}x")
    print(f"    ROE: {portfolio_roe:.1%} (negative due to pre-revenue biotech)")
    print(f"    Median Market Cap: ${median_market_cap/1e9:.1f} Billion")
    
    print(f"\n  Analyst Consensus: {analyst_rating}")
    print(f"  Analyst Count: {analyst_count} holdings covered")
    print(f"  Implied Upside: {analyst_upside:.1%}")
    
    # Score Layer 3 (max 4 points)
    layer3_score = 0
    
    # Position in 52-week range (buying opportunity?)
    if position_in_range < 0.30:
        layer3_score += 2
        print("\n  ✅ Trading near 52-week low → POTENTIAL BUYING OPPORTUNITY (+2)")
    elif position_in_range < 0.50:
        layer3_score += 1
        print("\n  ⚠️ Trading in lower half of range → REASONABLE ENTRY (+1)")
    else:
        print("\n  ⚠️ Trading near 52-week high → WAIT FOR PULLBACK (+0)")
    
    # Analyst upside potential
    if analyst_upside > 0.50:
        layer3_score += 2
        print(f"  ✅ >50% Analyst Upside → SIGNIFICANT UPSIDE POTENTIAL (+2)")
    elif analyst_upside > 0.30:
        layer3_score += 1
        print(f"  ⚠️ 30-50% Analyst Upside → MODERATE UPSIDE (+1)")
    else:
        print(f"  ❌ <30% Upside → LIMITED UPSIDE (+0)")
    
    # P/E context (biotech P/E can be misleading due to pre-revenue companies)
    print(f"\n  Valuation Context:")
    print(f"    • XBI P/E {portfolio_pe:.1f}x vs S&P 500 ~28x → Appears cheaper")
    print(f"    • However, many holdings are PRE-REVENUE (P/E distorted)")
    print(f"    • P/B {portfolio_pb:.2f}x more meaningful for biotech")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: EFFICIENCY & RISK MANAGEMENT
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: STRUCTURAL EFFICIENCY & RISK")
    print("█" * 70)
    
    print(f"  Index Type: {index_type}")
    print(f"  Weighting Methodology: {weighting}")
    print(f"  Number of Holdings: {holdings_count}")
    print(f"  Top 10 Holdings Weight: {top10_weight:.1%}")
    
    print(f"\n  Risk Metrics:")
    print(f"    Beta (market sensitivity): {beta:.2f}")
    print(f"    Standard Deviation: {volatility:.1%}")
    print(f"    Maximum Drawdown (since inception): {max_drawdown:.1%}")
    
    # Volatility comparison to ARKG
    print(f"\n  Volatility Comparison (long-term):")
    print(f"    • XBI: {xbi_volatility_long:.1%}")
    print(f"    • ARKG: {arkg_volatility_long:.1%}")
    print(f"    → XBI is {((arkg_volatility_long - xbi_volatility_long)/arkg_volatility_long*100):.0f}% LESS volatile than ARKG")
    
    # Score Layer 4 (max 2 points)
    layer4_score = 0
    
    # Equal-weight structure assessment
    if top10_weight < 0.20:
        layer4_score += 1
        print("\n  ✅ Top 10 weight <20% → EXCELLENT DIVERSIFICATION (+1)")
    elif top10_weight < 0.30:
        layer4_score += 0.5
        print("\n  ⚠️ Top 10 weight 20-30% → GOOD DIVERSIFICATION (+0.5)")
    else:
        print("\n  ❌ Top 10 weight >30% → CONCENTRATION RISK (+0)")
    
    # Risk-adjusted efficiency (lower volatility than peers)
    if xbi_volatility_long < 0.35:
        layer4_score += 1
        print(f"  ✅ Volatility {xbi_volatility_long:.1%} → LOWER THAN ACTIVE PEERS (+1)")
    else:
        print(f"  ⚠️ Volatility {xbi_volatility_long:.1%} → HIGH VOLATILITY (+0)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score:.1f}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    print(f"  Assets Under Management: ${aum/1e9:.2f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Provider: State Street Global Advisors (SPDR)")
    print(f"  Index Provider: S&P Dow Jones Indices")
    
    # AUM growth trends
    aum_prev = 7.4e9  # $7.4B as of March 2026 [citation:10]
    aum_growth = (aum - aum_prev) / aum_prev
    print(f"\n  AUM Growth (Mar→May 2026): {aum_growth:.1%}")
    
    # Institutional/retail appeal
    print(f"\n  Market Position:")
    print(f"    • Largest passive biotech ETF by AUM")
    print(f"    • Competes with IBB ({8.25e9/1e9:.2f}B) [citation:8]")
    print(f"    • Net inflows (TTM): ~$508M [citation:4]")
    
    # Score Layer 5 (max 2 points)
    layer5_score = 0
    
    # AUM assessment
    if aum > 10e9:
        layer5_score += 1
        print("\n  ✅ AUM >$10B → MEGA-SCALE & HIGH LIQUIDITY (+1)")
    elif aum > 5e9:
        layer5_score += 0.5
        print("\n  ⚠️ AUM $5-10B → GOOD SCALE & LIQUIDITY (+0.5)")
    else:
        print("\n  ❌ AUM <$5B → SMALL FUND (+0)")
    
    # Provider reputation
    layer5_score += 1
    print("\n  ✅ State Street Global Advisors → ESTABLISHED PROVIDER (+1)")
    
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
    print(f"  {'1. Fee Efficiency & Yield':<20} {layer1_score:<10.1f} {6:<10} {layer1_score/6*100:.0f}%")
    print(f"  {'2. Performance/Growth':<20} {layer2_score:<10.1f} {4:<10} {layer2_score/4*100:.0f}%")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10} {layer3_score/4*100:.0f}%")
    print(f"  {'4. Structural Efficiency':<20} {layer4_score:<10.1f} {2:<10} {layer4_score/2*100:.0f}%")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10.1f} {2:<10} {layer5_score/2*100:.0f}%")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10} {total_score/max_score*100:.0f}%")
    
    # Final verdict
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID ETF INVESTMENT")
        print("    → Exceptional structure, strong performance, reasonable fees")
        print("    → Suggested use: CORE BIOTECH HOLDING 5-10% of portfolio")
    elif total_score >= 12:
        print("    ✅ SOLID ETF - STRONG FUNDAMENTALS")
        print("    → Equal-weight diversification, strong recovery, analyst upside")
        print("    → Suggested use: CORE SATELLITE HOLDING 3-5% of portfolio")
    elif total_score >= 9:
        print("    ⚠️ SOLID BUT HAS RISKS")
        print("    → High volatility, cyclical biotech risks, negative ROE")
        print("    → Suggested use: TACTICAL HOLDING 2-3% of portfolio")
    elif total_score >= 6:
        print("    ⚠️ MODERATE - Understand trade-offs")
        print("    → Long-term returns good but high drawdown risk")
        print("    → Suggested use: SMALL ALLOCATION 1-2% of portfolio")
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
        ("PFEB (Buffer ETF)", 12, "📌 DEFINED-OUTCOME"),
        ("XBI (Biotech ETF)", total_score, "✅ SOLID ETF"),
        ("COGT (Biotech Stock)", 13, "⚠️ SPECULATIVE BUY"),
        ("SCHD (Dividend ETF)", 14.5, "✅ CORE HOLDING"),
        ("FSLR (Solar Stock)", 17, "✅ STRONG BUY"),
    ]
    
    print(f"\n  {'Company/ETF':<25} {'Score':<8} {'/18':<5} {'Verdict':<20}")
    print("  " + "-" * 60)
    for name, score, verdict in comparisons:
        print(f"  {name:<25} {score:<8} /18    {verdict:<20}")
    
    print("\n  XBI Key Differentiators:")
    print("    • Equal-weight structure → top 10 only 15.7% of assets")
    print("    • Expense ratio 0.35% → cheaper than active peers")
    print("    • TTM return +83.15% → exceptional recovery from 2022-2024 lows")
    print("    • Analyst upside ~55% → Strong Buy consensus across 145 holdings")
    print("    • Lower volatility than ARKG (32.7% vs 39.3% long-term)")
    
    # =========================================================
    # XBI-SPECIFIC NOTES
    # =========================================================
    print("\n" + "=" * 70)
    print("📌 XBI - KEY CHARACTERISTICS & USE CASE")
    print("=" * 70)
    print("""
    WHAT XBI IS:
    • Passively managed ETF tracking S&P Biotechnology Select Industry Index 
    • Equal-weighted structure → no single stock dominates
    • 150+ holdings across all biotech subsectors
    • Provides pure-play exposure to U.S. biotechnology sector
    
    WHAT XBI IS NOT:
    • NOT a genomics-focused ETF (unlike ARKG)
    • NOT a large-cap biotech ETF (unlike IBB)
    • NOT a low-volatility product (beta 0.88, but sector cyclical)
    
    WHY THE EQUAL-WEIGHT STRUCTURE MATTERS:
    • Prevents over-concentration in any single company
    • Captures upside from smaller, innovative biotechs
    • Reduces risk of a single FDA rejection crushing the fund
    • More representative of biotech innovation breadth
    
    WHEN TO USE XBI:
    • For broad biotech sector exposure without single-stock risk
    • When expecting biotech M&A activity or FDA approval cycle to accelerate
    • As a tactical rotation play from growth/tech into healthcare
    
    PERFORMANCE CYCLE PATTERN:
    • 2020: +48.19% (pandemic biotech boom)
    • 2021: -20.53% (post-peak correction)
    • 2022: -25.76% (bear market)
    • 2023: +7.50% (stabilization)
    • 2024: +1.09% (consolidation)
    • 2025: +35.85% (recovery begins)
    • 2026 YTD: +13.01% (momentum continues)
    
    RISK FACTORS:
    • High volatility: Maximum drawdown -63.89% from 2021 peak
    • Pre-revenue holdings: Many companies have no earnings
    • FDA dependency: Negative trial results can crush individual holdings
    • Interest rate sensitivity: Biotech valuations are rate-sensitive
    """)
    
    # =========================================================
    # SUMMARY STATISTICS
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 XBI KEY STATISTICS SUMMARY")
    print("=" * 70)
    
    print(f"""
    Fund Metrics:
    ├── Net Assets:       ${aum/1e9:.2f} Billion
    ├── Expense Ratio:    {expense_ratio:.2%}
    ├── Holdings:         {holdings_count}
    ├── Turnover:         {turnover:.1%}
    ├── Inception:        {inception_date}
    ├── Weighting:        {weighting}
    └── Dividend Yield:   {dividend_yield:.2%}
    
    Performance (as of Apr 2026):
    ├── YTD 2026:         +{ytd_return:.1%}
    ├── TTM:              +{ttm_return:.1%}
    ├── 3-Year (cum):     +{three_year_return:.1%}
    ├── 5-Year (cum):     +{five_year_return:.1%}
    ├── 10-Year (cum):    +{ten_year_return:.1%}
    └── 20-Year (cum):    +{twenty_year_return:.1%}
    
    Valuation (Portfolio):
    ├── P/E Ratio:        {portfolio_pe:.2f}x
    ├── P/B Ratio:        {portfolio_pb:.2f}x
    ├── ROE:              {portfolio_roe:.1%}
    └── Median Mkt Cap:   ${median_market_cap/1e9:.1f}B
    
    Risk Metrics:
    ├── Beta:             {beta:.2f}
    ├── Std Deviation:    {volatility:.1%}
    └── Max Drawdown:     {max_drawdown:.1%}
    
    Analyst Outlook:
    ├── Rating:           {analyst_rating}
    ├── Holdings Covered: {analyst_count}
    └── Implied Upside:   {analyst_upside:.1%}
    
    Key Strengths:
    ├── Equal-weight diversification (top 10 only 15.7%)
    ├── Low expense ratio for biotech sector
    ├── Exceptional TTM recovery (+83%)
    └── Strong analyst upside consensus
    
    Key Weaknesses:
    ├── High volatility and deep drawdowns
    ├── Negative portfolio ROE (many pre-revenue)
    └── Cyclical sector performance pattern
    """)
    
    return {
        "total_score": total_score,
        "max_score": max_score,
        "layer_scores": {
            "fee_efficiency": layer1_score,
            "performance": layer2_score,
            "valuation": layer3_score,
            "structural": layer4_score,
            "financial_health": layer5_score
        },
        "aum": aum,
        "expense_ratio": expense_ratio,
        "ytd_return": ytd_return,
        "ttm_return": ttm_return,
        "beta": beta,
        "max_drawdown": max_drawdown,
        "analyst_upside": analyst_upside
    }


def plot_xbi_performance():
    """Create XBI performance chart with key levels"""
    
    print("\n📈 Generating XBI price chart...")
    
    xbi = yf.Ticker("XBI")
    data = xbi.history(period="2y")
    
    if data.empty:
        print("❌ No price data available for XBI")
        return
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Price chart with moving averages
    ax1.plot(data.index, data['Close'], label='XBI Price', linewidth=2, color='#1a73e8')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-Day MA', linewidth=1.5, color='#e67e22')
    ax1.plot(data.index, data['Close'].rolling(window=200).mean(), 
             label='200-Day MA', linewidth=1.5, color='#2ecc71')
    
    # Draw 52-week high/low reference lines
    current_price = data['Close'].iloc[-1]
    week_high = 133.60
    week_low = 73.94
    
    ax1.axhline(y=week_high, color='red', linestyle='--', alpha=0.5, label=f'52W High: ${week_high:.2f}')
    ax1.axhline(y=current_price, color='green', linestyle='-', alpha=0.7, label=f'Current: ${current_price:.2f}')
    ax1.axhline(y=week_low, color='red', linestyle=':', alpha=0.3, label=f'52W Low: ${week_low:.2f}')
    
    ax1.set_title('SPDR S&P Biotech ETF (XBI) - 2 Year Price History', 
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
    plt.savefig('XBI_chart.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved: XBI_chart.png")
    plt.show()


def compare_xbi_vs_arkg():
    """Compare XBI with ARKG using TUNAURA framework metrics"""
    
    print("\n" + "=" * 70)
    print("🔬 XBI vs ARKG - TUNAURA FRAMEWORK COMPARISON")
    print("=" * 70)
    
    print("""
    {:<20} {:>15} {:>15} {:>15}
    """.format("Metric", "XBI", "ARKG", "Winner"))
    print("  " + "-" * 65)
    
    comparisons_data = [
        ("Expense Ratio", "0.35%", "0.75%", "XBI"),
        ("AUM", "$8.75B", "$1.16B", "XBI"),
        ("Holdings", "153", "32", "XBI"),
        ("Top 10 Weight", "15.7%", "~40%", "XBI"),
        ("1Y Return", "+83.15%", "+14.08%", "XBI"),
        ("3Y Return (cum)", "+71.83%", "+26.74%", "XBI"),
        ("5Y Return (cum)", "+7.98%", "-4.61%", "XBI"),
        ("10Y Return (cum)", "+148.17%", "+7.39%", "XBI"),
        ("Volatility (long-term)", "32.7%", "39.3%", "XBI"),
        ("Max Drawdown", "-63.9%", "-83.6%", "XBI"),
        ("Dividend Yield", "0.35%", "0.00%", "XBI"),
        ("Management", "Passive", "Active", "Depends"),
    ]
    
    for metric, xbi_val, arkg_val, winner in comparisons_data:
        print(f"  {metric:<20} {xbi_val:>15} {arkg_val:>15} {winner:>15}")
    
    print("\n" + "-" * 65)
    print("""
    VERDICT: XBI wins on MOST metrics for broad biotech exposure
    
    XBI Advantages:
    • Much lower fees (0.35% vs 0.75%)
    • Better diversification (153 vs 32 holdings)
    • Equal-weight reduces single-stock risk
    • Stronger long-term track record
    • Less severe drawdowns
    
    ARKG Advantages:
    • Active management (potential for outsized returns)
    • Focus on genomics/thematic innovation
    • Cathie Wood's ARK brand / hype factor
    
    When to choose XBI:
    → Broad biotech sector exposure without stock-picking risk
    → Lower-cost, more diversified option
    → Evidence-based investing approach
    
    When to choose ARKG:
    → Strong conviction in genomics/CRISPR theme
    → Willing to accept higher volatility and fees
    → Believe in active management edge
    """)
    
    print("  " + "-" * 65)
    print("  Recommendation: XBI as CORE, ARKG as SATELLITE (if any)")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🧬 XBI ANALYSIS - TUNAURA FRAMEWORK")
    print("Applying the Turkish SaaS scorecard to a biotech ETF")
    print("=" * 70)
    
    # Run ETF analysis
    results = analyze_xbi_tunaura()
    
    # Interactive menu
    print("\n" + "=" * 70)
    print("📊 OPTIONS")
    print("=" * 70)
    print("  1. Display XBI price chart (2-year history)")
    print("  2. Compare XBI vs ARKG side-by-side")
    print("  3. Run analysis again")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        plot_xbi_performance()
    elif choice == "2":
        compare_xbi_vs_arkg()
    elif choice == "3":
        analyze_xbi_tunaura()
    else:
        print("\n✅ Analysis complete!")
        print(f"\n📌 XBI scored {results['total_score']:.1f}/18 on the TUNAURA framework")
        print("   → Classification: SOLID ETF - CORE BIOTECH HOLDING")
