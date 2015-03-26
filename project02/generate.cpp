#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

int main()
{
  ofstream BuildFile("randomnum.txt");

  srand(time(NULL));
  int num;
  
 
   for( int j = 0; j < 100; j++)
    {
      num = ( 1 +(rand() %  150 ));
  
    BuildFile << num << endl;
    }
  
  BuildFile.close();
     
  return 0;

}
