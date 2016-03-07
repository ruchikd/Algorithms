//
//  main.c
//  CheckIfNumberIsPowerOf2
//
//  Created by Ruchik Dave on 3/6/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

int checkIfNumIsPowerOf2 (int givenNumber){
    int num = givenNumber;
    
    if (num == 0){
        return -1;
    }
    int divisor = 0;
    
    if (num < 0)
        divisor = -2;
    else
        divisor = 2;
    
    while (num != 1){
        num = num / divisor;
        if (num == 1){
            return 0;
        }
        if ((num % divisor) != 0 ){
            return -1;
        }
    }
    
    printf ("%d is power of 2\n");
    return 0;
}

int main(int argc, const char * argv[]) {
    int num = -32;
    
    if (checkIfNumIsPowerOf2(num) == 0)
        printf("%d is power of 2\n", num);
    else
        printf("%d is not power of 2\n", num);

    return 0;
}
