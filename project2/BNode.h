// using hungarian notation p_(name) indicate pointer
#ifndef BNODE
#define BNODE



class BNode{

 public:

  /*  Constructors */

  			      // An empty constructor 
  BNode( int num, bool leaf);	      //  A constructor with int and bool
  void  splitNode( int t, BNode* n); // A node gets to full needs to be split

  int* p_Keys;		    // an array of keys / SHOUL BE STRING **
  int numCell;		    // current number 
  BNode* search(int key);   // temp doing with key should be STRING **
  void traverse();	    //  a function done in previous assing
  void Fillup(int key); 
  BNode** p2_child; 		// an array of pointers


  void remove(int key);
  void removeFromLeaf(int key );
  void removeFromNonLeaf(int key);
  int getPred(int key);
  int getSucc(int key);
  void fill(int key); 
  void bPrev(int key);
  void bNext(int key);
  void merge(int key);
  int findKey(int key);
  bool internalNode;		//  check if its an internal leaf  
  friend class BTree;
  
 private:

  

  int minAmount; 		// the amount of keys that I can have.


};

#endif
