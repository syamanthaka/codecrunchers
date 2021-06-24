/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int* totalcoins;


void Setup(){
    totalcoins = (int*) malloc(1 * sizeof(int));
}

void Turn(){
    int crec;
     
    crec = getCoinsReceivedLastTurn();
    *totalcoins+=crec;
    if(totalcoins>=0){
       play(1);    
    }
    else{
      play(0);
    }
    
}

void TearDown(){
     free(totalcoins);
}
