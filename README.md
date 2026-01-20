# 📊 TOPSIS Web Service

A web-based implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using **Python and Streamlit**.  
This project allows users to rank alternatives from a CSV file by applying custom weights and impacts in an interactive and visually appealing interface.

**Created by:** Purnika Malhotra  

---

## 🔍 What is TOPSIS?

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** technique used to rank alternatives based on their closeness to an ideal solution.  
The best alternative is the one that has:
- **Shortest distance from the ideal best solution**
- **Farthest distance from the ideal worst solution**

---

## 🧠 TOPSIS Methodology

The TOPSIS algorithm follows these steps:

1. **Construct the Decision Matrix**  
   The input CSV file contains alternatives (rows) and criteria (columns).

2. **Normalize the Decision Matrix**  
   Each criterion is normalized to remove scale differences.

3. **Apply Weights**  
   User-defined weights are applied to each criterion to reflect importance.

4. **Determine Ideal Best and Ideal Worst**  
   - Ideal Best: Best values for benefit criteria, worst for cost criteria  
   - Ideal Worst: Worst values for benefit criteria, best for cost criteria

5. **Calculate Separation Measures**  
   Euclidean distance from ideal best and ideal worst is calculated.

6. **Compute TOPSIS Score**  
   The relative closeness to the ideal solution is calculated.

7. **Rank Alternatives**  
   Higher TOPSIS score indicates a better alternative.

---

## ⚙️ Features

- Upload CSV file with decision data
- Custom weights and impacts input
- Input validation for correctness
- Automatic ranking using TOPSIS
- Downloadable ranked output CSV
- Clean, modern UI built with Streamlit

---

## 📁 Input Format

- CSV file must contain **at least 3 columns**
- First column: Alternative names (non-numeric)
- Remaining columns: Numeric criteria values
- Weights and impacts must match the number of criteria

Example:
