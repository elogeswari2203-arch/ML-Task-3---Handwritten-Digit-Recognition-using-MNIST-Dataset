## **TASK 3 - Handwritten Digit Recognition (MNIST)**



1\. What is TensorFlow?



TensorFlow is a Deep Learning library.



Used for:

\- Neural Networks

\- Image Recognition

\- AI Models

\- Deep Learning  



Import:



import tensorflow as tf



\--------------------------------------------------



2\. What is MNIST?



MNIST is a handwritten digit dataset.



Contains:



Digits:

0 1 2 3 4 5 6 7 8 9



Used for:

\- Image classification

\- Deep learning practice



\--------------------------------------------------



3\. Import MNIST Dataset



from tensorflow.keras.datasets import mnist



\--------------------------------------------------



4\. Load Dataset



(X\_train, y\_train), (X\_test, y\_test) = mnist.load\_data()



Meaning:



X\_train = training images

y\_train = training labels



X\_test = testing images

y\_test = testing labels



\--------------------------------------------------



5\. What is Training Data?



Data used for learning.



Example:



Image of 5 -> Label 5



Model learns this pattern.



\--------------------------------------------------



6\. What is Testing Data?



Used to check model performance.



Model sees new images.



\--------------------------------------------------



7\. X\_train.shape



Output:



(60000, 28, 28)



Meaning:



60000 images



Each image:

28 rows

28 columns



\--------------------------------------------------



8\. y\_train.shape



Output:



(60000,)



Meaning:



60000 labels



One label for each image.



\--------------------------------------------------



9\. Display Image



plt.imshow(X\_train\[0], cmap='gray')



Meaning:



Show first image.



\--------------------------------------------------



10\. cmap='gray'



Displays image in grayscale.



Black = low pixel value



White = high pixel value



\--------------------------------------------------



11\. Display Label



plt.title(f"Label: {y\_train\[0]}")



Shows actual digit.



Example:



Label: 5



\--------------------------------------------------



12\. Show Graph Window



plt.show()



Displays image window.



\--------------------------------------------------



13\. Important Concept



Image = Input



Label = Answer



In ML:



Input -> Features



Answer -> Target



\--------------------------------------------------



14\. Dataset Structure



X\_train = Images



y\_train = Labels



Example:



Image -> 5



Label -> 5



Image -> 0



Label -> 0



\--------------------------------------------------



15\. Final Meaning



Load handwritten digit images and their answers,

then display one image and its label.

