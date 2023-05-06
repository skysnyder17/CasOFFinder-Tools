import pandas as pd

# Step 2: Extract features from off-target sites
def extract_features(off_target_sites_file):
    data = pd.read_csv(off_target_sites_file, delimiter='\t')
    features = []
    for index, row in data.iterrows():
        feature = []
        # Extract relevant information (e.g., chromatin accessibility, DNA methylation) from off-target site
        
        # Example: Extract chromatin accessibility score
        chromatin_accessibility = row['Chromatin_Accessibility']
        feature.append(chromatin_accessibility)
        
        # Example: Extract DNA methylation level
        dna_methylation = row['DNA_Methylation']
        feature.append(dna_methylation)
        
        # Add additional features as needed
        
        # Add the extracted features to the feature list
        features.append(feature)
    return features

# Main script
if __name__ == '__main__':
    # Off-target sites file
    off_target_sites_file = 'off_target_sites.txt'
    
    # Step 2: Extract features
    features = extract_features(off_target_sites_file)
    print(f"Extracted features: {features}")
