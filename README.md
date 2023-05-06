
## CRISPR Off-Target Prediction for Gene Therapy

This is a Python implementation of an off-target prediction pipeline for CRISPR-based gene therapy using CasOFFinder and machine learning techniques.

### Overview

The pipeline consists of four main steps:

1. **Input guide RNA sequence**: Provide the guide RNA sequence of interest to target a specific genomic locus.

2. **Off-target site prediction**: Use CasOFFinder to identify potential off-target sites for the guide RNA sequence. Extract relevant features from the off-target sites, such as mismatch positions, number of mismatches, chromatin accessibility, and DNA methylation.

3. **Machine learning model training**: Train a machine learning model using the extracted features and labels (cleavage or no cleavage) for the off-target sites. The model can be tuned to optimize accuracy, specificity, or other performance metrics.

4. **Off-target site evaluation**: Use the trained machine learning model to predict the likelihood of off-target cleavage for new off-target sites based on their features. The predictions can be used to assess the safety and efficacy of CRISPR-based gene therapy approaches.

### Installation

To use this pipeline, you need to have the following dependencies installed:

- Python 3.x
- CasOFFinder (https://github.com/snugel/cas-offinder)
- scikit-learn (https://scikit-learn.org/stable/)
- pandas (https://pandas.pydata.org/)
- numpy (https://numpy.org/)

You can install the Python libraries using `pip` or `conda`:

```
pip install scikit-learn pandas numpy
```

### Usage

To use the pipeline, follow these steps:

1. Clone or download the repository to your local machine.

2. Open `off_target_prediction.py` in a Python IDE or text editor.

3. Modify the `input_sequence` variable to provide the guide RNA sequence of interest.

4. Run the script using a Python interpreter.

5. After the script completes, examine the generated files in the `output` directory. These files include:

- `off_target_sites.txt`: a list of potential off-target sites identified by CasOFFinder.
- `off_target_features.csv`: a table of extracted features for the off-target sites.
- `off_target_labels.csv`: a table of labels (cleavage or no cleavage) for the off-target sites.
- `trained_model.pkl`: a serialized machine learning model trained on the extracted features and labels.

6. To evaluate the model on new off-target sites, modify `test_prediction.py` and execute it using the trained model and the new off-target site features.


### References

- CasOFFinder: https://github.com/snugel/cas-offinder
- scikit-learn: https://scikit-learn.org/stable/
- pandas: https://pandas.pydata.org/
- numpy: https://numpy.org/
