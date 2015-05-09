 Project Two: B-Tree
========================================

![B-Tree](https://salihdeveci.files.wordpress.com/2012/10/btree-3.gif)



####B-Tree Overview 
---------------------
B-Tree are special in many forms, some of the characteristics that make it so special is that it contains logarithmic time in areas such as insertion,  search, and deletion.  The _B Tree_ is derived from the class [binary tree](http://en.wikipedia.org/wiki/Binary_tree) which is less complex in form of implementation and functionality.  The B Tree also manages to be a self balancing tree. B-Tree begin from top to bottom so new numbers being inserted get added at the root and then begins to adjust itself. 



####Content
---------------

* `BNode.cpp` - File containing all the functionality of a B Tree node. 
* `Bnode.h` - Header file containing what is stored in the class of B-Node.
* `Btree.h` - Header file containing B-Tree class and other variables stored in B-tree
* `Btree.cpp` - File containing all the functionality of B-tree.
* `Driver.cpp` - File containing main(), linking all the files togther.
* `generate.cpp`- File which generates random numbers and writes them to file named 'randumnum.txt'
* `randomnum.txt` - File containing random numbers to place in B-Tree. 


####Resources Used:
-----------------------

1. [Wikipedia](http://en.wikipedia.org/wiki/B-tree)
2. [CLR Algorithm Book](http://www.amazon.com/Introduction-Algorithms-Edition-Thomas-Cormen/dp/0262033844)
3. [Stack Overflow](http://stackoverflow.com/questions/16305154/b-tree-node-implementation)



