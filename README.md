# TrueFork  
By Stephanie Anshell and Ved Panse
---
## Introduction

**What we wanted to find out:**
We explored a massive dataset of Food.com recipes and user reviews to answer one simple but important question:
**Are healthy recipes rated worse than unhealthy ones?**

**Why this question matters:**
Nutrition-conscious cooks often wonder whether choosing healthier meals means sacrificing taste—or at least, popularity. If online ratings tend to favor indulgent dishes, this might skew what people choose to cook or share. Our analysis helps shed light on potential biases in online recipe ratings and could be useful to food bloggers, nutritionists, or anyone curious about how healthiness affects perception.

**Where the data came from:**
We used two files from Food.com:

* `RAW_recipes.csv`, which includes over 230,000 recipes with ingredients, cooking time, and nutrition information.
* `RAW_interactions.csv`, which contains nearly 1 million user ratings and reviews, dating back to 2008.

After merging and cleaning these datasets:

* We analyzed a dataset of **83,782 recipes** and **13 columns**, each with an associated **average rating** based on user feedback.
* Key columns we used in our analysis:

  * `nutrition`: A list of values (as a string) containing calories, fat, sugar, etc.
  * `avg_rating`: The average rating a recipe received (from 1.0 to 5.0).
  * `is_unhealthy`: A binary column we created to label recipes as unhealthy if their calorie or sugar content exceeded a certain threshold.

**Our main question (framed for statistical testing):**

> **Do unhealthy recipes receive higher average ratings than healthy ones?**

* **Null Hypothesis (H₀):** There's no difference in average ratings between healthy and unhealthy recipes.
* **Alternative Hypothesis (H₁):** Unhealthy recipes are rated higher than healthy ones.

---

## Data Cleaning and Exploration  
### Dataset Cleaning

We started with two CSVs: `RAW_recipes.csv` and `RAW_interactions.csv`. The recipes dataset includes information like ingredients, cooking steps, and a `nutrition` column (a stringified list of nutrient values). The interactions dataset contains user-submitted ratings and reviews for specific recipe IDs.

### Cleaning Steps:

1. **Merged the Datasets**
   We merged `RAW_recipes` (left) and `RAW_interactions` (right) on `id = recipe_id`. This gave us a single table with both recipe details and user feedback.

2. **Replaced Invalid Ratings**
   Some ratings were recorded as `0`, which likely doesn’t indicate a true rating (Food.com uses a 1–5 scale). We treated these as missing by replacing all 0s with `np.nan`.

3. **Computed Average Rating**
   For each recipe, we computed the average of its valid (non-NaN) ratings and stored this in a new column: `avg_rating`.

4. **Parsed Nutrition Info**
   The `nutrition` column contained a stringified list of values like `[calories, fat, sugar, sodium, protein, saturated_fat, carbs]`. We parsed this into individual numeric columns.

5. **Created `is_unhealthy` Flag**
   We created a new column `is_unhealthy`, which is `True` for recipes above the 75th percentile in calories, sugar, and fat — and `False` otherwise. This lets us label recipes as “healthy” or “unhealthy” for hypothesis testing.

6. **Kept NaNs in `avg_rating` for Now**
   Recipes with no valid ratings have `NaN` in `avg_rating`. Instead of dropping them during cleaning, we left them in and filtered them out only when needed (e.g. in hypothesis testing or modeling).

These steps were necessary to ensure that downstream analysis (e.g. comparing healthy vs. unhealthy recipe ratings) relied only on meaningful, interpretable data. Without parsing the nutrition column or addressing the invalid ratings, we’d risk basing conclusions on broken or irrelevant inputs.

### Cleaned Dataset Preview

Here’s the head of our cleaned dataset:
![Preview of cleaned dataset head](images/step2-head.png)
---

## Missing Data  

We noticed that a lot of ratings were listed as 0, which probably means they were missing or invalid. We treated those as `NaN`. Recipes that had no valid ratings at all were removed, just so we wouldn’t be basing anything off of empty data.

---

## Hypothesis Testing  

We ran a permutation test (5,000 iterations) to compare the average ratings of healthy vs. unhealthy recipes.  

- **Observed difference:** -0.0031  
- **p-value:** 0.7248  

Since the p-value is way above 0.05, we couldn’t reject the null hypothesis. So, there's no solid evidence that unhealthy recipes are rated higher. If anything, healthy ones might be slightly better rated — but the difference is tiny and probably just random.

---

## Prediction Problem  

We turned this into a yes/no prediction:  
> Will a recipe get a high rating (4.5 or above)?

To do this, we used:
- Features like calories, sugar, fat, number of ingredients, etc.
- A binary target column: `high_rating = True` if average rating ≥ 4.5

---

## Baseline Model  

Our starting point was super simple: we used a `DummyClassifier` that always predicts the most common class — which is `high_rating = False`.  

Not surprisingly, it got an accuracy of around **74.82%**, which just reflects the fact that most recipes aren't rated super high.

---

## Final Model  

To do better, we used a **Random Forest Classifier**. It works well with messy data, captures nonlinear patterns, and doesn’t need a ton of tweaking to perform decently. We used features like calories, sugar, fat, and number of ingredients.

If we ever want to understand *why* a recipe gets a good rating, we’d switch to a **Logistic Regression model**, since it’s easier to interpret.

---

## Fairness Check  

We looked at whether the model was being unfair to certain kinds of recipes (like healthy vs. unhealthy).  
So far, it seems okay — accuracy didn’t vary much across recipe types. That said, more fairness testing (maybe by cuisine or ingredient type) would be interesting for the future.
