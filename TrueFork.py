import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data recipes
recipes = pd.read_csv('Data/RAW_recipes.csv')
recipes

# Data interactions
interactions = pd.read_csv('Data/interactions.csv')
interactions

# Replace ratings of 0 with NaN
interactions['rating'] = interactions['rating'].replace(0, np.nan)

# Average rating per recipe
avg_ratings = interactions.groupby('recipe_id')['rating'].mean().rename('avg_rating')

# Merge recipes & average ratings
merged = recipes.merge(avg_ratings, left_on='id', right_on='recipe_id', how='left')

# Parse the 'nutrition' column --> separate numeric fields
def parse_nutrition(nutr_str):
    if pd.isna(nutr_str) or len(nutr_str) < 2:
        return [np.nan]*7
    nutrients = nutr_str.strip('[]').split(',')
    try:
        nutrients = [float(val.strip()) for val in nutrients]
    except:
        nutrients = [np.nan]*7
    return nutrients

nutrient_cols = ['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']
nutrition_values = merged['nutrition'].apply(parse_nutrition).tolist()
nutrition_df = pd.DataFrame(nutrition_values, columns=nutrient_cols)

# Concatenate nutritional info back to merged dataset
cleaned = pd.concat([merged, nutrition_df], axis=1)

# Drop recipes without any valid average rating
cleaned = cleaned.dropna(subset=['avg_rating'])

# Cleaned DataFrame
print("Cleaned Dataset Preview:")
print(cleaned[['id', 'name', 'minutes', 'avg_rating', 'calories', 'sugar', 'total_fat', 'protein', 'carbohydrates']].head(), "\n")

# Summary statistics
numeric_cols = ['minutes', 'avg_rating', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']
print("Summary Statistics:")
print(cleaned[numeric_cols].describe(), "\n")

# Plot: Distribution of Average Ratings
plt.figure(figsize=(8, 4))
plt.hist(cleaned['avg_rating'], bins=20, edgecolor='black')
plt.title('Distribution of Average Recipe Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Frequency')
plt.show()

# Plot: Distribution of Calories
plt.figure(figsize=(8, 4))
plt.hist(cleaned['calories'].dropna(), bins=25, edgecolor='black')
plt.title('Distribution of Recipe Calories')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.show()

# Plot: Preparation Time vs. Average Rating
plt.figure(figsize=(8, 5))
plt.scatter(cleaned['minutes'], cleaned['avg_rating'], alpha=0.5)
plt.title('Preparation Time vs. Average Rating')
plt.xlabel('Minutes to Prepare')
plt.ylabel('Average Rating')
plt.show()

# Correlation between calories and average rating
corr_cal_rtg = cleaned[['calories', 'avg_rating']].dropna().corr().iloc[0, 1]
print(f"Correlation between calories and average rating: {corr_cal_rtg:.4f}\n")

# Top 5 Highest-Rated and Lowest-Rated Recipes
highest_rated = cleaned.nlargest(5, 'avg_rating')[['name', 'avg_rating', 'calories', 'minutes']]
lowest_rated = cleaned.nsmallest(5, 'avg_rating')[['name', 'avg_rating', 'calories', 'minutes']]

print("Top 5 Highest Rated Recipes:")
print(highest_rated, "\n")

print("Top 5 Lowest Rated Recipes:")
print(lowest_rated)
