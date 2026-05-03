"""
Stock Analyzer for TUNAURA Framework
Quick analysis of any public company
"""

import yfinance as yf

def analyze_stock(ticker):
    """Quick fundamental analysis of a stock"""
    
    stock = yf.Ticker(ticker)
    info = stock.info
    
    print("=" * 60)
    print(f"📊 {ticker.upper()} - QUICK ANALYSIS")
    print("=" * 60)
    
    # Get key metrics
    name = info.get('longName', 'N/A')
    sector = info.get('sector', 'N/A')
    market_cap = info.get('marketCap', 0)
    pe = info.get('trailingPE', 0)
    gross_margin = info.get('grossMargins', 0)
    profit_margin = info.get('profitMargins', 0)
    revenue_growth = info.get('revenueGrowth', 0)
    debt_to_equity = info.get('debtToEquity', 0)
    current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
    
    print(f"\n📌 {name}")
    print(f"   Sector: {sector}")
    print(f"   Market Cap: ${market_cap/1e9:.2f} Billion")
    print(f"   Current Price: ${current_price:.2f}")
    
    print(f"\n📈 PROFITABILITY")
    print(f"   Gross Margin: {gross_margin:.1%}" if gross_margin else "   Gross Margin: N/A")
    print(f"   Profit Margin: {profit_margin:.1%}" if profit_margin else "   Profit Margin: N/A")
    
    print(f"\n📈 GROWTH")
    print(f"   Revenue Growth: {revenue_growth:.1%}" if revenue_growth else "   Revenue Growth: N/A")
    
    print(f"\n💰 VALUATION")
    print(f"   P/E Ratio: {pe:.1f}x" if pe else "   P/E Ratio: N/A (company may be unprofitable)")
    
    print(f"\n🏦 FINANCIAL HEALTH")
    print(f"   Debt/Equity: {debt_to_equity:.2f}" if debt_to_equity else "   Debt/Equity: N/A")
    
    print("\n" + "=" * 60)
    
    # Simple verdict
    score = 0
    if gross_margin and gross_margin > 0.40:
        score += 1
    if profit_margin and profit_margin > 0.15:
        score += 1
    if revenue_growth and revenue_growth > 0.15:
        score += 1
    if pe and pe < 25:
        score += 1
    
    if score >= 3:
        print("\n✅ VERDICT: SOLID BUSINESS")
    elif score >= 2:
        print("\n⚠️ VERDICT: ACCEPTABLE - CHECK FURTHER")
    else:
        print("\n❌ VERDICT: WEAK - AVOID")
    
    return score

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., FSLR, MSFT, COGT): ").upper()
    analyze_stock(ticker)
