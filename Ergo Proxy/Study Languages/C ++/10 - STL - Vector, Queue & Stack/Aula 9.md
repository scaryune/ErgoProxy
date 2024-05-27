# Priority Queue

A priority queue is a **special type of queue** in which each element is associated with a **priority value**. And, elements are served on the basis of their priority. That is, higher priority elements are served first.

However, if elements with the same priority occur, they are served according to their order in the queue.

**Assigning Priority Value**

Generally, the value of the element itself is considered for assigning the priority. For example,

The element with the highest value is considered the highest priority element. However, in other cases, we can assume the element with the lowest value as the highest priority element.

We can also set priorities according to our needs.

![the element with highest priority is removed from the priority queue](https://cdn.programiz.com/sites/tutorial2program/files/Introduction.png "Priority Queue")

Removing Highest Priority Element

---

### Difference between Priority Queue and Normal Queue

In a queue, the **first-in-first-out rule** is implemented whereas, in a priority queue, the values are removed **on the basis of priority**. The element with the highest priority is removed first.

---

## Implementation of Priority Queue

Priority queue can be implemented using an array, a linked list, a heap data structure, or a binary search tree. Among these data structures, heap data structure provides an efficient implementation of priority queues.

Hence, we will be using the heap data structure to implement the priority queue in this tutorial. A max-heap is implemented in the following operations. If you want to learn more about it, please visit [max-heap and min-heap](https://www.programiz.com/dsa/heap-sort#heap).

A comparative analysis of different implementations of priority queue is given below.

|Operations|peek|insert|delete|
|---|---|---|---|
|Linked List|`O(1)`|`O(n)`|`O(1)`|
|Binary Heap|`O(1)`|`O(log n)`|`O(log n)`|
|Binary Search Tree|`O(1)`|`O(log n)`|`O(log n)`|

---

## Priority Queue Operations

Basic operations of a priority queue are inserting, removing, and peeking elements.

Before studying the priority queue, please refer to the [heap data structure](https://www.programiz.com/dsa/heap-data-structure) for a better understanding of binary heap as it is used to implement the priority queue in this article.

---

### 1. Inserting an Element into the Priority Queue

Inserting an element into a priority queue (max-heap) is done by the following steps.

- Insert the new element at the end of the tree.
    
    ![insert an element at the end of the priority queue](https://cdn.programiz.com/sites/tutorial2program/files/insert-1_0.png "Priority queue insertion")
    
    Insert an element at the end of the queue
    
- [Heapify](https://www.programiz.com/dsa/heap-data-structure#heapify) the tree.
    
    ![heapify the priority queue after inserting new element](https://cdn.programiz.com/sites/tutorial2program/files/insert-2_0.png "Priority queue insertion")
    
    Heapify after insertion
    

Algorithm for insertion of an element into priority queue (max-heap)

If there is no node, 
  create a newNode.
else (a node is already present)
  insert the newNode at the end (last node from left to right.)
  
heapify the array

For Min Heap, the above algorithm is modified so that `parentNode` is always smaller than `newNode`.

---

### 2. Deleting an Element from the Priority Queue

Deleting an element from a priority queue (max-heap) is done as follows:

- Select the element to be deleted.
    
    ![choose the element to be deleted from the priority queue](https://cdn.programiz.com/sites/tutorial2program/files/delete-1_0.png "Priority queue deletion")
    
    Select the element to be deleted
    
- Swap it with the last element.
    
    ![swap the element to be deleted with the last leaf node element](https://cdn.programiz.com/sites/tutorial2program/files/delete-2_0.png "Swap the element with the last leaf of heap")
    
    Swap with the last leaf node element
    
- Remove the last element.
    
    ![remove the last leaf node element](https://cdn.programiz.com/sites/tutorial2program/files/delete-3.png "Remove last leaf element")
    
    Remove the last element leaf
    
- Heapify the tree.
    
    ![heapify the priority queue](https://cdn.programiz.com/sites/tutorial2program/files/delete-4.png "Heapify Priority Queue after deletion")
    
    Heapify the priority queue
    

Algorithm for deletion of an element in the priority queue (max-heap)

If nodeToBeDeleted is the leafNode
  remove the node
Else swap nodeToBeDeleted with the lastLeafNode
  remove noteToBeDeleted
   
heapify the array

For Min Heap, the above algorithm is modified so that the both `childNodes` are smaller than `currentNode`.

---

### 3. Peeking from the Priority Queue (Find max/min)

Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.

For both Max heap and Min Heap

return rootNode

---

### 4. Extract-Max/Min from the Priority Queue

Extract-Max returns the node with maximum value after removing it from a Max Heap whereas Extract-Min returns the node with minimum value after removing it from Min Heap.

---

## Priority Queue Implementations in Python, Java, C, and C++


```
// Priority Queue implementation in C++

#include <iostream>
#include <vector>
using namespace std;

// Function to swap position of two elements
void swap(int *a, int *b) {
  int temp = *b;
  *b = *a;
  *a = temp;
}

// Function to heapify the tree
void heapify(vector<int> &hT, int i) {
  int size = hT.size();
  
  // Find the largest among root, left child and right child
  int largest = i;
  int l = 2 * i + 1;
  int r = 2 * i + 2;
  if (l < size && hT[l] > hT[largest])
    largest = l;
  if (r < size && hT[r] > hT[largest])
    largest = r;

  // Swap and continue heapifying if root is not largest
  if (largest != i) {
    swap(&hT[i], &hT[largest]);
    heapify(hT, largest);
  }
}

// Function to insert an element into the tree
void insert(vector<int> &hT, int newNum) {
  int size = hT.size();
  if (size == 0) {
    hT.push_back(newNum);
  } else {
    hT.push_back(newNum);
    for (int i = size / 2 - 1; i >= 0; i--) {
      heapify(hT, i);
    }
  }
}

// Function to delete an element from the tree
void deleteNode(vector<int> &hT, int num) {
  int size = hT.size();
  int i;
  for (i = 0; i < size; i++) {
    if (num == hT[i])
      break;
  }
  swap(&hT[i], &hT[size - 1]);

  hT.pop_back();
  for (int i = size / 2 - 1; i >= 0; i--) {
    heapify(hT, i);
  }
}

// Print the tree
void printArray(vector<int> &hT) {
  for (int i = 0; i < hT.size(); ++i)
    cout << hT[i] << " ";
  cout << "\n";
}

// Driver code
int main() {
  vector<int> heapTree;

  insert(heapTree, 3);
  insert(heapTree, 4);
  insert(heapTree, 9);
  insert(heapTree, 5);
  insert(heapTree, 2);

  cout << "Max-Heap array: ";
  printArray(heapTree);

  deleteNode(heapTree, 4);

  cout << "After deleting an element: ";

  printArray(heapTree);
}
```

---

## Priority Queue Applications

Some of the applications of a priority queue are:

- Dijkstra's algorithm
- for implementing stack
- for load balancing and interrupt handling in an operating system
- for data compression in Huffman code

- [](https://www.programiz.com/dsa/priority-queue#definition)
- [](https://www.programiz.com/dsa/priority-queue#implementation)
- [](https://www.programiz.com/dsa/priority-queue#insert)
- [](https://www.programiz.com/dsa/priority-queue#delete)
- [](https://www.programiz.com/dsa/priority-queue#code)
- [](https://www.programiz.com/dsa/priority-queue#applications)

[

  


](https://www.programiz.com/cpp-programming/deque "C++ Deque")