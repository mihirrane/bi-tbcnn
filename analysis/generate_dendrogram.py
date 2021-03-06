from scipy.cluster.hierarchy import dendrogram, linkage
import random
from matplotlib.pyplot import show
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.colors as colors
from sklearn.decomposition import PCA
from collections import Counter
max_d = 62


with open("./test_vectors/cpp_vectors_10D_tbcnn_def_use.txt", "r") as f:
	cpp_data = f.readlines()

with open("./test_vectors/cpp_vectors_10D_tbcnn_def_use.txt", "r") as f:
	java_data = f.readlines()

data = java_data
# data.extend(java_data)
labels = []


bubblesort_vectors = []
mergesort_vectors = []
quicksort_vectors = []
linkedlist_vectors = []
queue_vectors = []
stack_vectors = []
heap_vectors = []
bfs_vectors = []
dfs_vectors = []
knapsack_vectors = []

cpp_bubblesort_vectors = []
cpp_mergesort_vectors = []
cpp_quicksort_vectors = []
cpp_linkedlist_vectors = []
cpp_queue_vectors = []
cpp_stack_vectors = []
cpp_heap_vectors = []
cpp_bfs_vectors = []
cpp_dfs_vectors = []
cpp_knapsack_vectors = []


java_bubblesort_vectors = []
java_mergesort_vectors = []
java_quicksort_vectors = []
java_linkedlist_vectors = []
java_queue_vectors = []
java_stack_vectors = []
java_heap_vectors = []
java_bfs_vectors = []
java_dfs_vectors = []
java_knapsack_vectors = []



vectors_all = []
labels_all = []
label_index = []
lang_index = []
cpp_vectors = []
java_vectors = []
lang_labels = []
cpp_label_index = []
java_label_index = []
cpp_labels_all = []
java_labels_all = []

# for line in cpp_data:
# 	l = line.replace("\n","").strip()
# 	splits = l.split(" ")
# 	label = splits[0]
# 	vector = splits[1:len(splits)]
# 	vector_f = [float(i) for i in vector]

# 	# labels.append(label)
# 	if label == "bfs":
# 		bfs_vectors.append(vector_f)
# 		label_index.append(1)
# 		cpp_label_index.append(1)
# 		cpp_bfs_vectors.append(vector_f)
# 	if label == "dfs":
# 		dfs_vectors.append(vector_f)
# 		label_index.append(2)
# 		cpp_label_index.append(2)
# 		cpp_dfs_vectors.append(vector_f)
# 	if label == "bubblesort":
# 		bubblesort_vectors.append(vector_f)
# 		cpp_bubblesort_vectors.append(vector_f)
# 		label_index.append(3)
# 		cpp_label_index.append(3)
# 	if label == "quicksort":
# 		quicksort_vectors.append(vector_f)
# 		cpp_quicksort_vectors.append(vector_f)
# 		label_index.append(4)
# 		cpp_label_index.append(4)
# 	if label == "mergesort":
# 		mergesort_vectors.append(vector_f)
# 		cpp_mergesort_vectors.append(vector_f)
# 		label_index.append(5)
# 		cpp_label_index.append(5)
# 	if label == "heap":
# 		heap_vectors.append(vector_f)
# 		cpp_heap_vectors.append(vector_f)
# 		label_index.append(6)
# 		cpp_label_index.append(6)
# 	if label == "linkedlist":
# 		linkedlist_vectors.append(vector_f)
# 		cpp_linkedlist_vectors.append(vector_f)
# 		label_index.append(7)
# 		cpp_label_index.append(7)
# 	if label == "queue":
# 		queue_vectors.append(vector_f)
# 		cpp_queue_vectors.append(vector_f)
# 		label_index.append(8)
# 		cpp_label_index.append(8)
# 	if label == "stack":
# 		stack_vectors.append(vector_f)
# 		cpp_stack_vectors.append(vector_f)
# 		label_index.append(9)
# 		cpp_label_index.append(9)
# 	if label == "knapsack":
# 		knapsack_vectors.append(vector_f)
# 		cpp_knapsack_vectors.append(vector_f)
# 		label_index.append(10)
# 		cpp_label_index.append(10)

# 	cpp_vectors.append(vector_f)
# 	# if label != "knapsack":
# 	vectors_all.append(vector_f)
# 	labels_all.append(label+"_cpp")
# 	lang_index.append(1)
# 	cpp_labels_all.append(label)
# 	lang_labels.append("cpp")
	
for line in java_data:
	l = line.replace("\n","").strip()
	splits = l.split(" ")
	label = splits[0]
	vector = splits[1:len(splits)]
	vector_f = [float(i) for i in vector]

	# labels.append(label)
	if label == "bfs":
		bfs_vectors.append(vector_f)
		java_bfs_vectors.append(vector_f)
		label_index.append(11)
		java_label_index.append(11)
	if label == "dfs":
		dfs_vectors.append(vector_f)
		java_dfs_vectors.append(vector_f)
		label_index.append(12)
		java_label_index.append(12)
	if label == "bubblesort":
		bubblesort_vectors.append(vector_f)
		java_bubblesort_vectors.append(vector_f)
		label_index.append(13)
		java_label_index.append(13)
	if label == "quicksort":
		quicksort_vectors.append(vector_f)
		java_quicksort_vectors.append(vector_f)
		label_index.append(14)
		java_label_index.append(14)
	if label == "mergesort":
		mergesort_vectors.append(vector_f)
		java_mergesort_vectors.append(vector_f)
		label_index.append(15)
		java_label_index.append(15)
	if label == "heap":
		heap_vectors.append(vector_f)
		java_heap_vectors.append(vector_f)
		label_index.append(16)
		java_label_index.append(16)
	if label == "linkedlist":
		linkedlist_vectors.append(vector_f)
		java_linkedlist_vectors.append(vector_f)
		label_index.append(17)
		java_label_index.append(17)
	if label == "queue":
		queue_vectors.append(vector_f)
		java_queue_vectors.append(vector_f)
		label_index.append(18)
		java_label_index.append(18)
	if label == "stack":
		stack_vectors.append(vector_f)
		java_stack_vectors.append(vector_f)
		label_index.append(19)
		java_label_index.append(19)
	if label == "knapsack":
		knapsack_vectors.append(vector_f)
		java_knapsack_vectors.append(vector_f)
		label_index.append(20)
		java_label_index.append(20)

	java_vectors.append(vector_f)
	# if label != "knapsack":
	vectors_all.append(vector_f)
	labels_all.append(label+"_java")
	lang_index.append(2)
	java_labels_all.append(label)
	lang_labels.append("java")


# labels = ["bfs","dfs","bublesort","quicksort","mergesort","heap","linkedlist", "queue","stack","knapsack"]
vectors = []
print("aaaaa : " + str(len(dfs_vectors)))
# vectors.append(random.choice(bfs_vectors))
# vectors.append(random.choice(dfs_vectors))
# vectors.append(random.choice(bubblesort_vectors))
# vectors.append(random.choice(quicksort_vectors))
# vectors.append(random.choice(mergesort_vectors))
# vectors.append(random.choice(heap_vectors))
# vectors.append(random.choice(linkedlist_vectors))
# vectors.append(random.choice(queue_vectors))
# vectors.append(random.choice(stack_vectors))
# vectors.append(random.choice(knapsack_vectors))

samples = 10
vectors.extend(random.sample(bfs_vectors,samples))
vectors.extend(random.sample(dfs_vectors,samples))
vectors.extend(random.sample(bubblesort_vectors,samples))
vectors.extend(random.sample(quicksort_vectors,samples))
vectors.extend(random.sample(mergesort_vectors,samples))
vectors.extend(random.sample(heap_vectors,samples))
vectors.extend(random.sample(linkedlist_vectors,samples))
vectors.extend(random.sample(queue_vectors,samples))
vectors.extend(random.sample(stack_vectors,samples))
vectors.extend(random.sample(knapsack_vectors,samples))



labels.extend(["bfs" for i in range(0,samples)])
labels.extend(["dfs" for i in range(0,samples)])
labels.extend(["bublesort" for i in range(0,samples)])
labels.extend(["quicksort" for i in range(0,samples)])
labels.extend(["mergesort" for i in range(0,samples)])
labels.extend(["heap" for i in range(0,samples)])
labels.extend(["linkedlist" for i in range(0,samples)])
labels.extend(["queue" for i in range(0,samples)])
labels.extend(["stack" for i in range(0,samples)])
labels.extend(["knapsack" for i in range(0,samples)])

print(labels)
print("length of labels : " + str(len(labels)))
# print vectors
cpp_label_dict = {
	1: "bfs_cpp",
	2: "dfs_cpp",
	3: "bubblesort_cpp",
	4: "quicksort_cpp",
	5: "mergesort_cpp",
	6: "heap_cpp",
	7: "linkedlist_cpp",
	8: "queue_cpp",
	9: "stack_cpp",
	10: "knapsack_cpp",
}
java_label_dict = {
	11: "bfs_java",
	12: "dfs_java",
	13: "bubblesort_java",
	14: "quicksort_java",
	15: "mergesort_java",
	16: "heap_java",
	17: "linkedlist_java",
	18: "queue_java",
	19: "stack_java",
	20: "knapsack_java"
}

pca = PCA(n_components=2)
vectors_all_pca = pca.fit_transform(vectors_all)

unique = list(set(label_index))
colors_c = [plt.cm.jet(float(i)/max(unique)) for i in unique]

for i, u in enumerate(unique):
    xi = [vectors_all_pca[:,0][j] for j  in range(len(vectors_all_pca[:,0])) if label_index[j] == u]
    yi = [vectors_all_pca[:,1][j] for j  in range(len(vectors_all_pca[:,1])) if label_index[j] == u]
    plt.scatter(xi, yi, c=colors_c[i], label=java_label_dict[u])

plt.legend(bbox_to_anchor=(1,1), loc=1, ncol=3)
plt.title('Visualization of java programs (vectors extracted from D-TBCNN)')
plt.show()

def augmented_dendrogram(*args, **kwargs):

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        for i, d in zip(ddata['icoord'], ddata['dcoord']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            plt.plot(x, y, 'ro')
            plt.annotate("%.3g" % y, (x, y), xytext=(0, -8),
                         textcoords='offset points',
                         va='top', ha='center')

    return ddata

def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (10 program each class)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

print("leng of vectors : " + str(len(vectors)))

Z = linkage(vectors_all, "ward")
# print(Z)

# fancy_dendrogram(Z, labels= labels)
# dendrogram(Z,truncate_mode='lastp',p=12,labels = labels, show_contracted=True)

ddata = fancy_dendrogram(Z,truncate_mode='lastp',labels = labels_all,max_d=max_d)


# Retrieving cluster
clusters = fcluster(Z, max_d, criterion='distance')
print(clusters)
print("length of cluster : " + str(len(clusters)))

# cluster_indexes = [x for x in range(0,11)]
from collections import defaultdict
result = defaultdict(list)
for k, v in zip(clusters, labels_all):
	result[k].append(v)

for k,v in result.items():
	print("---------------------------")
	print("Number of programs : " + str(len(v)))
	print("Cluster %s - %s" % (str(k), str(v)))


show()
