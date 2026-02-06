import pandas as pd

class DataTransform:
    def to_int_nullable(self, series):
        """Convert numeric-like column to nullable integer"""
        return pd.to_numeric(series, errors="coerce").astype("Int64")

    def to_float(self, series):
        """Convert column to float"""
        return pd.to_numeric(series, errors="coerce")

    def parse_term_months(self, series):
        """Convert '36 months' → 36"""
        extracted = series.astype(str).str.extract(r"(\d+)", expand=False)
        return pd.to_numeric(extracted, errors="coerce").astype("Int64")

    def parse_percentage(self, series):
        """Convert '13.5%' → 13.5"""
        cleaned = series.astype(str).str.replace("%", "", regex=False).str.strip()
        return pd.to_numeric(cleaned, errors="coerce")

    def parse_month_year(self, series):
        """Convert 'Jan-2022' → datetime"""
        return pd.to_datetime(series, format="%b-%Y", errors="coerce")

    def apply_all(self, df):
        """
        Apply key conversions in one place.
        """
        df = df.copy()

        # IDs
        if "id" in df.columns:
            df["id"] = self.to_int_nullable(df["id"])
        if "member_id" in df.columns:
            df["member_id"] = self.to_int_nullable(df["member_id"])

        # Term
        if "term" in df.columns:
            df["term_months"] = self.parse_term_months(df["term"])

        # Interest rate
        if "int_rate" in df.columns:
            df["int_rate"] = self.parse_percentage(df["int_rate"])

        # Dates
        for col in ["issue_date", "last_payment_date", "next_payment_date", "last_credit_pull_date"]:
            if col in df.columns:
                df[col] = self.parse_month_year(df[col])

        return df
