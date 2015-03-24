#include <iostream>
#include "BNode.h"

using namespace std;

BNode::BNode(int num, bool leaf){
  minAmount = num;
  internalNode = leaf; 

  // ------------------------------------------------------------
  // p_keys == the number of keys each cell can contain
  // p2_child ==  the number of pointer held by each cell
  
  p_Keys = new int[2 * minAmount-1];  	// allocationg size of cell (node)
  
  p2_child = new BNode* [2 * minAmount]; // " " the number of pointers for each cell

  numCell = 0;			// amount of keys init to Zero 
  
} 



BNode *BNode::search( int key)
{

  int  i = 0;

  while( i < numCell && key > p_Keys[i])
    
    i++;

  if( p_Keys[i] == key )
    {
      return this;		// return pointer type Bnode
    }

  //  Leaf node ==  bottom of tree
  if (internalNode  == true )
    {
      return NULL;
    }

 
  return p2_child[i]->search(key);

  
} //  end of search 






void BNode::traverse()
{

  int i;


  for( i = 0; i < numCell; i++)
    {
      if( internalNode == false )
	{
	  p2_child[i]->traverse();
	}
      
      cout << " " << p_Keys[i]; // recursively print out
 
    }

  // print the last child

  if( internalNode == false)
    {
     p2_child[i]->traverse();

    }


  
} //  end traverse()


// split node contains current node which is the node beign  split
// and also spilt which is a new node  where info from current node is
// being transferred to split node

void BNode::splitNode( int k , BNode* currentNode )
{
  // create a new node for starters
  BNode* split = new BNode(currentNode->minAmount, currentNode->internalNode);
  
  split->numCell = minAmount-1;	// decrease the value in counter for each cell


  // copy the last int in node n to node split

  for( int i =0; i < minAmount-1; i++)
    {
      split->p_Keys[i] = currentNode->p_Keys[i + minAmount];

    }

  if( currentNode->internalNode == false )
    {

      for( int c = 0; c < minAmount; c++) //  count up to max number in cell
	{
	  //  remember double pointers (tricky)
	  
	  split->p2_child[c] = currentNode->p2_child[c+minAmount];
	  
	}

    }

  // Reduce the number of keys in current node 
  currentNode->numCell = minAmount - 1;



  // new node new child
  for( int j = numCell; j > k + 1; j--)
    {
      p2_child[j+1] = p2_child[j];

    }
  
  // connect the new child to this node
  p2_child[k+1] = split; 

  
  for(int j  = numCell-1; j >= k; j--)
    {
      p_Keys[j+1] = p_Keys[j];
    }

  p_Keys[k] = currentNode->p_Keys[minAmount -1];
  
  numCell = numCell + 1;

  
}



void BNode::Fillup(int key)	// check google style guide for variable name
{ 


  int i = numCell - 1;

  if( internalNode == true )
    { 
      while( i >= 0 && p_Keys[i] > key )
	{

	  p_Keys[i+1] = p_Keys[i]; 
	  i--;
	  
	}

      p_Keys[i+1] = key; 	// insert the key 
      
      numCell = numCell+1; 	// counter up by 1

    }


  else
    {
      while( i >= 0 && p_Keys[i] > key)
	i--;

      if(p2_child[i+1]->numCell == 2*minAmount-1)
	{

	  splitNode(i+1, p2_child[i+1]);


	  if(p_Keys[i+1] < key)
	    { i++;}

	}

      p2_child[i+1]->Fillup(key);

    }
}


// Build a delete function
// 
// 
//
// 
// 
int BNode::findKey(int key)
{
    int index = 0;
    while (index < numCell &&p_Keys[index] < key)
        index++;
    return index;

}


void BNode::remove(int key)
{ 
  int index = findKey(key);

  if(index < numCell && p_Keys[index] == key)
    {


  
      if (internalNode == true )
	{
	  removeFromLeaf(index);
	}
      else
	{
	  removeFromNonLeaf(index);
	}
    }

 else
   {
     if (internalNode == true) 
        {
            cout << "The key "<< key <<" is does not exist in the tree\n";
            return;
        }
 
     bool flag;
     if(index == numCell)
       {
	 index = true;
       } 
     else
       {
	 index = false;
       } 


     
        if (p2_child[index]->numCell < minAmount)
          {   fill(index);}
 

        if (flag && index > numCell)
	  {
	    p2_child[index-1]->remove(key);
	  }
        else
	  {
	    p2_child[index]->remove(key);
	  }

	return;
   }

}

void BNode::removeFromLeaf(int key)
{
 

    for (int i=key + 1; i<numCell; i++)
      {
        p_Keys[i-1] = p_Keys[i];
	
      }

    numCell--;
 
    return;
}
 
// A function to remove the key from this node - which is a not internal-leaf
void BNode::removeFromNonLeaf(int key)
{
 
  int temp;
  temp = p_Keys[key];
 
 
    if (p2_child[key]->numCell >= minAmount)
    {
        int pred = getPred(key);
        p_Keys[key] = pred;
        p2_child[key]->remove(pred);
    }
 
    else if  (p2_child[key+1]->numCell >= minAmount)
    {
      int successor  = getSucc(key);
        p_Keys[key] = successor;
        p2_child[key + 1]->remove(successor);
    }
 
    else
    {
      merge(key);
      p2_child[key]->remove(temp);
      
    }
    return;
    
}



int BNode::getPred(int key)  	// heavy debugg
{

    BNode *currentNode = p2_child[key];
    while (!currentNode->internalNode) // while the current node checks out false
      {
	currentNode = currentNode->p2_child[currentNode->numCell];
      }
    
    return currentNode->p_Keys[currentNode->numCell-1];
}
 
int BNode::getSucc(int key)
{
 
    BNode *current = p2_child[key + 1];
    while (!current->internalNode)
      {
	current = current->p2_child[0];
      }
 

    return current->p_Keys[0];
    
}



// Leaf for tomorrow



void BNode::fill(int key)
{
 

    if (key!=0 && p2_child[key-1]->numCell >=minAmount)
        bPrev(key);
 

    else if (key != numCell && p2_child[key+1]->numCell >= minAmount)
      {
        bNext(key);
      }

    else
    {
        if (key != numCell)
	  {
	    merge(key);
	  }
        else
	  {
            merge(key-1);
	  } //  close else 
	
    }
    return;
    
}


void BNode::bPrev(int key)	// before previous 
{
 
  BNode *child, *sibling; 	
  
  child = p2_child[key];
  sibling=p2_child[key-1];
 

  for (int i = child->numCell-1; i>=0; i--)
        child->p_Keys[i+1] = child->p_Keys[i];
 
 
    if (!child->internalNode)
    {
        for(int i=child->numCell; i >= 0; i--)
	  {
            child->p2_child[i + 1] = child->p2_child[i];
	  }
	
    }
 

    child->p_Keys[0] = p_Keys[key-1];
 

    if (!internalNode)
      {
        child->p2_child[0] = sibling->p2_child[sibling->numCell];
      }
    
    p_Keys[key-1] = sibling->p_Keys[sibling->numCell-1]; // reduce the amount of nodes in the cell by onex

    child->numCell += 1;	// increment the child by one
    sibling->numCell -= 1;	// subtract one from the sibx
    
     return;
    
}




//
// pointerrs!!!


void BNode::bNext(int key)
{


  BNode *child, *sibling;
  
  child = p2_child[key];
  sibling = p2_child[key + 1];
  
  child->p_Keys[(child->numCell)] = p_Keys[key]; // check syntax.x
 
    if (!(child->internalNode))
      {
        child->p2_child[(child->numCell)+ 1] = sibling->p2_child[0];
      }

    p_Keys[key] = sibling->p_Keys[0];
 
    for (int i=1; i < sibling->numCell; i++)
      {
        sibling->p_Keys[i-1] = sibling->p_Keys[i];
      }

    if (!sibling->internalNode)
    {
        for(int i=1; i<=sibling->numCell; i++)
	  {
	    sibling->p2_child[i-1] = sibling->p2_child[i];
	  }
	
    }
 

    child->numCell += 1; 		//  increase the child
    sibling->numCell -= 1;		// decrease the sibling 
 
    return;
}



void BNode::merge(int key1)
{
  BNode *child, *sibling;
  child= p2_child[key1];
  sibling = p2_child[key1+1];
 
  child->p_Keys[minAmount-1] = p_Keys[key1];
 

  for (int i=0; i < sibling->numCell; i++)
    child->p_Keys[i+minAmount] = sibling->p_Keys[i];
 
  if (!child->internalNode)
    {
      for(int i=0; i <= sibling->numCell; i++)
	child->p2_child[i+minAmount] = sibling->p2_child[i];
    }
 
  for (int i = key1+1; i< numCell; i++)
    p_Keys[i-1] = p_Keys[i];
 

  for (int i=key1 + 2; i <= numCell; i++)
    p2_child[i-1] = p2_child[i];
 

  child->numCell += sibling->numCell + 1;
  numCell--;
 

  delete(sibling);		// delete this cell
  return;
  
}
