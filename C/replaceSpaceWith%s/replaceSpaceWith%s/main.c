//
//  main.c
//  replaceSpaceWith%s
//
//  Created by Ruchik Dave on 3/11/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void replaceSpace(char * str){
    if (str == NULL)
        return;
    
    int len = strlen(str), i = 0, j = 0, newLen = 0;

    while(str[i] != '\0'){
        if (str[i] == ' '){
            newLen = newLen + 2;
        }
        newLen++;
        i++;
    }
    printf("len = %d\n", len);
    printf("new length = %d\n", newLen);
    
    char * newStr = (char*)malloc(sizeof(char)*newLen);
    memset (newStr, 0, sizeof(char)*newLen);
    i = 0;
    
    while (str[i] != '\0'){
        if (str[i] == ' '){
            newStr[j++] = '%';
            newStr[j++] = 's';
        }else{
            newStr[j++] = str[i];
        }
        i++;
    }
    newStr[j] = '\0';
    
    printf("New String = %s\n", newStr);
}

int main(int argc, const char * argv[]) {
    char * sentence = " Hi, My Name is Ruchik Samir Dave";
    
    replaceSpace(" ");

    return 0;
}
