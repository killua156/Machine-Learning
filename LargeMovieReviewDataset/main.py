import os
import pandas as pd

# Define folder paths relative to the script
neg_path = r"C:\Users\jeanr\OneDrive\Desktop\Machine Learning\Machine-Learning\LargeMovieReviewDataset\train\neg"
pos_path = r"C:\Users\jeanr\OneDrive\Desktop\Machine Learning\Machine-Learning\LargeMovieReviewDataset\train\pos"


# Function to read all text files in a folder
def load_reviews(folder, label):
    reviews = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            reviews.append((file.read(), label))
    return reviews

# Load negative and positive reviews
neg_reviews = load_reviews(neg_path, "negative")
pos_reviews = load_reviews(pos_path, "positive")

# Combine and create DataFrame
df = pd.DataFrame(neg_reviews + pos_reviews, columns=["review", "label"])

# Save to CSV in the current directory
csv_path = "./reviews.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file '{csv_path}' created successfully!")
