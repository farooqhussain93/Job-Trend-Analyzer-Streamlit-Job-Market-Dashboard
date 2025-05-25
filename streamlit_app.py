
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load data
df = pd.read_csv('rozee_jobs.csv')

st.title("Real-Time Job Trend Analyzer")

st.write("### Raw Job Data")
st.dataframe(df.head())

# Top 5 Most In-Demand Job Titles
st.write("### Top 5 Most In-Demand Job Titles")
top_titles = df['Title'].value_counts().head(5)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_titles.values, y=top_titles.index, palette='Blues_r', ax=ax1)
ax1.set_xlabel("Number of Listings")
ax1.set_ylabel("Job Title")
st.pyplot(fig1)

# Top 5 Required Skills
# st.write("### Top 5 Required Skills")
# all_skills = df['skills'].dropna().str.split(',').sum()
# skill_counts = Counter([skill.strip() for skill in all_skills])
# top_skills = dict(skill_counts.most_common(5))
# fig2, ax2 = plt.subplots()
# sns.barplot(x=list(top_skills.values()), y=list(top_skills.keys()), palette='Greens_r', ax=ax2)
# ax2.set_xlabel("Frequency")
# ax2.set_ylabel("Skills")
# st.pyplot(fig2)

# Cities with Highest Number of Openings
st.write("### Top Hiring Cities")
top_cities = df['Location'].value_counts().head(5)
fig3, ax3 = plt.subplots()
sns.barplot(x=top_cities.values, y=top_cities.index, palette='Oranges_r', ax=ax3)
ax3.set_xlabel("Number of Listings")
ax3.set_ylabel("City")
st.pyplot(fig3)

# Posting Trends Over Time (if available)
if 'date_posted' in df.columns:
    df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')
    df['post_date'] = df['date_posted'].dt.date
    st.write("### Job Postings Over Time")
    trend_data = df['post_date'].value_counts().sort_index()
    fig4, ax4 = plt.subplots()
    trend_data.plot(kind='line', marker='o', ax=ax4)
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Number of Jobs")
    st.pyplot(fig4)

# Optional Keyword Filter
search_term = st.text_input("🔍 Enter a keyword to filter jobs (e.g., Data Analyst):")
if search_term:
    filtered = df[df['title'].str.contains(search_term, case=False, na=False)]
    st.write(f"### Filtered Results for '{search_term}'")
    st.dataframe(filtered.head())
