import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. Load Processed Data
# ==========================================

data = pd.read_csv("processed_data.csv")

print("Data loaded successfully!")
print("Dataset shape:", data.shape)
print("\nColumns:")
print(data.columns.tolist())


# ==========================================
# 2. Separate Features and Target
# ==========================================

X = data[["RM", "LSTAT", "PTRATIO"]]
y = data["MEDV"]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print("MEDV")


# ==========================================
# 3. Train / Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining shape:", X_train.shape)
print("Testing shape:", X_test.shape)


# ==========================================
# 4. Define Models
# ==========================================

models = {

    "Linear Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ]),

    "Ridge Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=200,
        random_state=42
    )
}


# ==========================================
# 5. Train and Evaluate Models
# ==========================================

results = {}

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5
    r2 = r2_score(y_test, predictions)

    results[name] = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

    print(f"{name}")
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")


# ==========================================
# 6. Compare Models
# ==========================================

results_df = pd.DataFrame(results).T

print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

print(results_df)


# ==========================================
# 7. Select Best Model
# ==========================================

best_model_name = results_df["RMSE"].idxmin()

best_model = models[best_model_name]

print("\nBest Model:")
print(best_model_name)


# ==========================================
# 8. Save Final Model
# ==========================================

joblib.dump(best_model, "model.pkl")

print("\nFinal model saved successfully!")
print("File: model.pkl")