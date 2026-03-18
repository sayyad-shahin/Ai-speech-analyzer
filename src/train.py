from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

from dataset import load_data

X, y = load_data("data/ravdess")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "model.pkl")