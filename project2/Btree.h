#ifndef TWOTREETREE
#define TWOTREETREE

#include <iostream>
#include "BNode.h"

using namespace std;

class Btree{

private:
  BNode* root;			// initil. the root of tree
  int t; 	       		// The size of the cell

  
 public:
  
  Btree(int t);
  void insert(int key);
  void traverse();

  BNode* search(int key);

  void remove(int key1);


};


#endif

  

