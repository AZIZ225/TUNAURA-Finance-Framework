"""
ISHARES BIOTECHNOLOGY ETF (IBB) - TUNAURA FRAMEWORK ANALYSIS
Applying the 5-layer scorecard to a large-cap market-cap-weighted biotech ETF
Data as of May 2026
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_ibb_tunaura():
    """
    IBB analysis using the TUNAURA 5-layer framework
    Layer 1: Profitability - Expense ratio, yield
    Layer 2: Growth - Performance, AUM growth
    Layer 3: Valuation - P/E, analyst upside
    Layer 4: Efficiency - Market-cap weighting, concentration risk
    Layer 5: Financial Health - AUM, institutional backing
    """
    
    print("=" * 70)
    print("🧬 ISHARES BIOTECHNOLOGY ETF (IBB)")
    print("TUNAURA FRAMEWORK ANALYSIS - Large-Cap Market-Cap-Weighted Biotech ETF")
    print("Data as of May 2026")
    print("=" * 70)
    
    # =========================================================
    # FUNDAMENTAL ETF DATA
    # =========================================================
    
    # ETF-level metrics from search results
    aum = 8.25e9  # $8.25 billion net assets 
    expense_ratio = 0.0044  # 0.44% expense ratio 
    holdings_count = 260  # 260 holdings 
    inception_date = "2001-02-05"  # February 5, 2001 inception 
    
    # Weighting methodology
    weighting = "Market-cap weighted"
    index_name = "ICE Biotechnology Index"
    
    # Performance metrics
    current_price = 168.40
    ytd_return = 0.0168
    one_year_return = 0.2620
    three_year_return = 0.0894
    five_year_return = 0.0869
    ten_year_return = 4.5122
    
    # Annual returns
    annual_returns = {
        2025: 0.280,
        2024: -0.024,
        2023: 0.036,
        2022: -0.136,
        2021: 0.010,
        2020: 0.259,
    }
    
    # Yield metrics
    dividend_yield = 0.0022
    thirty_day_yield = -0.0013
    
    # Risk metrics
    beta = 0.722
    volatility = 0.19
    max_drawdown_3y = -0.2485
    sharpe_ratio = 1.71
    alpha = 26.10
    
    # Valuation metrics
    pe_ratio = -372.51
    sector_pe = 24.36
    
    # Price metrics
    week_52_high = 179.64
    week_52_low = 116.25
    
    # Analyst data
    analyst_rating = "Strong Buy"
    analyst_upside = 0.2887
    analyst_target = 222.20
    
    # Top holdings concentration
    top10_weight = 0.5084
    
    # Flows data
    ytd_flows = -226e6
    one_year_flows = 667e6
    
    # AUM growth
    aum_prev = 7.4e9
    aum_growth = (aum - aum_prev) / aum_prev
    
    # Peer comparison to XBI
    xbi_ytd = 0.1025
    xbi_ttm = 0.6537
    xbi_10y = 1.3471
    xbi_expense = 0.0035
    
    # =========================================================
    # LAYER 1: PROFITABILITY & FEE EFFICIENCY
    # =========================================================
    print("\n" + "█" * 70)
    print("📊 LAYER 1: FEE EFFICIENCY & YIELD")
    print("█" * 70)
    
    print(f"  ETF Net Assets: ${aum/1e9:.2f} Billion")
    print(f"  Expense Ratio: {expense_ratio:.2%}")
    print(f"  Holdings Count: {holdings_count}")
    print(f"  Inception Date: {inception_date}")
    print(f"\n  Dividend Yield (TTM): {dividend_yield:.2%}")
    print(f"  30-Day SEC Yield: {thirty_day_yield:.2%}")
    
    # Score Layer 1
    layer1_score = 0
    
    if expense_ratio < 0.0040:
        layer1_score += 3
        print("\n  ✅ Expense Ratio <0.40% → LOW COST (+3)")
    elif expense_ratio < 0.0050:
        layer1_score += 2
        print("\n  ✅ Expense Ratio 0.40-0.50% → REASONABLE COST (+2)")
    else:
        print("\n  ⚠️ Expense Ratio >0.50% → MODERATE COST (+0)")
    
    print(f"\n  Fee Comparison to XBI:")
    print(f"    • IBB: {expense_ratio:.2%}")
    print(f"    • XBI: {xbi_expense:.2%}")
    print(f"    → IBB is {expense_ratio - xbi_expense:.2%} more expensive than XBI")
    
    if dividend_yield > 0.0050:
        layer1_score += 1
        print(f"\n  ✅ Dividend Yield >0.5% → MODERATE INCOME (+1)")
    elif dividend_yield > 0.0010:
        layer1_score += 0.5
        print(f"\n  ⚠️ Dividend Yield 0.10-0.50% → MINIMAL INCOME (+0.5)")
    else:
        print(f"\n  ❌ Dividend Yield <0.10% → NEGLIGIBLE INCOME (+0)")
    
    if one_year_flows > 500e6:
        layer1_score += 1.5
        print(f"\n  ✅ One-year inflows +${one_year_flows/1e6:.0f}M → STRONG DEMAND (+1.5)")
    elif one_year_flows > 0:
        layer1_score += 0.5
        print(f"\n  ⚠️ Positive but modest inflows → MODERATE DEMAND (+0.5)")
    else:
        print(f"\n  ❌ Negative flows → OUTFLOWS (+0)")
    
    print(f"\n  LAYER 1 SCORE: {layer1_score:.1f}/6")
    
    # =========================================================
    # LAYER 2: GROWTH & PERFORMANCE
    # =========================================================
    print("\n" + "█" * 70)
    print("📈 LAYER 2: PERFORMANCE & GROWTH")
    print("█" * 70)
    
    print(f"  Current Price: ${current_price:.2f}")
    print(f"  YTD 2026: {ytd_return:.1%}")
    print(f"  TTM: {one_year_return:.1%}")
    print(f"  3-Year Cumulative: {three_year_return:.1%}")
    print(f"  5-Year Cumulative: {five_year_return:.1%}")
    print(f"  10-Year Cumulative: {ten_year_return:.1%}")
    
    print(f"\n  Annual Returns History:")
    print(f"    2025: +{annual_returns[2025]:.1%}")
    print(f"    2024: {annual_returns[2024]:.1%}")
    print(f"    2023: +{annual_returns[2023]:.1%}")
    print(f"    2022: {annual_returns[2022]:.1%}")
    print(f"    2021: +{annual_returns[2021]:.1%}")
    print(f"    2020: +{annual_returns[2020]:.1%}")
    
    print(f"\n  vs XBI (Equal-Weight Biotech ETF):")
    print(f"    YTD:  IBB {ytd_return:.1%} vs XBI {xbi_ytd:.1%} → UNDERPERFORM by {xbi_ytd - ytd_return:.1%}")
    print(f"    TTM:  IBB {one_year_return:.1%} vs XBI {xbi_ttm:.1%} → UNDERPERFORM by {xbi_ttm - one_year_return:.1%}")
    print(f"    10Y:  IBB +{ten_year_return:.1%} vs XBI +{xbi_10y:.1%} → OUTPERFORM by {ten_year_return - xbi_10y:.1%}")
    
    layer2_score = 0
    
    if one_year_return > 0.30:
        layer2_score += 2
        print("\n  ✅ TTM Return >30% → STRONG RECENT PERFORMANCE (+2)")
    elif one_year_return > 0.20:
        layer2_score += 1
        print("\n  ⚠️ TTM Return 20-30% → MODERATE (+1)")
    else:
        print("\n  ❌ TTM Return <20% → WEAK (+0)")
    
    if ten_year_return > 4.0:
        layer2_score += 2
        print(f"  ✅ 10-Year Return +{ten_year_return:.0f}% → EXCELLENT LONG-TERM RECORD (+2)")
    elif ten_year_return > 2.0:
        layer2_score += 1
        print(f"  ⚠️ 10-Year Return +{ten_year_return:.0f}% → GOOD (+1)")
    else:
        print(f"  ❌ 10-Year Return <200% → MODERATE (+0)")
    
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
    print(f"    P/E Ratio: {pe_ratio:.2f}x (Negative due to pre-revenue biotech losses)")
    print(f"    Biotech Sector Forward P/E: {sector_pe:.2f}x")
    
    print(f"\n  Analyst Consensus: {analyst_rating}")
    print(f"  Analyst Price Target: ${analyst_target:.2f}")
    print(f"  Implied Upside: {analyst_upside:.1%}")
    
    layer3_score = 0
    
    if position_in_range < 0.30:
        layer3_score += 2
        print("\n  ✅ Trading near 52-week low → POTENTIAL BUYING OPPORTUNITY (+2)")
    elif position_in_range < 0.50:
        layer3_score += 1
        print("\n  ⚠️ Trading in lower half of range → REASONABLE ENTRY (+1)")
    else:
        print("\n  ⚠️ Trading near 52-week high → WAIT FOR PULLBACK (+0)")
    
    if analyst_upside > 0.25:
        layer3_score += 2
        print(f"  ✅ >25% Analyst Upside → SIGNIFICANT UPSIDE POTENTIAL (+2)")
    elif analyst_upside > 0.15:
        layer3_score += 1
        print(f"  ⚠️ 15-25% Analyst Upside → MODERATE UPSIDE (+1)")
    else:
        print(f"  ❌ <15% Upside → LIMITED UPSIDE (+0)")
    
    print(f"\n  LAYER 3 SCORE: {layer3_score:.1f}/4")
    
    # =========================================================
    # LAYER 4: STRUCTURAL EFFICIENCY & RISK
    # =========================================================
    print("\n" + "█" * 70)
    print("⚙️ LAYER 4: STRUCTURAL EFFICIENCY & RISK")
    print("█" * 70)
    
    print(f"  Index: {index_name}")
    print(f"  Weighting Methodology: {weighting}")
    print(f"  Number of Holdings: {holdings_count}")
    print(f"  Top 10 Holdings Weight: {top10_weight:.1%}")
    
    print(f"\n  Risk Metrics:")
    print(f"    Beta: {beta:.3f}")
    print(f"    Volatility: {volatility:.1%}")
    print(f"    Max Drawdown (3Y): {max_drawdown_3y:.1%}")
    print(f"    Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"    Alpha: {alpha:.1f}")
    
    xbi_volatility = 0.327
    xbi_beta = 0.88
    print(f"\n  Risk Comparison vs XBI:")
    print(f"    Volatility: IBB {volatility:.1%} vs XBI {xbi_volatility:.1%}")
    print(f"    Beta: IBB {beta:.3f} vs XBI {xbi_beta:.2f}")
    
    layer4_score = 0
    
    if top10_weight < 0.40:
        layer4_score += 1
        print("\n  ✅ Top 10 weight <40% → REASONABLE DIVERSIFICATION (+1)")
    elif top10_weight < 0.55:
        layer4_score += 0.5
        print("\n  ⚠️ Top 10 weight 40-55% → MODERATE CONCENTRATION (+0.5)")
    else:
        print("\n  ❌ Top 10 weight >55% → HIGH CONCENTRATION RISK (+0)")
    
    if sharpe_ratio > 1.5:
        layer4_score += 1
        print(f"  ✅ Sharpe Ratio {sharpe_ratio:.2f} → EXCELLENT RISK-ADJUSTED RETURNS (+1)")
    elif sharpe_ratio > 1.0:
        layer4_score += 0.5
        print(f"  ⚠️ Sharpe Ratio {sharpe_ratio:.2f} → GOOD (+0.5)")
    else:
        print(f"  ❌ Sharpe Ratio <1.0 → MODERATE (+0)")
    
    print(f"\n  LAYER 4 SCORE: {layer4_score:.1f}/2")
    
    # =========================================================
    # LAYER 5: FINANCIAL HEALTH
    # =========================================================
    print("\n" + "█" * 70)
    print("🏦 LAYER 5: FINANCIAL HEALTH")
    print("█" * 70)
    
    print(f"  AUM: ${aum/1e9:.2f} Billion")
    print(f"  Provider: iShares (BlackRock)")
    print(f"  Index Provider: ICE Data Indices")
    
    print(f"\n  Fund Flows:")
    print(f"    YTD: ${ytd_flows/1e6:.0f}M")
    print(f"    1-Year: +${one_year_flows/1e6:.0f}M")
    
    print(f"\n  Market Position:")
    print(f"    • Largest traditional biotech ETF alongside XBI")
    print(f"    • Tracks NYSE Biotechnology Index since 2001")
    
    layer5_score = 0
    
    if aum > 10e9:
        layer5_score += 1
        print("\n  ✅ AUM >$10B → MEGA-SCALE & HIGH LIQUIDITY (+1)")
    elif aum > 5e9:
        layer5_score += 0.5
        print("\n  ⚠️ AUM $5-10B → GOOD SCALE (+0.5)")
    else:
        print("\n  ❌ AUM <$5B → SMALL FUND (+0)")
    
    layer5_score += 1
    print("\n  ✅ BlackRock iShares → WORLD'S LARGEST ETF PROVIDER (+1)")
    
    print(f"\n  LAYER 5 SCORE: {layer5_score:.1f}/2")
    
    # =========================================================
    # FINAL SCORECARD
    # =========================================================
    print("\n" + "=" * 70)
    print("🎯 TUNAURA FRAMEWORK - FINAL SCORECARD")
    print("=" * 70)
    
    total_score = layer1_score + layer2_score + layer3_score + layer4_score + layer5_score
    max_score = 18
    
    print(f"\n  {'Layer':<20} {'Score':<10} {'Max':<10}")
    print("  " + "-" * 40)
    print(f"  {'1. Fee Efficiency':<20} {layer1_score:<10.1f} {6:<10}")
    print(f"  {'2. Performance':<20} {layer2_score:<10.1f} {4:<10}")
    print(f"  {'3. Valuation':<20} {layer3_score:<10.1f} {4:<10}")
    print(f"  {'4. Structure':<20} {layer4_score:<10.1f} {2:<10}")
    print(f"  {'5. Financial Health':<20} {layer5_score:<10.1f} {2:<10}")
    print("  " + "-" * 40)
    print(f"  {'TOTAL':<20} {total_score:<10.1f} {max_score:<10}")
    
    print("\n" + "-" * 50)
    print("  FINAL VERDICT:")
    
    if total_score >= 15:
        print("    ✅ VERY SOLID ETF INVESTMENT")
    elif total_score >= 12:
        print("    ✅ SOLID ETF - STRONG FUNDAMENTALS")
    elif total_score >= 9:
        print("    ⚠️ SOLID BUT HAS RISKS")
    elif total_score >= 6:
        print("    ⚠️ MODERATE - Understand trade-offs")
    else:
        print("    ❌ NOT SOLID - Better alternatives available")
    
    return {
        "total_score": total_score,
        "layer_scores": {
            "fee": layer1_score,
            "performance": layer2_score,
            "valuation": layer3_score,
            "structure": layer4_score,
            "health": layer5_score
        }
    }


def plot_ibb_chart():
    """Create IBB price chart"""
    print("\n📈 Generating IBB chart...")
    ibb = yf.Ticker("IBB")
    data = ibb.history(period="6mo")
    
    if data.empty:
        print("❌ No data available")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='IBB', linewidth=2)
    plt.title('iShares Biotechnology ETF (IBB) - 6 Month Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('IBB_chart.png', dpi=150)
    print("✅ Chart saved: IBB_chart.png")
    plt.show()


def compare_ibb_xbi():
    """Compare IBB vs XBI"""
    print("\n" + "=" * 70)
    print("🔬 IBB vs XBI COMPARISON")
    print("=" * 70)
    
    print("""
    Metric                    IBB              XBI              Winner
    -------------------------------------------------------------------
    Expense Ratio            0.44%            0.35%            XBI
    Top 10 Weight            50.8%            15.7%            XBI
    Volatility               19.0%            32.7%            IBB
    10Y Return               +451%            +135%            IBB
    TTM Return               +26.2%           +65.4%           XBI
    Analyst Upside           +28.9%           +55%             XBI
    
    VERDICT: 
    - IBB for stability and long-term track record
    - XBI for upside potential and recent momentum
    """)



# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n🧬 IBB ANALYSIS - TUNAURA FRAMEWORK")
    
    results = analyze_ibb_tunaura()
    
    print("\n📊 OPTIONS")
    print("  1. Display IBB price chart")
    print("  2. Compare IBB vs XBI")
    print("  3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        plot_ibb_chart()
    elif choice == "2":
        compare_ibb_xbi()
    else:
        print("\n✅ Analysis complete!")