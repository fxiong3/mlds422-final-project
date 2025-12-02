# Movie Critic Rating Prediction Project

## 🌟 Project Overview

This project focuses on building a machine learning model to predict movie critic ratings based on various movie features. The goal is to understand the factors that influence critical success and to develop a predictive model, starting with a baseline Linear Regression approach.

### Project Structure

```
/mlds422-final-project
├── .env.example              # Template for environment variables
├── .gitignore                # Files/folders to be ignored by Git
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── data/                     # Directory for raw/processed data files (ignored by Git)
├── notebook/
│   └── analysis_and_modeling.ipynb  # Jupyter notebook for EDA and ML modeling
└── src/
    └── db.py                 # Module for database connection and data loading
```

## 🛠️ Getting Started

Follow these steps to set up and run the project locally.

### 1\. Prerequisites

  * Python 3.8+
  * PostgreSQL Database (for movie data storage)

### 2\. Environment Setup

It is highly recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows
```

### 3\. Install Dependencies

Install all required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4\. Configuration

The project uses environment variables for sensitive information, such as database credentials.

1.  Copy the environment template to create your local configuration file:

    ```bash
    cp .env.example .env
    ```

2.  Edit the newly created `.env` file and fill in your PostgreSQL connection details:

    ```ini
    ## Database Configuration (PostgreSQL)
    DB_HOST=your_host_ip
    DB_PORT=5432
    DB_NAME=your_database_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    ```

### 5\. Data

The project assumes movie data is pre-loaded into a table named `public.movies` in your configured PostgreSQL database.

The `src/db.py` module handles the connection and data retrieval:

  * `get_connection()`: Establishes a connection to the PostgreSQL database.
  * `load_movies()`: Fetches all records from the `public.movies` table into a Pandas DataFrame.

## 🏃 Usage

The core analysis and modeling workflow is contained within the Jupyter notebook.

### Run the Analysis

1.  Start the Jupyter Lab or Notebook server from the project root:
    ```bash
    jupyter notebook
    # OR
    jupyter lab
    ```
2.  Navigate to the `notebook/` directory and open **`analysis_and_modeling.ipynb`**.
3.  Execute the cells sequentially to:
      * Load data from the PostgreSQL database.
      * Perform Exploratory Data Analysis (EDA).
      * Preprocess the data (e.g., handling missing values, encoding categorical features).
      * Train the Linear Regression model.
      * Evaluate model performance using metrics like R², MAE, and MSE.
      * Review potential future improvements.

## 💻 Dependencies

The primary libraries used in this project are:

| Library | Purpose |
| :--- | :--- |
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `scikit-learn` (`sklearn`) | Machine learning modeling and utilities |
| `statsmodels` | Statistical modeling |
| `psycopg` | PostgreSQL database adapter |
| `python-dotenv` | Loading environment variables from `.env` file |

*(This list is sourced from `requirements.txt`)*

-----

## 💡 Future Improvements

Potential areas for future work include:

1.  **Advanced Modeling:** Implementing more complex models such as **Random Forests** or **Gradient Boosting** to capture non-linear relationships.
2.  **Feature Engineering:** Creating interaction terms (e.g., `runtime` x `genre`) or using polynomial features.
3.  **Model Regularization:** Applying **Lasso** or **Ridge** regression to prevent overfitting and identify the most important predictors.