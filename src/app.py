import altair as alt
import pandas as pd
import streamlit as st


# TODO cache this with st.cache and lru cache within same day?
def get_step_df(years_ago, day_range) -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "day": list(range(-day_range, 1)) * 2,
            "steps": [10000] * (day_range + 1) + [9000] * (day_range + 1),
            "year": ["current"] * (day_range + 1) + ["previous"] * (day_range + 1),
        }
    )
    return df


st.title("Oura review")

years_ago = st.slider("Year(s) ago", min_value=1, max_value=5, value=1)
day_range = st.slider("Days compared", min_value=0, max_value=30, value=6)

step_df = get_step_df(years_ago, day_range)

step_chart = (
    alt.Chart(step_df)
    .mark_line()
    .encode(
        x="day",
        y="steps",
        color="year",
    )
)

st.altair_chart(step_chart, use_container_width=False)
st.dataframe(step_df)
