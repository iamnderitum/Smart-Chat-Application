"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Example Data
user_profiles =  pd.DataFrame({
    "course_id":[1,2,3],
    "preferences":[
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 0]
    ]
})

course_profiles = pd.DataFrame({
    "course_id": [1, 2, 3],
    "features": [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 0]
    ]
})

def recommend_courses(user_id):
    user_vector = user_profiles[user_profiles["user_id"]  == user_id]["preferences"].value[0]
    similarities = cosine_similarity([user_vector], course_profiles["features"].tolist())
    recommendations = course_profiles.iloc[similarities.argsort()[0][-3:]]['course_id'].tolist()
    return recommendations

"""