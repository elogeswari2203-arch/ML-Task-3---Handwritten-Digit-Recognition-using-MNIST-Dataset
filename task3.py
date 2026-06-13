# Import libraries
import tensorflow as tf
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Display dataset shapes
print("Training Images Shape:", X_train.shape)
print("Training Labels Shape:", y_train.shape)

# Display first image
plt.imshow(X_train[10], cmap='gray')

# Show image title
plt.title(f"Label: {y_train[10]}")

# Display image
plt.show()

print(y_train[0])
print(X_train[0].shape)