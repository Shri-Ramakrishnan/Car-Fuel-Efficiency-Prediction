# Car Fuel Efficiency Prediction System

## Project Goal
Predict the fuel efficiency (MPG) of a car using technical and categorical parameters from the Auto MPG dataset.

## Dataset
- Source: UCI Auto MPG dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data)
- Target: mpg
- Features: cylinders, displacement, horsepower, weight, acceleration, model_year, origin

## Workflow
1. Data Collection: Download dataset automatically.
2. Data Cleaning: Handle missing values, convert types, drop irrelevant columns, map origin.
3. EDA: Summary stats, visualizations (distribution, correlation heatmap, pairplot, boxplots).
4. Feature Engineering: Encode origin, scale features, optional derived feature.
5. Modeling: Train LinearRegression, Ridge, RandomForest, XGBoost.
6. Evaluation: Compare models with MSE, RMSE, MAE, R²; plots for best model.
7. Saving: Model as joblib, cleaned data as CSV.

## Instructions to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run notebook: Open `notebooks/fuel_efficiency_analysis.ipynb` in Jupyter and execute all cells.
3. Optional: Run Streamlit app: `streamlit run app/streamlit_app.py`

## Outputs
- Notebook: `notebooks/fuel_efficiency_analysis.ipynb`
- Model: `models/mpg_predictor.joblib`
- Cleaned Data: `data/auto_mpg_cleaned.csv`
- App: `app/streamlit_app.py`
