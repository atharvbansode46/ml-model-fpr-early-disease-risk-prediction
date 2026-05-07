import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

try:
    # Load dataset
    data = pd.read_csv("dataset.csv")

    print("Dataset Loaded Successfully!\n")
    print(data.head())

    # Features and target
    X = data[["age", "bp", "sugar", "cholesterol", "heart_rate"]]
    y = data["risk"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100)

    model.fit(X_train, y_train)

    # Save model
    with open("disease_model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("\n✅ Model trained successfully!")
    print("✅ disease_model.pkl file created!")

except FileNotFoundError:
    print("❌ ERROR: dataset.csv file not found!")

except KeyError as e:
    print(f"❌ ERROR: Missing column in dataset -> {e}")

except Exception as e:
    print(f"❌ ERROR: {e}")