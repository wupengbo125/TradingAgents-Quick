import argparse
import datetime
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

def main():
    parser = argparse.ArgumentParser(description="Run Trading Agents Analysis non-interactively.")
    parser.add_argument(
        "ticker",
        type=str,
        nargs="?",
        default="SPY",
        help="Ticker symbol (default: SPY)"
    )
    parser.add_argument(
        "-d", "--date",
        type=str,
        default=datetime.datetime.now().strftime("%Y-%m-%d"),
        help="Analysis date in YYYY-MM-DD format (default: today)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output of intermediate step details (default: False)"
    )
    args = parser.parse_args()

    # DEFAULT_CONFIG already applies TRADINGAGENTS_* env-var overrides
    config = DEFAULT_CONFIG.copy()

    # Initialize with custom config
    ta = TradingAgentsGraph(debug=args.verbose, config=config)

    # forward propagate
    print(f"Starting non-interactive analysis for {args.ticker} on {args.date}...")
    final_state, decision = ta.propagate(args.ticker, args.date)
    print("\n=== ANALYSIS RESULT ===")
    print(decision)

    # Save Markdown report
    try:
        from pathlib import Path
        from cli.main import save_report_to_disk
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        ticker_clean = args.ticker.strip().upper()
        save_path = Path("reports") / f"{ticker_clean}_{timestamp}"
        
        report_file = save_report_to_disk(final_state, ticker_clean, save_path)
        print(f"\n[Success] Consolidated report generated at: {report_file}")
    except Exception as e:
        print(f"\n[Warning] Could not generate Markdown report: {e}")

if __name__ == "__main__":
    main()

