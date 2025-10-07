import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("university_database.db")  # adjust if needed
TABLE = "university_rankings"

def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found at: {DB_PATH.resolve()}")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql(f"SELECT * FROM {TABLE};", conn)

    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    if "world_rank" in df.columns:
        df["world_rank"] = pd.to_numeric(df["world_rank"], errors="coerce").astype("Int64")
    if "score" in df.columns:
        df["score"] = pd.to_numeric(df["score"], errors="coerce")

    # insert duke tech
    new_row = {
        "year": 2014,
        "institution": "Duke Tech",
        "country": "USA",
        "world_rank": 350,
        "score": 60.5,
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # check to make sure duke tech inserted
    duke_df = df.loc[df["institution"] == "Duke Tech"].copy()
    print("\nRows for 'Duke Tech':")
    print(duke_df)

    # check to make sure duke tech
    duke_count = (df["institution"] == "Duke Tech").sum()
    print("\nDuke Tech count:", int(duke_count))

    # 4) number of japan colleges in top 200
    jp_top200_2013 = (
        df.loc[(df["country"] == "Japan") & (df["world_rank"].notna()) & (df["world_rank"] <= 200) & (df["year"] == 2013)]
          .groupby("country")
          .size()
          .reset_index(name="total")
    )
    print("\nJapan in top-200 (2013):")
    print(jp_top200_2013)

    # check oxford score
    ox_before = df.loc[(df["year"] == 2014) & (df["institution"] == "University of Oxford"), ["year", "institution", "score"]]
    print("\nOxford 2014 (before update):")
    print(ox_before)

    # update score
    mask_ox_2014 = (df["year"] == 2014) & (df["institution"] == "University of Oxford")
    df.loc[mask_ox_2014, "score"] = (df.loc[mask_ox_2014, "score"] + 1.2).round(2)

    # check score update
    ox_after = df.loc[mask_ox_2014, ["year", "institution", "score"]]
    print("\nOxford 2014 (after update):")
    print(ox_after)

    # check amount of colleges that need to be deleted
    mask_2015_low = (df["year"] == 2015) & df["score"].notna() & (df["score"] < 45)
    deleting_count = int(mask_2015_low.sum())
    print("\nWill delete (year=2015 & score < 45):", deleting_count)

    # delete
    df = df.loc[~mask_2015_low].copy()

    # check deletion
    remaining_count = int(((df["year"] == 2015) & df["score"].notna() & (df["score"] < 45)).sum())
    print("Remaining (year=2015 & score < 45):", remaining_count)

    # Persist changes back to SQLite (overwrite the table with the modified DataFrame)
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE, conn, if_exists="replace", index=False)

    print("\nDone. Table updated in the database.")

if __name__ == "__main__":
    main()
