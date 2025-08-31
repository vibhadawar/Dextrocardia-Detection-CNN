*** Dextrocardia Detection using Deep Learning***

 **Project Overview**

This project uses a Convolutional Neural Network (CNN) to detect Dextrocardia (a rare heart condition where the heart is positioned on the right side of the chest) from chest X-ray images.

1.Built using TensorFlow/Keras

2. Preprocessed medical image dataset
 
3.Evaluated using accuracy, precision, recall, F1-score

4.Deployed with Flask + Ngrok for testing on Google Colab

⚙Features

->Image preprocessing (resizing, grayscale conversion, normalization)

->CNN model with multiple Conv + Pooling layers

->Training & validation on medical dataset

->Model evaluation using classification report

->Flask-based web app to upload & predict X-ray images

* Tech Stack / Libraries

NumPy, Pandas → Data handling

Matplotlib, Seaborn → Visualization

TensorFlow / Keras → Deep Learning model

scikit-learn → Evaluation metrics

Flask, flask-ngrok → Web deployment

* Project Workflow

Data Preprocessing → Load and prepare X-ray images

Model Design → CNN layers for feature extraction & classification

Training → Compile & fit model on dataset

Evaluation → Accuracy, classification report, confusion matrix

Deployment → Flask app (with ngrok for Colab testing)

📊 Results

Accuracy: 90%

Precision/Recall/F1-score: <img width="522" height="193" alt="image" src="https://github.com/user-attachments/assets/99b29dd6-5a98-4a43-aada-a78f32f8b783" />


Model successfully classifies images into:

Normal

Dextrocardia
