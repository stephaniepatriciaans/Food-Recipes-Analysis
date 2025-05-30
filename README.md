# TrueFork  
By Stephanie Anshell and Ved Panse

## Introduction  
**What we wanted to find out:**  
We looked at recipes from Food.com to see if healthy dishes are rated any differently than indulgent ones. After that, we tried to build a model that could predict whether a recipe would get a high rating.

**Where the data came from:**  
We used two CSVs: `RAW_recipes.csv` and `RAW_interactions.csv`. These include thousands of recipes and user reviews going all the way back to 2008.

**Our main question:**  
Do healthy recipes get rated worse than unhealthy ones?  

- **Null Hypothesis (H₀):** There's no difference in average ratings between healthy and unhealthy recipes.  
- **Alternative Hypothesis (H₁):** Unhealthy recipes are rated higher than healthy ones.

---

## Data Cleaning and Exploration  

Here’s what we did to clean and explore the data:

- Merged `recipes` and `interactions` on `id = recipe_id`
- Replaced any rating of 0 with `NaN`, then calculated the average rating per recipe
- Broke down the `nutrition` field (which was a string) into separate numeric columns like calories, sugar, fat, etc.
- Dropped recipes that didn’t have any valid ratings
- (-- Add example table later --)

We also made an interactive plot:
// TODO fill it in here Steph!

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
