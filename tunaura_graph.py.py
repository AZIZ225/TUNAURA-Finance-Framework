"""
TUNAURA STYLE BUSINESS ANALYZER WITH GRAPHS
Complete analysis tool with visual charts for SaaS and tech companies
Based on our Turkish cloud-backup analysis framework
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Set up nice looking charts
plt.style.use('seaborn-v0_8-darkgrid')

def analyze_company(ticker):
    """Complete business analysis with graphs"""
    
    print("=" * 70)
    print(f"📊 ANALYZING: {ticker.upper()}")
    print("=" * 70)
    
    # Fetch data
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # ===== PROFITABILITY LAYER =====
    print("\n💰 PROFITABILITY")
    print("-" * 50)
    
    gross_margin = info.get('grossMargins', 0)
    net_margin = info.get('profitMargins', 0)
    op_margin = info.get('operatingMargins', 0)
    
    if gross_margin:
        print(f"  Gross Margin:     {gross_margin:.1%}")
        if gross_margin > 0.50:
            print("    ✅ Excellent (>50%)")
        elif gross_margin > 0.35:
            print("    ⚠️ Acceptable (35-50%)")
        else:
            print("    ❌ Poor (<35%)")
    
    if net_margin:
        print(f"  Net Margin:       {net_margin:.1%}")
        if net_margin > 0.15:
            print("    ✅ Excellent (>15%)")
        elif net_margin > 0.05:
            print("    ⚠️ Acceptable (5-15%)")
        else:
            print("    ❌ Poor (<5%)")
    
    # ===== GROWTH LAYER =====
    print("\n📈 GROWTH")
    print("-" * 50)
    
    revenue_growth = info.get('revenueGrowth', 0)
    earnings_growth = info.get('earningsGrowth', 0)
    
    if revenue_growth:
        print(f"  Revenue Growth:   {revenue_growth:.1%}")
        if revenue_growth > 0.20:
            print("    ✅ Excellent (>20%)")
        elif revenue_growth > 0.10:
            print("    ⚠️ Acceptable (10-20%)")
        else:
            print("    ❌ Poor (<10%)")
    
    # ===== VALUATION (Payback Period) =====
    print("\n💰 VALUATION")
    print("-" * 50)
    
    pe = info.get('trailingPE', 0)
    ps = info.get('priceToSalesTrailing12Months', 0)
    
    if pe:
        print(f"  P/E Ratio:        {pe:.1f}x")
        if pe < 20:
            print("    ✅ Good payback (<20 years)")
        elif pe < 30:
            print("    ⚠️ Fair payback (20-30 years)")
        else:
            print("    ❌ Long payback (>30 years)")
    
    # ===== EFFICIENCY (Like our employee analysis) =====
    print("\n⚙️ EFFICIENCY")
    print("-" * 50)
    
    revenue = info.get('totalRevenue', 0)
    employees = info.get('fullTimeEmployees', 0)
    
    if revenue and employees and employees > 0:
        revenue_per_employee = revenue / employees
        print(f"  Revenue per Employee: ${revenue_per_employee:,.0f}")
        if revenue_per_employee > 500000:
            print("    ✅ Excellent (like efficient SaaS)")
        elif revenue_per_employee > 200000:
            print("    ⚠️ Acceptable")
        else:
            print("    ❌ Low — like our TUNAURA red flag!")
    
    # ===== FINANCIAL HEALTH =====
    print("\n🏦 FINANCIAL HEALTH")
    print("-" * 50)
    
    debt_to_equity = info.get('debtToEquity', 0)
    current_ratio = info.get('currentRatio', 0)
    
    if debt_to_equity:
        print(f"  Debt to Equity:   {debt_to_equity:.2f}")
        if debt_to_equity < 0.5:
            print("    ✅ Low debt (<0.5)")
        elif debt_to_equity < 1.0:
            print("    ⚠️ Moderate (0.5-1.0)")
        else:
            print("    ❌ High debt (>1.0)")
    
    # ===== FINAL SCORECARD =====
    print("\n" + "=" * 70)
    print("🎯 FINAL VERDICT")
    print("=" * 70)
    
    # Calculate simple score
    score = 0
    if gross_margin and gross_margin > 0.50:
        score += 2
    if net_margin and net_margin > 0.15:
        score += 2
    if revenue_growth and revenue_growth > 0.20:
        score += 2
    if revenue_growth and revenue_growth > 0.10:
        score += 1
    if pe and pe < 25:
        score += 1
    
    print(f"  Score: {score}/8")
    
    if score >= 6:
        print("\n  ✅ SOLID BUSINESS — Like our target analysis")
        print("  → Consider buying on dips")
    elif score >= 4:
        print("\n  ⚠️ SOLID BUT HAS RISKS — Like TUNAURA with employee concerns")
        print("  → Wait for better price or verify metrics")
    else:
        print("\n  ❌ WEAK BUSINESS")
        print("  → Avoid or only speculative")
    
    return score

def plot_stock(ticker, period="6mo"):
    """Create a professional stock chart"""
    
    print(f"\n📈 Generating chart for {ticker.upper()}...")
    
    # Download historical data
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    if data.empty:
        print(f"❌ No data available for {ticker}")
        return
    
    # Create a figure with multiple subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Plot 1: Price and moving averages
    ax1.plot(data.index, data['Close'], label='Close Price', linewidth=2, color='#2E86AB')
    ax1.plot(data.index, data['Close'].rolling(window=20).mean(), 
             label='20-day MA', linewidth=1.5, color='#A23B72')
    ax1.plot(data.index, data['Close'].rolling(window=50).mean(), 
             label='50-day MA', linewidth=1.5, color='#F18F01')
    
    ax1.fill_between(data.index, data['Close'].min(), data['Close'].max(), 
                      alpha=0.1, color='#2E86AB')
    ax1.set_title(f'{ticker.upper()} - Stock Price with Moving Averages', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price (USD)', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Trading volume
    colors = ['#73AB84' if data['Close'].iloc[i] >= data['Close'].iloc[i-1] 
              else '#A23B72' for i in range(len(data))]
    ax2.bar(data.index, data['Volume'], color=colors, alpha=0.7)
    ax2.set_title('Trading Volume', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the chart as an image
    filename = f"{ticker}_chart.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"✅ Chart saved as: {filename}")
    
    # Display the chart
    plt.show()
    
    return data

def plot_margin_comparison(tickers):
    """Compare profit margins across multiple companies"""
    
    print("\n📊 Generating margin comparison chart...")
    
    companies = []
    gross_margins = []
    net_margins = []
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        companies.append(info.get('longName', ticker)[:15])  # Truncate long names
        
        gross = info.get('grossMargins', 0)
        net = info.get('profitMargins', 0)
        gross_margins.append(gross * 100 if gross else 0)
        net_margins.append(net * 100 if net else 0)
    
    # Create bar chart
    x = range(len(companies))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar([i - width/2 for i in x], gross_margins, width, label='Gross Margin', color='#2E86AB')
    bars2 = ax.bar([i + width/2 for i in x], net_margins, width, label='Net Margin', color='#A23B72')
    
    ax.set_ylabel('Margin (%)', fontsize=12)
    ax.set_title('Profit Margin Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(companies, rotation=45, ha='right')
    ax.legend()
    ax.axhline(y=20, color='green', linestyle='--', alpha=0.5, label='20% Target')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height:.0f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height:.0f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('margin_comparison.png', dpi=150, bbox_inches='tight')
    print("✅ Chart saved as: margin_comparison.png")
    plt.show()

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🔬 TUNAURA STYLE BUSINESS ANALYZER WITH GRAPHS")
    print("Based on the Turkish Cloud-Backup SaaS Analysis")
    print("=" * 70)
    
    # Analyze example companies
    examples = ["CRM", "MSFT", "NET"]
    
    for ticker in examples:
        analyze_company(ticker)
        print("\n" + "~" * 70)
    
    # Ask user what they want to do
    print("\n📊 What would you like to do?")
    print("  1. Plot stock chart for a company")
    print("  2. Compare margins across companies")
    print("  3. Run full analysis with chart for a new ticker")
    print("  4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        ticker = input("Enter ticker symbol (e.g., CRM, NVDA, AAPL): ").upper()
        period = input("Enter period (1mo, 3mo, 6mo, 1y, 2y, 5y) [default: 6mo]: ").strip() or "6mo"
        plot_stock(ticker, period)
        
    elif choice == "2":
        tickers_input = input("Enter tickers separated by commas (e.g., CRM,MSFT,NVDA): ").upper()
        tickers_list = [t.strip() for t in tickers_input.split(",")]
        plot_margin_comparison(tickers_list)
        
    elif choice == "3":
        ticker = input("Enter ticker symbol: ").upper()
        analyze_company(ticker)
        plot_stock(ticker, "1y")
        
    else:
        print("✅ Analysis complete!")