//
//  main.c
//  checkIfStringCharsAreUnique
//
//  Created by Ruchik Dave on 3/10/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void checkIfStrCharsAreUnique(char * str){
    int ret = 0, i = 0, val = 0;
    int ascii[256];
    
    if (str == NULL){
        printf ("Input Error\n");
    }
    
    memset(ascii, 0, sizeof(int)*256);
    
    while (str[i] != '\0'){
        val = (int)str[i];
        if (ascii[val] == 1){
            ret = -1;
            break;
        }else{
            ascii[val] = 1;
        }
        if (ret == 0)
            i++;
    }
    
    
    if (ret == -1)
        printf("String %s is not having unique chars, dup char = %c\n", str, str[i]);
    else
        printf("String %s is having unique chars\n", str);
}

int main(int argc, const char * argv[]) {
    char str[] = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?";
    
    checkIfStrCharsAreUnique(str);

    return 0;
}
