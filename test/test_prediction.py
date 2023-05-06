import pandas as pd

# Step 4: Evaluate the model on new off-target sites
def evaluate_model(model_file, new_features_file):
    # Load the trained model
    model = pd.read_pickle(model_file)

    # Load the new off-target site features
    new_features = pd.read_csv(new_features_file)

    predictions = model.predict(new_features)
    return predictions

# Main script
if __name__ == '__main__':
    # Trained model file
    model_file = 'trained_model.pkl'

    # New off-target site features file
    new_features_file = 'new_off_target_features.csv'

    # Step 4: Evaluate the model on new off-target sites
    predictions = evaluate_model(model_file, new_features_file)
    print(f"Predictions: {predictions}")
