import numpy as np
from sklearn import datasets
import sklearn
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D


# class PCA():
#     def calculate_covariance_matrix(self, X, Y=None):
#         # Calculate conv
#         m = X.shape[0]
#         X = X - np.mean(X, axis=0)
#         Y = X if Y == None else Y - np.mean(Y, axis=0)
#         return 1 / m * np.matmul(X.T, Y)

#     def transform(self, X, n_components):

#         covariance_matrix = self.calculate_covariance_matrix(X)
#         eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

#         idx = eigenvalues.argsort()[::-1]
#         eigenvectors = eigenvectors[:, idx]
#         eigenvectors = eigenvectors[:, :n_components]

#         # Transform
#         return np.matmul(X, eigenvectors)


# def main():

#     # Demo of how to reduce the dimensionality of the data to two dimension
#     # and plot the results.

#     # Load the dataset
#     data = datasets.load_digits()
#     X = data.data
#     # print(type(X))
#     print(np.shape(X))
#     print(X)
#     y = data.target
#     # print(type(y))
#     print(np.shape(y))
#     print(y)

#     # Project the data onto the 2 primary principal components
#     X_trans = PCA().transform(X, 2)

#     x1 = X_trans[:, 0]
#     x2 = X_trans[:, 1]

#     cmap = plt.get_cmap('viridis')
#     colors = [cmap(i) for i in np.linspace(0, 1, len(np.unique(y)))]

#     class_distr = []
#     # Plot the different class distributions
#     for i, l in enumerate(np.unique(y)):
#         _x1 = x1[y == l]
#         _x2 = x2[y == l]
#         _y = y[y == l]
#         class_distr.append(plt.scatter(_x1, _x2, color=colors[i]))

#     # Add a legend
#     plt.legend(class_distr, y, loc=1)

#     # Axis labels
#     plt.suptitle("PCA Dimensionality Reduction")
#     plt.title("Digit Dataset")
#     plt.xlabel('Principal Component 1')
#     plt.ylabel('Principal Component 2')
#     plt.savefig("1.jpg")


def main():
    pca = sklearn.decomposition.PCA(n_components=3)
    data = datasets.load_digits()
    X = data.data
    y = data.target
    # pca.fit(X)
    # output = pca.score(X)
    # print(output)
    # print(np.shape(output))
    # output = pca.fit_transform(X)
    # print(output)
    X_trans = pca.fit_transform(X)
    x1 = X_trans[:, 0]
    x2 = X_trans[:, 1]
    x3 = X_trans[:, 2]
    # print(type(x3))
    # print(len(x3))
    # print(len(x3[0]))

    cmap = plt.get_cmap('viridis')
    colors = [cmap(i) for i in np.linspace(0, 1, len(np.unique(y)))]
    # print(colors)
    # print("####################")

    # class_distr = []

    # mpl_toolkits.mplot3d.axes3d
    ax = plt.subplot(111, projection='3d')
    # ax = plt.subplot(111)
    # Plot the different class distributions
    for i, l in enumerate(np.unique(y)):
        _x1 = x1[y == l]
        _x2 = x2[y == l]
        _x3 = x3[y == l]
        _y = y[y == l]
        # class_distr.append(plt.(_x1, _x2,, color=colors[i]))
        ax.scatter(_x1, _x2, _x3, color=colors[i])

    # Add a legend
    # plt.legend(class_distr, y, loc=1)

    # Axis labels
    plt.suptitle("PCA Dimensionality Reduction")
    plt.title("Digit Dataset")
    # plt.xlabel('Principal Component 1')
    # plt.ylabel('Principal Component 2')
    # plt.savefig("2.jpg")

    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')

    # plt.show()
    plt.savefig("3d.jpg")


if __name__ == "__main__":
    main()
