from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pickle

word_classes = []
with open('to_plot/plot.pk', 'rb') as file:
    try:
        while True:
            word_classes.append(pickle.load(file))
    except EOFError:
        pass

pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(word_classes)

plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], marker='.')
plt.title('test plot')

plt.show()