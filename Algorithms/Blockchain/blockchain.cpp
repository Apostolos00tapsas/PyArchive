#include "block.cpp"
#include <stdlib.h>
#include <time.h>
using namespace std;
const int MAX=26+26+10;

string printRandomString(int n) 
{ 
	char alphabet[MAX] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
                          'h', 'i', 'j', 'k', 'l', 'm', 'n',  
                          'o', 'p', 'q', 'r', 's', 't', 'u', 
                          'v', 'w', 'x', 'y', 'z', 'A','B','C',
						  'E','F','G','H','I','J','L','M','N',
						  'O','P','Q','R', 'S', 'T', 'U', 
                          'V', 'W', 'X', 'Y', 'Z','1','2','3',
						  '4','5','6','7','8','9','0'}; 
    
    
    string res = ""; 
    for (int i = 0; i < n; i++)  
        res = res + alphabet[rand() % MAX]; 
      
    return res; 
} 

int main(){
	blockchain a;
	srand (time(NULL));
    a.add_node(printRandomString(10),printRandomString(15));
	a.add_node(printRandomString(10),printRandomString(15));
    a.add_node(printRandomString(10),printRandomString(15));
	a.display();
    return 0;
}
