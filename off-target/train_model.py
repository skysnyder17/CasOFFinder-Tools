from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Step 3: Train the machine learning model
def train_model(features_file, labels_file):
    # Load features and labels from files
    features = pd.read_csv(features_file)
    labels = pd.read_csv(labels_file)
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    return model, accuracy

# Main script
if __name__ == '__main__':
    # Features and labels files
    features_file = 'off_target_features.csv'
    labels_file = 'off_target_labels.csv'
    
    # Step 3: Train the model
    model, accuracy = train_model(features_file, labels_file)
    print(f"Model trained with accuracy: {accuracy}")
