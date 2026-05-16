import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load city dataset
cities = pd.read_csv("cities.csv")

features = cities[[
    "cost",
    "safety",
    "internet",
    "climate",
    "nightlife"
]]

# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)

# Train KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
cities["cluster"] = kmeans.fit_predict(scaled_data)


def recommend_city(user_input):
    user_df = pd.DataFrame([user_input])

    user_scaled = scaler.transform(user_df)

    cluster = kmeans.predict(user_scaled)[0]

    matched = cities[cities["cluster"] == cluster]

    matched = matched.copy()

    matched["score"] = (
        abs(matched["cost"] - user_input["cost"]) +
        abs(matched["safety"] - user_input["safety"]) +
        abs(matched["internet"] - user_input["internet"]) +
        abs(matched["climate"] - user_input["climate"]) +
        abs(matched["nightlife"] - user_input["nightlife"])
    )

    matched = matched.sort_values(by="score")

    return matched.head(3).to_dict(orient="records")