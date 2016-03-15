//
//  main.c
//  Endianness
//
//  Created by Ruchik Dave on 3/15/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void show_mem_rep(char * start, int n){
    int i;
    for ( i = 0; i < n; i++){
        printf(" %.2x", start[i]);
    }
    printf ("\n");
}

void checkEndianness(){
    unsigned int i = 1;
    char *c = (char*)&i;
    if(*c){
        printf ("little endian\n");
    }else{
        printf ("big endian\n");
    }
}

int main(int argc, const char * argv[]) {
    int i = 0x01234567;
    
    show_mem_rep((char*)&i, sizeof(i));
    
    checkEndianness();
    
    return 0;
}
