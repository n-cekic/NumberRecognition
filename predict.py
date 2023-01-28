from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

import numpy as np

from Image import ImagePreprocessing as ip

digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.1, shuffle=False
)


# Learn the digits on the train subset
clf.fit(X_train, y_train)


def predict(image_path):
    image = ip()
    image.open(image_path)
    image.to_gray()
    image.locate_content()
    image.pixelate()
    image.invert()
    image = [int(x / 16) for x in image.image.getdata()]
    image = np.array(image)

    # Predict the value of the digit on the test subset
    predicted = clf.predict(image.reshape(1, -1))
    return predicted[0]
