#  An Intelligent Decision Ranking System using TOPSIS

**View it at** : https://topsis-19.streamlit.app/

A web-based implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using **Python and Streamlit**.  
This project allows users to rank alternatives from a CSV file by applying custom weights and impacts in an interactive and visually appealing interface.

**Created by:** Purnika Malhotra  

---

##  What is TOPSIS?

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** technique used to rank alternatives based on their closeness to an ideal solution.  
The best alternative is the one that has:
- **Shortest distance from the ideal best solution**
- **Farthest distance from the ideal worst solution**

---
## Python Package Publication

In addition to the web application, this project has been converted into a Python package implementing the TOPSIS algorithm. The package provides a command-line interface (CLI) that allows users to apply TOPSIS directly on CSV files without using the web interface.

**Link** : https://pypi.org/project/topsis-purnika-102303412/1.0.2/

The package was:

1. Structured following standard Python packaging guidelines

2. Tested locally using pip install .

3. Uploaded to TestPyPI for validation

4. Uploaded to PyPI for public access

5. Users can install the package using pip and run TOPSIS from the command line by providing input data, weights, and impacts.

**Example usage:**

topsis input.csv "1,1,1" "+,+,-" output.csv


This dual implementation (web application + Python package) makes the project flexible for both interactive use and programmatic/CLI-based decision analysis.

---

##  TOPSIS Methodology

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

##  Features

- Upload CSV file with decision data
- Custom weights and impacts input
- Input validation for correctness
- Automatic ranking using TOPSIS
- Downloadable ranked output CSV
- Clean, modern UI built with Streamlit

---

##  Input Format

- CSV file must contain **at least 3 columns**
- First column: Alternative names (non-numeric)
- Remaining columns: Numeric criteria values
- Weights and impacts must match the number of criteria

---

**Result Table (Output)**

After applying the TOPSIS algorithm, the system generates a ranked result table and provides it as a downloadable CSV file.

The output file contains all original columns along with the following additional fields:

**Topsis Score**
1. Represents the relative closeness of each alternative to the ideal solution.
The value lies between 0 and 1, where a higher score indicates a better alternative.

2. Rank
Alternatives are ranked in descending order based on the TOPSIS score.
Rank 1 corresponds to the best alternative.



