import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        """Return column names + dtypes"""
        return pd.DataFrame({
            "Column": self.df.columns,
            "Data Type": self.df.dtypes.values
        })

    def statistical_summary(self):
        """Mean/median/std for numeric columns"""
        numeric_df = self.df.select_dtypes(include=["number"])
        return pd.DataFrame({
            "Mean": numeric_df.mean(),
            "Median": numeric_df.median(),
            "Std Dev": numeric_df.std()
        })

    def categorical_counts(self):
        """Unique value counts for categorical columns"""
        categorical_cols = self.df.select_dtypes(include=["object", "category"]).columns
        return self.df[categorical_cols].nunique().sort_values(ascending=False)

    def dataframe_shape(self):
        """Rows/columns"""
        rows, cols = self.df.shape
        return f"Rows: {rows}, Columns: {cols}"

    def null_summary(self):
        """Null count + % per column"""
        null_count = self.df.isnull().sum()
        null_pct = (null_count / len(self.df) * 100).round(2)
        return pd.DataFrame({
            "Null Count": null_count,
            "Null Percentage": null_pct
        }).sort_values("Null Percentage", ascending=False)
