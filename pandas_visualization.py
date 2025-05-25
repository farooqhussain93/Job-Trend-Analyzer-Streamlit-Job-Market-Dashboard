import pandas as pd
import matplotlib.pyplot as plt
import collections

# Load CSV
df = pd.read_csv("rozee_jobs.csv")

# Show preview
print("\nPreview of Job Listings:\n")
print(df.head())

# Drop rows with missing titles/companies/locations
df.dropna(subset=["Title", "Company", "Location"], inplace=True)

# Top Job Titles
print("\nTop 5 Most Common Job Titles:")
top_titles = df["Title"].value_counts().head(5)
print(top_titles)

top_titles.plot(kind="bar", title="Top 5 Job Titles", color='skyblue')
plt.ylabel("Count")
plt.xlabel("Job Title")
plt.tight_layout()
plt.show()

# Top Cities
print("\nTop 5 Cities With Most Openings:")
top_cities = df["Location"].value_counts().head(5)
print(top_cities)

top_cities.plot(kind="bar", title="Top Cities", color='orange')
plt.ylabel("Count")
plt.xlabel("City")
plt.tight_layout()
plt.show()

# 🔎 Check for 'Description' column before skill analysis
if "Description" in df.columns:
    df["Description"] = df["Description"].fillna("").str.lower()
    common_skills = ["python", "excel", "sql", "java", "communication", "sales", "marketing", "react", "css", "html"]

    skills_found = []

    for desc in df["Description"]:
        for skill in common_skills:
            if skill in desc:
                skills_found.append(skill)

    skill_counts = dict(collections.Counter(skills_found))

    print("\nMost In-Demand Skills:")
    for skill, count in skill_counts.items():
        print(f"{skill}: {count}")

    plt.bar(skill_counts.keys(), skill_counts.values(), color='green')
    plt.xticks(rotation=45)
    plt.title("Most In-Demand Skills")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
else:
    print("\n No 'Description' column found. Skipping skill analysis.")