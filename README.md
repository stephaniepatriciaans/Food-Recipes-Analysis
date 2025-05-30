# TrueFork
By Stephanie Anshell and Ved Panse

## Introduction
**Project goal**: Analyze Food.com recipes to see if healthy dishes are rated differently than indulgent ones, then build a prediction model for recipe ratings.

**Data source**: We used two datasets from Food.com — `RAW_recipes.csv` and `RAW_interactions.csv` — which include over 200,000 recipes and user interactions dating back to 2008.

**Null hypothesis**: There is no difference in mean ratings between healthy and unhealthy recipes.

---

## Data Cleaning and Exploratory Data Analysis
- **Merge recipes & interactions** on `id = recipe_id`
- **Convert** ratings of 0 to `NaN`, then compute the `avg_rating` per recipe
- **Parse** the `nutrition` column into separate numerical features such as calories, sugar, fat, etc.
- **Drop rows** where average rating is missing
- **Example table** (-- later --)
- **Interactive plot**:
  <iframe
    src="assets/your-plot.html"
    width="800"
    height="600"
    frameborder="0"
  ></iframe>

---

## Assessment of Missingness
We observed missing values in the `rating` column of `RAW_interactions.csv`, where many entries had a rating of 0 (interpreted as missing). These were replaced with `NaN`, and recipes with no valid ratings were excluded from the final analysis to ensure rating calculations were reliable.

---

## Hypothesis Testing

**Null Hypothesis (H₀):** The average rating of unhealthy recipes is the same as the average rating of healthy recipes.  
**Alternative Hypothesis (H₁):** The average rating of unhealthy recipes is greater than the average rating of healthy recipes.

We performed a **permutation test with 5,000 iterations**, using the difference in mean ratings (unhealthy − healthy) as our test statistic.

- **Observed difference**: -0.0031  
- **p-value**: 0.7248

Since the p-value is significantly higher than 0.05, we **fail to reject the null hypothesis**. There is insufficient evidence to suggest that unhealthy recipes are rated more highly. If anything, healthy recipes may be rated slightly better—but the effect size is negligible and likely due to chance.

---

## Framing a Prediction Problem

We converted this into a **binary classification** problem:  
- **Target variable**: `high_rating`, which is True if a recipe's average rating ≥ 4.5  
- **Features**: Nutrition features (calories, sugar, fat, etc.), number of ingredients, and more

---

## Baseline Model

Our baseline model is a **DummyClassifier** used in the context of a binary classification problem (predicting whether a recipe is highly rated or not). It simply predicts the most frequent class (`high_rating = False`) and achieves an accuracy of around **74.82%** (based on class distribution).

---

## Final Model

To improve upon the baseline, we used a **Random Forest Classifier** with engineered features such as calories, sugar, and number of ingredients. This model captures nonlinear feature interactions and typically performs well with minimal tuning.

If our objective later shifts to interpretability, we plan to use a **Logistic Regression model** to better understand the influence of individual features.

---

## Fairness Analysis

We examined whether our model’s performance differed by recipe categories (e.g., diet-friendly vs. indulgent). Initial fairness checks showed no substantial accuracy gaps, though further fairness audits (e.g., by cuisine or ingredient origin) could be insightful for future work.
