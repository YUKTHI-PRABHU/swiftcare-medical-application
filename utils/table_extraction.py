import camelot
import pandas as pd

def extract_tables_from_pdf(filename):
    try:
        # Read tables from PDF
        tables = camelot.read_pdf(filename, pages='all')

        if tables.n == 0:
            return [], "⚠️ No tables found"

        # Convert Camelot tables to DataFrames
        dfs = [table.df for table in tables]

        return dfs, "✅ Tables extracted successfully"

    except Exception as e:
        return [], f"⚠️ Error: {str(e)}"
