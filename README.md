🧹 Data Cleaning Project

📌 Overview
This project focuses on cleaning, transforming, and preparing raw datasets for analysis and machine learning tasks. We work with two datasets:
AB_NYC_2019.csv.zip → Airbnb listings in New York City for 2019
CA_category_id.json → JSON file containing category information
The main goal is to ensure data integrity, consistency, and usability by handling common data quality issues.

⚙️ Features
The cleaning pipeline covers the following tasks:

Data Integrity
-Verified schema consistency, data types, and column names

Missing Data Handling
-Filled numeric columns with mean
-Filled categorical columns with mode
-Dropped rows with all missing values

Duplicate Removal
-Removed duplicate rows to maintain uniqueness

Standardization
-Renamed columns to lowercase and snake_case
-Converted date columns into datetime format
-Ensured consistent units and formats

Outlier Detection & Removal
-Applied IQR method to filter out extreme values
-Visualized outliers using boxplots

Data Export
-Final cleaned dataset saved as cleaned_data.csv

🗂️ Folder Structure
python
Copy
Edit
Data Cleaning/
│
├── main.py                # Main cleaning script
├── AB_NYC_2019.csv.zip    # Raw Airbnb dataset
├── CA_category_id.json    # Raw JSON dataset
├── cleaned_data.csv       # Final cleaned dataset (output)
└── README.md              # Project documentation

🚀 Installation & Usage
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/data-cleaning.git
cd data-cleaning

2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Run the Script
bash
Copy
Edit
python main.py

📊 Visualizations

Missing Data → Plotted using missingno
Outliers → Boxplots created using seaborn & matplotlib

Example:
python
Copy
Edit
import seaborn as sns
sns.boxplot(x=final_df['price'])

📝 Requirements
Python 3.8+
pandas
numpy
matplotlib
seaborn
missingno

Install all dependencies:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn missingno
✅ Output
After running the script, you will get:

cleaned_data.csv → Final cleaned dataset, ready for EDA, visualization, or machine learning.

📌 Next Steps
Perform Exploratory Data Analysis (EDA)

Build dashboards/visualizations

Use the cleaned dataset for ML models

👨‍💻 Author
Diyansh Rana
📧 [diyanshranajii2gmail.com]
