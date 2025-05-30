# TrueFork
By Stephanie Anshell and Ved Panse

## Introduction
**Project goal**: Analyze Food.com recipes to see if healthy dishes are rated differently than indulgent ones, then build a prediction model for recipe ratings.

**Data source**: mention RAW_recipes.csv and RAW_interactions.csv (recipes since 2008).

**Null hypothesis**: There is no difference in mean ratings between healthy and unhealthy recipes.


## Data Cleaning and Exploratory Data Analysis
- **Merge recipes & interactions** on `id = recipe_id`  
- **Convert** 0 → `NaN`, compute `mean_rating`  
- **Parse** `nutrition` into numeric columns  
- **Example table** (via `.to_markdown()`)  
- **Interactive plot**:
  <iframe
    src="assets/your-plot.html"
    width="800"
    height="600"
    frameborder="0"
  ></iframe>

## Assessment of Missingness

## Hypothesis Testing

## Framing a Prediction Problem

## Baseline Model

## Final Model

## Fairness Analysis
