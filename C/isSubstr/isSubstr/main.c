//
//  main.c
//  isSubstr
//
//  Created by Ruchik Dave on 4/24/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void isSubstr(char *str, char *target){
    if ((target == NULL) || (str == NULL)){
        printf("Error!\n");
        return;
    }
    
    int strLen = 0, targetLen = 0;
    while (str[strLen] != '\0') strLen++;
    while (target[targetLen] != '\0') targetLen++;
    
    printf("%d, %d\n", strLen, targetLen);
    if (targetLen > strLen){
        printf("Error!\n");
        return;
    }
    int i = 0, j = 0;
    while (str[i] != '\0'){
        j = 0;
        if (str[i] == target[j]){
            int newi = i;
            while(1){
                if (target[j] != str[newi])
                    break;
                newi++;
                j++;
                if (target[j] == '\0'){
                    printf("Yes is Substring from %d\n", i);
                    return;
                }
            }
        }
        i++;
    }
    
    printf("Not a substring\n");
    return;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    isSubstr("RuchikRuchikARuchikSRuchikDRuchikM", "RuchikD");
    return 0;
}
