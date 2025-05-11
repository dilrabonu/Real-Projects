

# 🧠 Fashion MNIST Image Classification with CNN

This project uses a **Convolutional Neural Network (CNN)** to classify clothing images from the popular **Fashion MNIST** dataset using TensorFlow/Keras. The goal was to build a high-performing model for image classification and gain deep insights into deep learning model building, training, and evaluation.

---

## 🗂️ Dataset

- **Source**: [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist)
- **Format**: 28x28 grayscale images
- **Classes** (0–9):
  - 0 = T-shirt/top
  - 1 = Trouser
  - 2 = Pullover
  - 3 = Dress
  - 4 = Coat
  - 5 = Sandal
  - 6 = Shirt
  - 7 = Sneaker
  - 8 = Bag
  - 9 = Ankle boot

---

## 📌 Project Structure

- `fashion-mnist_train.csv`: Training set (60,000 samples)
- `fashion-mnist_test.csv`: Test set (10,000 samples)
- `Fashion_MNIST_CNN.ipynb`: Complete notebook with training, evaluation, visualization, and model saving

---

## 🚀 Model Architecture

```python
Sequential([
    Conv2D(32, kernel_size=3, activation='relu'),
    MaxPooling2D(pool_size=2),
    
    Conv2D(64, kernel_size=3, activation='relu'),
    MaxPooling2D(pool_size=2),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

Optimizer: Adam

Loss: Categorical Crossentropy

Metrics: Accuracy

Batch Size: 64

Epochs: 10

📈 Results
Metric	Score
Final Train Accuracy	93.3%
Final Validation Accuracy	91.9%
Final Test Accuracy	92.8%

✅ Model Saved: fashion_mnist_cnn_model.h5

✅ Confusion Matrix plotted and analyzed

🧠 Key Learnings
Importance of normalizing pixel values

How CNN layers capture spatial features

Value of visualizing accuracy curves and confusion matrix

Balanced architecture + regularization improves generalization

End-to-end training and evaluation on real-world-like image data

📌 Future Improvements
Integrate Grad-CAM for model explainability

Deploy the model using Streamlit or Flask API

Experiment with data augmentation for better generalization

🛠️ Technologies Used
Python 🐍

TensorFlow & Keras

Pandas, NumPy, Matplotlib

Scikit-learn

Kaggle Notebooks

👩‍💻 Author
Dilrabo Khidirova
Master’s Student in Software Engineering & AI
Aspiring Machine Learning Engineer | Kaggle Practitioner | AI Storyteller


![image](https://github.com/user-attachments/assets/5a85dd26-c158-4721-8121-9653e739f970)

https://www.kaggle.com/code/dilrabonu/fashion-mnist
