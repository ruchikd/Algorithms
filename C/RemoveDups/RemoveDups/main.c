//
//  main.c
//  RemoveDups
//
//  Created by Ruchik Dave on 4/24/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

char * removeDups(char * str){
    if (str == NULL)
        return NULL;
    
    int len = strlen(str);
    if (len < 2)
        return NULL;
    
    int tail = 1;
    
    for (int i = 0; i < len; ++i){
        int j;
        for (j = 0; j < tail; ++j){
            if (str[i] == str[j])
                break;
        }
        if ( j == tail ){
            str[tail] == str[i];
            ++tail;
        }
    }
    str[tail] = '\0';
    printf("%s\n", str);
    
    return NULL;
    /*
    if (str == NULL)
        return NULL;
    
    int strLen = strlen(str);
    int end =  strLen;
    
    for (int i = 0; i < strLen-1; i++){
        int tail = i + 1;
        int exchanged = -1;
        
        while (tail < strLen){
            if (str[i] == str[tail]){
                char * temp = str[end];
                printf("str[end] = %c, str[tail] = %c", str[end], str[tail]);
                str[end] = str[tail];
                str[tail] = temp;
                exchanged = 1;
                end --;
            }
            if (exchanged == 1)
                tail --;
            else
                tail ++;
        }
        if ( i == end){
            break;
        }
    }
    printf("end = %d\n", end);
    if (end != strLen)
        str[end] = '\0';
    printf("%s\n", str);

    return str;
    */
}

int main(int argc, const char * argv[]) {
    // insert code here...
    char * str = removeDups("RuR");
    if (str != NULL)
        printf ("%s\n", str);
    else
        printf("NULL\n");
    return 0;
}
