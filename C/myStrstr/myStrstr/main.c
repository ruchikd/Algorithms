//
//  main.c
//  myStrstr
//
//  Created by Ruchik Dave on 3/5/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int mystrstr(char* haystack, char* needle){
    int position = -1;
    
    if ((haystack == NULL) || (needle == NULL))
        return position;
    
    int haystackLen = strlen(haystack);
    int needleLen = strlen(needle);
    
    for (int i = 0; i < haystackLen; i++){
        if (haystack[i] == needle[0]){
            int k = i;
            for (int j = 0; j < needleLen; j++){
                if (haystack[k] != needle[j]){
                    position = -1;
                    break;
                }else if (needle[j+1] == '\0'){
                    position = i;
                    return position;
                }
                k++;
            }
        }
    }
    
    return position;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int position = mystrstr("lllllll", "lll");
    
    printf("The position of needle in the haystack = %d\n", position);
    
    return 0;
}
