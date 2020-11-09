import itertools

import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_confusion_matrix(confusion, classes, normalize=False, cmap=plt.cm.Reds):
    """Plot a confusion matrix

    Args:
        confusion: confusion matrix computed by sklearn
        class: array of class names
        normalize: whether to normalize the counts in
                   the confusion matrix
        cmap: matplotlib color map
    """
    mpl.style.use('seaborn-ticks')
    fig = plt.figure(figsize=(20,10))

    plt.imshow(confusion, interpolation='nearest', cmap=cmap)
    plt.title("Confusion Matrix")
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = confusion.max() / 2.
    for i, j in itertools.product(range(confusion.shape[0]), range(confusion.shape[1])):
        plt.text(
            j, i, format(confusion[i, j], fmt),
            horizontalalignment="center",
            color="white" if confusion[i, j] > thresh else "black"
        )

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

