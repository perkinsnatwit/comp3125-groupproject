# College Data Analysis Project

A comprehensive Python project for analyzing college datasets through feature engineering and data visualization. This project analyzes college metrics including admission rates, tuition costs, and graduation outcomes for leading Boston-area institutions.

## Overview

This project processes college enrollment and performance data to extract meaningful insights about graduation rates, admission selectivity, tuition costs, and cohort demographics. It combines feature engineering techniques with advanced visualizations to provide a detailed analysis of college metrics.

The dataset includes 12 major colleges and universities with data on application volume, admission rates, graduation rates (4-year and 6-year), and tuition costs.

## Project Structure

```
comp3125-groupproject/
├── src/
│   ├── main.py                          # Main entry point - runs full pipeline
│   ├── feature_engineering_class.py     # FeatureEngineer class for feature creation
│   ├── feature_engineering.py           # Standalone feature engineering script
│   ├── visualization_class.py           # CollegeVisualizer class for plotting
│   ├── visualization.py                 # Standalone visualization script
│   └── __init__.py                      # Package initialization
├── datasets/
│   ├── dataset.csv                      # Primary college dataset
│   ├── engineered_data.csv              # Output: processed data with engineered features
│   ├── colleges_100.csv                 # Sample dataset (100 colleges)
│   └── college_data.csv                 # Alternative college dataset format
├── figures/                             # Output directory for generated visualizations
├── requirements.txt                     # Python package dependencies
└── README.md                            # This file
```

## Data

### Dataset Overview

The project analyzes 12 Boston-area colleges:
- Harvard University
- MIT (Massachusetts Institute of Technology)
- Tufts University
- Northeastern University
- Boston University
- Boston College
- Emerson College
- Suffolk University
- Emmanuel College
- MCPHS (Massachusetts College of Pharmacy and Health Sciences)
- Simmons University
- Wentworth Institute of Technology

### Data Columns

| Column | Description |
|--------|-------------|
| `colleges` | Name of the institution |
| `application_volume` | Number of applications received |
| `admission_rate` | Proportion of applicants admitted (decimal: 0-1) |
| `graduate_rate_4yr` | Proportion of cohort graduating within 4 years (decimal: 0-1) |
| `graduate_rate_6yr` | Proportion of cohort graduating within 6 years (decimal: 0-1) |
| `tuition_cost` | Annual tuition cost in USD |

## Features

### Feature Engineering

The `FeatureEngineer` class creates the following engineered features:

1. **Average Graduation Rate** (`avg_graduation_rate`)
   - Calculation: `(graduate_rate_4yr + graduate_rate_6yr) / 2`
   - Rounded to 3 decimal places
   - Provides overall graduation success metric

2. **Graduation Rate Improvement** (`graduation_rate_improvement`)
   - Calculation: `graduate_rate_6yr - graduate_rate_4yr`
   - Rounded to 3 decimal places
   - Shows increase from 4-year to 6-year completion

3. **Selectivity Score** (`selectivity_score`)
   - Calculation: `1 / admission_rate`
   - Rounded to 2 decimal places
   - Higher score = more selective/competitive institution
   - Inverts admission rate for intuitive interpretation

4. **Cohort Size** (`cohort_size`)
   - Calculation: `application_volume * admission_rate`
   - Rounded to 2 decimal places
   - Estimates size of admitted cohort

### Visualizations

The `CollegeVisualizer` class generates 9 comprehensive visualizations:

1. **Correlation Heatmap** (`correlation_heatmap.png`)
   - Shows correlations between all numeric college metrics
   - Identifies relationships between variables

2. **Selectivity vs 4-Year Graduation** (`selectivity_score_vs_4yr_graduation.png`)
   - Scatter plot with college names as hue
   - Analyzes relationship between selectivity and early graduation

3. **Selectivity vs 6-Year Graduation** (`selectivity_score_vs_6yr_graduation.png`)
   - Scatter plot showing selectivity vs longer-term graduation
   - Enables comparison with 4-year outcomes

4. **Admission Rate vs 6-Year Graduation** (`admission_vs_6yr_graduation.png`)
   - Direct examination of admission rate impact on graduation
   - Color-coded by college for easy identification

5. **Admission Rate vs 4-Year Graduation** (`admission_rate_vs_4yr_graduation.png`)
   - Scatter plot of admission selectivity vs early completion

6. **Tuition vs 4-Year Graduation (Dual-Axis)** (`tuition_vs_4yr_graduation_dual.png`)
   - Bar chart (tuition) + line plot (graduation rate)
   - Compares cost with early graduation outcomes

7. **Tuition vs 6-Year Graduation (Dual-Axis)** (`tuition_vs_6yr_graduation_dual.png`)
   - Bar chart (tuition) + line plot (6-year graduation)
   - Analyzes long-term graduation vs tuition investment

8. **Cohort Size vs 4-Year Graduation (Dual-Axis)** (`cohort_size_vs_4yr_graduation_dual.png`)
   - Bar chart (cohort size) + line plot (graduation rate)
   - Examines enrollment scale vs graduation success

9. **Cohort Size vs 6-Year Graduation (Dual-Axis)** (`cohort_size_vs_6yr_graduation_dual.png`)
   - Analyzes how cohort size relates to 6-year outcomes

## Project Team

**COMP3125 Group Project** - Chrisantus Odewumi, Nathaniel Perkins, Sahil Ramani
