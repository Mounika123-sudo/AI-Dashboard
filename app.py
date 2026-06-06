import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv("IPL_Matches_2008_2022.csv")
df = df.drop_duplicates()
df = df.fillna("Unknown")
st.title("IPL AI Dashboard")

st.dataframe(df.head())
st.metric("Total Matches", len(df))
st.metric("Total Cities", df["City"].nunique())
st.metric("Total Seasons", df["Season"].nunique())
season_count = df["Season"].value_counts()

fig = px.bar(
    x=season_count.index,
    y=season_count.values,
    title="Matches Per Season"
)

st.plotly_chart(fig)
city_count = df["City"].value_counts().head(10)

fig = px.bar(
    x=city_count.index,
    y=city_count.values,
    title="Top 10 Cities by Matches"
)

st.plotly_chart(fig)
win_count = df["WinningTeam"].value_counts().head(10)

fig = px.bar(
    x=win_count.index,
    y=win_count.values,
    title="Top Winning Teams"
)

st.plotly_chart(fig)
fig = px.pie(
    df,
    names="TossDecision",
    title="Toss Decisions"
)

st.plotly_chart(fig)
pom = df["Player_of_Match"].value_counts().head(10)

fig = px.bar(
    x=pom.index,
    y=pom.values,
    title="Top 10 Player of the Match Winners"
)

st.plotly_chart(fig)
season = st.sidebar.selectbox(
    "Select Season",
    sorted(df["Season"].unique())
)

filtered_df = df[df["Season"] == season]

st.subheader(f"Matches in Season {season}")
st.dataframe(filtered_df)