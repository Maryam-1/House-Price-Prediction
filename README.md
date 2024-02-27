# House Price Prediction

## Overview
This project focuses on predicting house prices by scraping data from the Zoopla website using a Python script with BeautifulSoup. The UK market data was thoroughly explored, cleaned, and preprocessed before being utilized to train machine learning models. The project culminates in a web application built using Flask, showcasing the predictive capabilities on a user-friendly interface.

## Objective
To develop a robust model that accurately predicts house prices based on various features extracted from the Zoopla website, and to deploy this model in a web application for easy access and use by end-users.

## Data Collection
- Data was scraped from the Zoopla website using BeautifulSoup.
- The dataset includes features such as location, property type, number of bedrooms, etc.
- A custom Python script automated the data collection process, ensuring a comprehensive dataset for analysis.

## Data Processing
- The dataset underwent extensive cleaning to remove inconsistencies and missing values.
- Feature engineering was applied to extract and select relevant features for the prediction model.
- Data preprocessing techniques were employed to prepare the dataset for machine learning algorithms.

## Model Development and Evaluation
- Explored various machine learning models, including Random Forest and Artificial Neural Networks (ANN), to find the best predictor for house prices.
- Fine-tuned model parameters to optimize performance.
- Random Forest was identified as the more accurate model for predicting house prices in this context.
- Here's a comprehensive summary of the methodologies and key findings:

#### Neural Networks

Preprocessing and Transformation: The data underwent several preprocessing steps, including outlier removal, normalization, and transformation. A significant transformation applied was the Box-Cox transformation, which helped in stabilizing variance and making the data more normally distributed.

Model Configuration: The Neural Network model was built with a specific architecture designed to address the regression problem of predicting house prices. The model included dense layers with ReLU activation functions, a method to prevent overfitting through dropout layers, and optimization techniques.

Performance and Evaluation: The performance of the Neural Network was measured using Mean Square Error (MSE) and Root Mean Square Error (RMSE). The report indicates an improvement in model performance after the Box-Cox transformation, showcasing a significant reduction in both MSE and RMSE values.

#### Random Forest

Model Explanation: Random Forest is described as an ensemble learning method that combines multiple decision trees to improve prediction accuracy. The model operates by building numerous decision trees during training and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

Configuration: The Random Forest model used in the study was configured with 100 estimators, indicating it comprised 100 distinct decision trees. A fixed random state was used to ensure repeatability of the results.

Evaluation: Similar to the Neural Network, the Random Forest model's predictive capability was evaluated using the Mean Square Error (MSE) metric.

#### Key Findings and Insights

The application of the Box-Cox transformation significantly improved the Neural Network model's performance, as evidenced by the reduction in MSE and RMSE values.
Both models demonstrated the importance of preprocessing and the right configuration to achieve accurate predictions in house price prediction tasks.
The report provides a comparative analysis of the models' performance, though specific details on which model performed better or insights into their comparative accuracy were not explicitly mentioned in the provided excerpts.

The Random Forest model, in particular, showed superior performance with an R^2 of 0.99, indicating a nearly perfect fit to the data. This suggests that including a broader range of property features can significantly improve price prediction accuracy.

#### Overall Implications

This detailed examination underscores the complexity of predictive modeling in real estate and the efficacy of advanced machine learning techniques in tackling such problems. The methodology outlined for both Neural Networks and Random Forest models showcases a rigorous approach to model selection, configuration, and evaluation, emphasizing the critical role of data preprocessing and transformation in enhancing model performance.


## Web Application
- Developed a Flask web application to deploy the predictive model.
- The application provides a user-friendly interface for users to input property details and receive price predictions.
- Implemented features for real-time data interaction and visualization.

## Technologies Used
- **Data Collection & Processing:** Python, BeautifulSoup
- **Machine Learning:** Scikit-learn, TensorFlow
- **Web Application:** Flask
- **Other Tools:** Pandas, NumPy

## Challenges Faced
- Overcoming the complexities of web scraping dynamic websites.
- Ensuring the robustness and reliability of the predictive model.
- Developing a user-friendly web interface that accommodates non-technical users.

## Future Work
- Enhance the model by incorporating more diverse datasets and advanced features.
- Improve the web application's UI/UX for better user engagement.
- Explore deployment options for scaling and accessibility.
