from DataStructures.MinHeap import MinHeap
import HelperClasses.GenerateArrays as genArrays
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def HeapSort(array):
    '''
    This function uses the MinHeap datastructure in order to sort an array

    Parameters : 
        array : [int]
            The array to be sorted

    Returns :
        sorted_array : [int]
            The array that has been sorted
        swap_count : int
            The number of swaps that were performed while sorting
    '''

    minheap = MinHeap(array)
    sorted_array = []

    while minheap.getHeapSize() > 0:
        sorted_array.append(minheap.deleteItem(0))

    return sorted_array, minheap.swap_count

if __name__ == '__main__':

    number_to_sort = 20
    starting_size = 2

    array_lengths = []
    time_spent = []
    swap_counts = []

    for i in range(1,number_to_sort):
        array_length = (starting_size)**i
        for j in range(0,5):
            array = genArrays.generate_random_array(array_length=array_length,min_value=0, max_value=array_length*3)
            start = time.time()
            sorted_array, swap_count = HeapSort(array=array)
            end = time.time()
            array_lengths.append(array_length)
            time_spent.append(end-start)
            swap_counts.append(swap_count)

    dictionary = {
        "Array Length": array_lengths,
        "Time Spent In Seconds": time_spent,
        "Swap Count": swap_counts
    }

    dataframe = pd.DataFrame.from_dict(dictionary)
    print(dataframe.head(10))

    fig, axes = plt.subplots(ncols=2, sharey=False)
    fig.set_figwidth(10)
    bright_palette = palette=sns.hls_palette(h=.5)
    sns.set_theme(style="whitegrid", palette=bright_palette)
    sns.lineplot(data=dataframe, x="Array Length", y="Time Spent In Seconds", ax=axes[0], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Time Spent In Seconds", ax=axes[0], color=bright_palette[1])
    sns.lineplot(data=dataframe, x="Array Length", y="Swap Count", ax=axes[1], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Swap Count", ax=axes[1], color=bright_palette[1])

    fig.canvas.manager.set_window_title('Heap Sort By Array Length')

    plt.tight_layout()
    plt.show()
