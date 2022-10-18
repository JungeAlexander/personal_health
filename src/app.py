import os
from datetime import date, datetime, timedelta

import altair as alt
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from qself.oura import OuraAPIClient

load_dotenv()
client = OuraAPIClient(os.environ["OURA_PERSONAL_ACCESS_TOKEN"])


# TODO cache this with st.cache and/or lru cache within same day?
def get_step_df(years_ago: int, day_range: int) -> pd.DataFrame:
    current_end = date.today()
    current_start = current_end - timedelta(days=day_range)
    prev_end = current_end - timedelta(days=365 * years_ago)  # TODO quick and dirty
    prev_start = prev_end - timedelta(days=day_range)
    current_da = client(
        "daily_activity",
        current_start.isoformat(),
        (current_end + timedelta(days=1)).isoformat(),
    )
    prev_da = client(
        "daily_activity",
        prev_start.isoformat(),
        (prev_end + timedelta(days=1)).isoformat(),
    )
    days = list(range(-day_range, 1)) * 2
    steps = []
    years = []
    timestamps = []
    for data, year in ((current_da, "current"), (prev_da, "previous")):
        for d in data["data"]:
            timestamp = d["timestamp"]
            dt = datetime.fromisoformat(timestamp)
            steps.append(d["steps"])
            years.append(str(dt.year))
            timestamps.append(timestamp)
    return pd.DataFrame(
        {
            "day": days,
            "steps": steps,
            "year": years,
            "timestamp": timestamps,
        }
    )


st.title("Oura review")

years_ago = st.slider("Year(s) ago", min_value=1, max_value=5, value=1)
day_range = st.slider("Days compared", min_value=0, max_value=30, value=6)

step_df = get_step_df(years_ago, day_range)

step_chart = (
    alt.Chart(step_df)
    .mark_line(point=True)
    .encode(
        x="day",
        y="steps",
        color="year",
    )
)

st.altair_chart(step_chart, use_container_width=False)
st.dataframe(step_df)
