## 🪄 Machine Learning App

This is a simple machine learning application built using Streamlit and Scikit-learn. It allows users to input various penguin characteristics and then predicts the species of the penguin based on these inputs. The app uses a Random Forest classifier trained on a dataset of penguins.

### 💎 Features
* Data visualization: Visualize the relationship between body mass and bill length of penguins using a scatter plot.
* Model training: The app uses a Random Forest Classifier to predict the species of a penguin based on input features like bill length, bill depth, flipper length, body mass, island, and gender.
* Interactive inputs: Users can select input features such as the island of the penguin, bill size, flipper size, body mass, and gender using sliders and dropdowns in the sidebar.
* Predictions: The app makes predictions about the species of a penguin (Adelie, Chinstrap, or Gentoo) based on the user's inputs.

### 🚩 Requirements
To run this app locally, you will need the following Python libraries:

streamlit
pandas
numpy
scikit-learn

You can install the required libraries using pip:
pip install streamlit pandas numpy scikit-learn

### ✨ Running the App
To run the app locally, use the following command:
streamlit run app.py

### 💡 How it Works
* Data Loading: The app loads a penguin dataset from a URL and displays the raw data.
* Data Preparation: The dataset is preprocessed, including one-hot encoding for categorical variables like the island and gender of the penguin.
* Model Training: A Random Forest classifier is trained on the penguin dataset to predict the species based on the input features.
* Prediction: The model predicts the species of the penguin based on the user's input and displays the predicted probabilities for each species (Adelie, Chinstrap, Gentoo).
* Visualization: The app shows a scatter plot of bill length vs. body mass and provides an overview of the input penguin and the prepared data.

### Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://machinelearning.streamlit.app/)

### GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/app-starter-kit?quickstart=1)

### CSV-file

https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv

### 🌟 Credit
This project was built on top of the foundation provided by [@dataprofessor](https://github.com/dataprofessor/dp-machinelearning). Thank you for your work!

## Acknowledgements

This project was built on top of the foundation provided by [@username](https://github.com/username). Thank you for your work!

The original project can be found at [(https://github.com/dataprofessor/dp-machinelearning)]



