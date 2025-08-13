#!/usr/bin/env python3
"""
Skeletal Python script with logging, pandas operations, and proper exit handling.
"""

import logging
import sys
import pandas as pd


def setup_logging():
    """Setup basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def main():
    """Main function containing the core logic."""
    
    try:
        logging.info("Starting application...")

        # Create a sample pandas DataFrame
        data = {
            'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'age': [25, 30, 35, 28],
            'city': ['New York', 'London', 'Tokyo', 'Paris']
        }
        df = pd.DataFrame(data)
        
        logging.info(f"Created pandas DataFrame with {len(df)} rows")
        logging.info(f"DataFrame columns: {list(df.columns)}")

        # Display the DataFrame
        print("\nSample DataFrame:")
        print(df)

        logging.info("Application completed successfully")
        return 0
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return 1


if __name__ == "__main__":
    setup_logging()
    exit_code = main()
    sys.exit(exit_code)
