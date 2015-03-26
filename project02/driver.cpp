#include<iostream>
#include "Btree.h"
#include "BNode.h"
using namespace std; 

int main()
{

  cout << "Runnning ... \n";


  Btree bt(4);

  bt.insert(5);
  bt.insert(4);
  bt.insert(10);
  bt.insert(45);
  bt.insert(69);
  bt.insert(55);
  bt.insert(99);
  bt.insert(89);
  bt.insert(140);
  bt.insert(9999);
  bt.insert(105);
  bt.insert(780);
  
  cout << "Here is the traversal: ";
  bt.traverse(); cout << endl;


  bt.remove(5);
    cout << "Traversal of tree after removing 5\n";
   bt.traverse();
    cout << endl;
 
    bt.remove(9999);
    cout << "Traversal of tree after removing 9999\n";
    bt.traverse();
    cout << endl;
 
      cout << "Here is the traversal: ";
  bt.traverse(); cout << endl;
    
  cout <<"program done. " << endl;

  //  READ IN FILE
  // ------------------------------------------------------------

  int temp;
  ifstream readFile;

  readFile.open("randomnum.txt");
  
  numOfLines = 100;
  removeArrary[50]; 
   
    
    for( int i = 0; i < numOfLines; i++)

      {
	if(  i < 50 )
	  {
	    removeArrary[i] = readFile;
	  }	
	bt.insert(readFile);
      
      } 

    bt.travers();

    for( i =0; i< 50 ; i++)
      {
	temp = removeArrary[i];  bt.remove(temp);

      }

    bt.trav();
    cout << "program terminated\n"; 

  
  return 0;  
} 
