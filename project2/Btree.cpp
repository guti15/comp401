#include "Btree.h"


Btree::Btree(int num )
{
  t = num; 
  root = NULL;

} 

void Btree::traverse()
{


  if ( root != NULL )
    {
      root->traverse();

    }
  
} 


BNode* Btree::search( int key)
{
  if (root == NULL)		// is the root empty
    { return NULL;}
  
  else
    { return root->search(key);} // no? keep looking!
  

} 

void Btree::insert(int key)
{

  // Check if tree is empty

  if (root == NULL)
    {
      // const.  a new node, t = size of cell determ prev. 
      
      root = new BNode( t, true); 
      root->p_Keys[0] = key;  	// * enter key of this func into node key
      root->numCell = 1; 		// init the number of keys in root

    }

  //  if tree is not full ...INSANE
  // two helper functions will be created 
  
  else
    {
      // how big is root?

      if(root->numCell == 2*t - 1)
	{

	  // create a new root

	  BNode* p_newRoot = new BNode(t, false);

	  // link previous root to new root just made

	  p_newRoot->p2_child[0] = root; // new root sets old root child

	  p_newRoot->splitNode(0, root);

	  // elect which node the key should go in

	  int i = 0;

	  if( p_newRoot->p_Keys[0] < key)
	    {
	      i++;

	      p_newRoot->p2_child[i]->Fillup(key);

	      //  change root

	      root = p_newRoot;
	    } 

	}

      else
	{

	  root->Fillup(key); //  assuming there is space at root
	}
    }
    
}




void Btree::remove(int key1)
{
    if (root == NULL)
    {
        cout << "The tree is empty\n";
        return;
    }
 
    // Call the remove function for root
    root->remove(key1);
 
    if (root->numCell == 0)
    {
        BNode *temp = root;
        if (root->internalNode)
            root = NULL;
        else
            root = root->p2_child[0];
 

        delete temp;
    }
    return;
}
