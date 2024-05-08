# URL_AUTHENTICATION
URL Authentication Model Neural Network Optimized by Genetic Algorithms

Its a web application implementing a Multilayer Perceptron Neural Network optimized using genetic algorithms. Detect whether a domain name or URL is malicious by inputting a URL.

# Previews
![Screenshot 2024-04-27 213143](https://github.com/vijayakrishna03/URL_AUTHENTICATION/assets/162059453/ec8d2cde-79a6-434a-900a-1165a9c512ee)


The model contains two files
-Genetic algorithm which have the folling work

1. Begin by integrating the CSV dataset and removing any unnecessary columns.
2. Employ SMOTE to address imbalances in the dataset's class distribution.
3. Divide the dataset into training and testing sets using an 80:20 ratio.
4. Set up a Multilayer Perception model.
5. Implement Adam optimization and a binary cross-entropy loss function.
6. Establish a model callback to halt training when validation loss reaches 0.1.
7. Train the model over 10 epochs with a batch size of 256.
8. Validate the model's performance using 10 examples.
9. Apply a genetic algorithm to each iteration of the model.
10. Assess the fitness of each model iteration based on its accuracy.
11. Identify the best model within the population.
12. Save the top-performing model as a .h5 file output.

-Model generation is tge second important filw which have 

1. Start by integrating the CSV dataset and eliminating any redundant columns.
2. Apply SMOTE to equalize the class distribution within the dataset.
3. Segment the dataset into training and testing sets using an 80:20 ratio.
4. Set up a Multilayer Perceptron.
5. Employ Adam Optimization along with a Binary Cross Entropy Loss Function.
6. Set up a model callback to pause training when the validation loss reaches 0.1.
7. Train the model over 10 epochs with a batch size of 256.
8. Validate the model's outcomes using 10 examples.
9. Save the model as a .h5 file output.

# Usage
To build the source , you will need Python3 and pip installed on your system
```
cd url_auth
pip install -r requirements.txt
streamlit run app.py
```
Visit localhost:8501 to see the web application
