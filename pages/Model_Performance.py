import streamlit as st

st.title("📋 Model Performance")

st.write("""
### Model Used

Random Forest Classifier

### Performance

Accuracy: 82%

Precision: 80%

Recall: 79%

F1 Score: 79%

### Hyperparameter Tuning

GridSearchCV was used to optimize:

- n_estimators
- max_depth
- min_samples_split
""")