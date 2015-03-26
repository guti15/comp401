#include<iostream>
#include "Btree.h"
#include "BNode.h"
#include <fstream>
using namespace std; 

int main()
{

  cout << "Runnning ... \n";



  // Btree bt(4);  // depending on what set is used 
  
  // bt.insert(5);
  // bt.insert(4);
  // bt.insert(10);
  // bt.insert(45);
  // bt.insert(69);
  // bt.insert(55);
  // bt.insert(99);
  // bt.insert(89);
  // bt.insert(140);
  // bt.insert(9999);
  // bt.insert(105);
  // bt.insert(780);
  
  // cout << "Here is the traversal: ";
  // bt.traverse(); cout << endl;


  // bt.remove(5);
  //   cout << "Traversal of tree after removing 5\n";
  //  bt.traverse();
  //   cout << endl;
 
  //   bt.remove(9999);
  //   cout << "Traversal of tree after removing 9999\n";
  //   bt.traverse();
  //   cout << endl;
 
  //     cout << "Here is the traversal: ";
  // bt.traverse(); cout << endl;
    
  // cout <<"program done. " << endl;

  //  READ IN FILE
  // ------------------------------------------------------------
  
  Btree bt(30);

  ifstream readFile;

  readFile.open("randomnum.txt"); 
  int temp;  
  int numOfLines = 100;
  int removeArrary[100]; 
  int j = 100, i = 0;
  cout << endl<< "before loop\n" ;


  while(!readFile.eof())
    { 

      readFile >> temp;
      // cout <<i << " " << temp << endl; 
      bt.insert(temp);
      removeArrary[i] = temp; 
      i++;
      
    }
   
  readFile.close();
  cout << "is it close\n";
  

  cout << "many lines longer Traversal number 1: " ; 

  bt.traverse();
    

    for( int i =0; i< 50 ; i++)
      {
	temp = removeArrary[i];
	bt.remove(temp);

      }

    cout << endl<< endl;
    cout <<  "this is traversal number 2: " ; 
    
    bt.traverse();

    cout << endl << endl;
    cout << "the amount of lines in second traversal is much shorter\n";
    cout << "program terminated\n"; 

  
  return 0;  

}
