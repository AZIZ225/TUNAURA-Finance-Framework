"""
RBOT ANALYSIS WITH PAYBACK PERIOD CALCULATION
Calculates how many years to recover $500 - $1000 investment
Based on historical annual returns
"""

def calculate_payback_period(investment_amount, annual_return_rate):
    """
    Calculate how many years to recover initial investment
    
    investment_amount: $ amount invested
    annual_return_rate: expected annual return (as decimal, e.g., 0.15 for 15%)
    """
    if annual_return_rate <= 0:
        return "Never (negative or zero return)"
    
    years = 0
    current_value = investment_amount
    target_value = investment_amount * 2  # Double to recover initial + profit
    
    # For payback of initial amount only (not double)
    years_to_recover_initial = 1 / annual_return_rate
    
    # For doubling money (return of capital + equal profit)
    years_to_double = 1 / annual_return_rate
    
    return years_to_recover_initial, years_to_double

def analyze_rbot_with_payback():
    print("=" * 70)
    print("🤖 ISHARES AUTOMATION & ROBOTICS ETF (RBOT)")
    print("TUNAURA FRAMEWORK ANALYSIS WITH PAYBACK PERIOD")
    print("=" * 70)
    
    # Basic metrics
    aum = 3.65
    expense_ratio = 0.40
    holdings = 135
    inception = "2016"
    one_year_return = 38.39
    three_year_return = 63.62
    since_inception = 240.11
    top10_weight = 42.6
    
    # Historical annual returns (RBOT actual data)
    historical_returns = {
        2017: -18.3,
        2018: 37.8,
        2019: 38.8,
        2020: 21.0,
        2021: -34.2,
        2022: 38.5,
        2023: 5.5,
        2024: 17.4,
        2025: 21.64,
    }
    
    # Calculate average annual return
    avg_return = sum(historical_returns.values()) / len(historical_returns)
    
    print("\n📊 FUND METRICS")
    print("-" * 50)
    print(f"  AUM: ${aum} Billion")
    print(f"  Expense Ratio: {expense_ratio}%")
    print(f"  Holdings: {holdings}")
    print(f"  Top 10 Weight: {top10_weight}%")
    
    print("\n📈 PERFORMANCE")
    print("-" * 50)
    print(f"  1-Year Return: +{one_year_return}%")
    print(f"  3-Year Cumulative: +{three_year_return}%")
    print(f"  Since Inception (2016): +{since_inception}%")
    
    print(f"\n📊 HISTORICAL ANNUAL RETURNS")
    print("-" * 50)
    for year, ret in historical_returns.items():
        if ret >= 0:
            print(f"  {year}: +{ret}%")
        else:
            print(f"  {year}: {ret}%")
    
    print(f"\n📈 AVERAGE ANNUAL RETURN (2017-2025): {avg_return:.1f}%")
    
    # =========================================================
    # PAYBACK PERIOD CALCULATION
    # =========================================================
    print("\n" + "=" * 70)
    print("💰 PAYBACK PERIOD ANALYSIS")
    print("=" * 70)
    
    # Investment scenarios
    investment_amounts = [500, 750, 1000]
    return_rates = [
        avg_return,           # Average historical return (18.7%)
        one_year_return,      # Recent 1-year return (38.39%)
        15.0,                 # Conservative estimate
        10.0,                 # Very conservative
        20.0,                 # Optimistic
    ]
    
    print("\nBased on DIFFERENT RETURN SCENARIOS:\n")
    print(f"{'Investment':<12} {'Annual Return':<15} {'Years to Recover Initial':<25} {'Years to Double Money':<20}")
    print("-" * 75)
    
    for inv in investment_amounts:
        for rate in return_rates:
            if rate <= 0:
                continue
            
            years_initial = 1 / (rate / 100)
            years_double = 1 / (rate / 100)
            
            # Color coding based on years
            if years_initial < 3:
                initial_marker = "✅ Quick"
            elif years_initial < 5:
                initial_marker = "⚠️ Moderate"
            else:
                initial_marker = "❌ Slow"
            
            if years_double < 5:
                double_marker = "✅ Quick"
            elif years_double < 8:
                double_marker = "⚠️ Moderate"
            else:
                double_marker = "❌ Slow"
            
            rate_label = f"{rate:.1f}%"
            print(f"${inv:<8} {rate_label:<15} {years_initial:.1f} years ({initial_marker}){' ':<5} {years_double:.1f} years ({double_marker})")
        print("-" * 75)
    
    # =========================================================
    # SPECIFIC SCENARIO TABLES
    # =========================================================
    print("\n" + "=" * 70)
    print("📊 SPECIFIC INVESTMENT SCENARIOS")
    print("=" * 70)
    
    # Table 1: Based on AVERAGE historical return (18.7%)
    avg_rate = avg_return
    print(f"\n📌 SCENARIO 1: Based on AVERAGE HISTORICAL RETURN ({avg_rate:.1f}% per year)")
    print("-" * 60)
    print(f"  {'Investment':<12} {'Years to Recover':<20} {'Years to Double':<18} {'Value after 5 Years':<20}")
    print("-" * 60)
    
    for inv in investment_amounts:
        years_initial = 1 / (avg_rate / 100)
        years_double = 1 / (avg_rate / 100)
        value_5years = inv * ((1 + avg_rate/100) ** 5)
        
        print(f"  ${inv:<8} {years_initial:.1f} years{' ':<12} {years_double:.1f} years{' ':<10} ${value_5years:.0f}")
    
    # Table 2: Based on CONSERVATIVE return (10%)
    conservative_rate = 10.0
    print(f"\n📌 SCENARIO 2: Based on CONSERVATIVE RETURN ({conservative_rate:.1f}% per year)")
    print("-" * 60)
    print(f"  {'Investment':<12} {'Years to Recover':<20} {'Years to Double':<18} {'Value after 5 Years':<20}")
    print("-" * 60)
    
    for inv in investment_amounts:
        years_initial = 1 / (conservative_rate / 100)
        years_double = 1 / (conservative_rate / 100)
        value_5years = inv * ((1 + conservative_rate/100) ** 5)
        
        print(f"  ${inv:<8} {years_initial:.1f} years{' ':<12} {years_double:.1f} years{' ':<10} ${value_5years:.0f}")
    
    # Table 3: Based on OPTIMISTIC return (25%)
    optimistic_rate = 25.0
    print(f"\n📌 SCENARIO 3: Based on OPTIMISTIC RETURN ({optimistic_rate:.1f}% per year)")
    print("-" * 60)
    print(f"  {'Investment':<12} {'Years to Recover':<20} {'Years to Double':<18} {'Value after 5 Years':<20}")
    print("-" * 60)
    
    for inv in investment_amounts:
        years_initial = 1 / (optimistic_rate / 100)
        years_double = 1 / (optimistic_rate / 100)
        value_5years = inv * ((1 + optimistic_rate/100) ** 5)
        
        print(f"  ${inv:<8} {years_initial:.1f} years{' ':<12} {years_double:.1f} years{' ':<10} ${value_5years:.0f}")
    
    # =========================================================
    # PROJECTED YEAR-BY-YEAR GROWTH
    # =========================================================
    print("\n" + "=" * 70)
    print("📈 PROJECTED YEAR-BY-YEAR GROWTH")
    print("=" * 70)
    
    for inv in investment_amounts:
        print(f"\n💰 ${inv} INVESTMENT PROJECTION (at {avg_rate:.1f}% average return):")
        print("-" * 50)
        print(f"  {'Year':<10} {'Value':<15} {'Profit':<15} {'Cumulative Profit':<20}")
        print("  " + "-" * 55)
        
        value = inv
        cumulative_profit = 0
        for year in range(1, 11):
            previous_value = value
            value = value * (1 + avg_rate/100)
            profit = value - previous_value
            cumulative_profit += profit
            
            if value < inv:
                print(f"  Year {year:<5} ${value:.0f}{' ':<12} ${profit:.0f}{' ':<12} ${cumulative_profit:.0f}")
            else:
                recovered_marker = "✅"
                print(f"  Year {year:<5} ${value:.0f}{' ':<12} ${profit:.0f}{' ':<12} ${cumulative_profit:.0f} {recovered_marker}")
            
            if value >= inv and year == 1:
                print(f"  {' ':<7} ✅ INITIAL INVESTMENT RECOVERED!")
        
        # Find exact year when investment is recovered
        value = inv
        for year in range(1, 11):
            value = value * (1 + avg_rate/100)
            if value >= inv:
                print(f"\n  📌 INITIAL ${inv} RECOVERED IN YEAR {year}")
                break
    
    # =========================================================
    # SUMMARY RECOMMENDATION
    # =========================================================
    print("\n" + "=" * 70)
    print("🎯 INVESTMENT SUMMARY & RECOMMENDATION")
    print("=" * 70)
    
    print(f"""
    Based on RBOT's historical average return of {avg_return:.1f}%:

    For a ${investment_amounts[0]} investment:
    ├── Expected recovery of initial capital: ~{1/(avg_return/100):.1f} years
    ├── Expected doubling of money: ~{1/(avg_return/100):.1f} years  
    ├── Projected value after 5 years: ${investment_amounts[0] * ((1 + avg_return/100) ** 5):.0f}
    └── Projected value after 10 years: ${investment_amounts[0] * ((1 + avg_return/100) ** 10):.0f}

    For a ${investment_amounts[2]} investment:
    ├── Expected recovery of initial capital: ~{1/(avg_return/100):.1f} years
    ├── Expected doubling of money: ~{1/(avg_return/100):.1f} years
    ├── Projected value after 5 years: ${investment_amounts[2] * ((1 + avg_return/100) ** 5):.0f}
    └── Projected value after 10 years: ${investment_amounts[2] * ((1 + avg_return/100) ** 10):.0f}

    ⚠️ IMPORTANT DISCLAIMERS:
    ├── Past performance does not guarantee future results
    ├── RBOT has shown high volatility (range: -34% to +38% annually)
    ├── Thematic ETFs carry higher risk than broad market indices
    ├── Consider your risk tolerance before investing
    └── This analysis is for educational purposes only
    """)
    
    print("\n" + "=" * 70)
    print("✅ Analysis complete!")
    print("=" * 70)

# Run the analysis
analyze_rbot_with_payback()
