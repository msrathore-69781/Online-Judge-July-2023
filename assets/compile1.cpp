#include <iostream>
#include <cstring>
#include<string>
using namespace std;
 
string getCompressedString(string &input) {
//int l=strlen(input);
     int var=0,count=1;
    
    
     for (int i =0;input[i]!='\0';i++){
         if(input[i]==input[i+1]){
             count++;
            
         }
         else{
             if (count>1){
                 char ch=input[i];
                 input[var]=ch;
                
                 input[var+1]=(char)(count+'0');
                 var+=2;
                 count=1;
        }
             else{
                 input[var]=input[i];
                 var++;
                
             }
            
         }
        
        
     }
     //for (int i=var-1;input[i]!='\0';i++){
     //input[i]='\0';}
    
       input = input.substr(0,var);
     return input;   
 }

/*string getCompressedString(string &input) {
    
    int n=input.size();
    int a = 0,b = 0,j = 0,k = 0;
    
    for(int i = 0; i !=n ; i++){
        
        if(input[j] == input[i]){
            b++; 
        }
        
        else if(b > 1) {
            j = i;
            input[k] = input[i-1];
            k++;
            input[k] = b+48;
            k++;
            b = 0; i--;
        }
        
        else if(b == 1){
            j = i;
            input[k] = input[i-1];
            k++;
            b = 0; i--;
        }
    }
    
    input = input.substr(0,k);
    return input;
*/
int main() {
    int size = 1e6;
    string str;
    cin >> str;
    str = getCompressedString(str);
    cout << str+"A" << endl;
}