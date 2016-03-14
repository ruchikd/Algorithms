//
//  main.c
//  FindIfAnagrams
//
//  Created by Ruchik Dave on 3/13/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void findIfAnagrams(char * str1, char * str2){
    if ((str1 == NULL) || (str2 == NULL)){
        printf("Not an Anagram\n");
        return;
    }
    
    if (strlen(str1) != strlen(str2)){
        printf("Not an Anagram\n");
        return;
    }
    
    int letters[256];
    for (int i = 0; i < 256; i++){
        letters[i] = 0;
    }
    
    for (int i = 0; i < strlen(str1); i++){
        letters[(int)str1[i]]++;
    }
    
    for (int i = 0; i < strlen(str2); i++){
        letters[(int)str2[i]]--;
    }
    
    for (int i = 0; i < 256; i++){
        if (letters[i] != 0){
            printf("Not an Anagram\n");
            return;
        }
    }
    
    printf("%s & %s are Anagrams\n", str1, str2);
    return;
}

int main(int argc, const char * argv[]) {
    findIfAnagrams("", "");

    return 0;
}
