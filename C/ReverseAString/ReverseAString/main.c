//
//  main.c
//  ReverseAString
//
//  Created by Ruchik Dave on 4/24/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

char * reverse(char * str){
    if (str == NULL)
        return NULL;
    
    int strLen = 0, i = 0;
    while (str[strLen] != '\0')
        strLen++;
    
    char * newStr = (char*)malloc(sizeof(char)*strLen);
    
    for (int j = strLen-1; j >= 0; j--)
        newStr[i++] = str[j];
    
    newStr[i] = '\0';
    
    printf("%s\n", newStr);
    return newStr;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    char * str = "Hello, World!";
    
    reverse(str);
    return 0;
}
