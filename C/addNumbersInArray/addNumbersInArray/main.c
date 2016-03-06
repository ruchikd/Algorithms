//
//  main.c
//  addNumbersInArray
//
//  Created by Ruchik Dave on 3/6/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arrToNum(int arr[]){
    int num = 0, tens = 1;
    
    for (int i = strlen(arr); i > 0; i--){
        num = num + (itoa(arr[i] * tens));
        tens = tens*10;
    }
    
    return num;
}

void addArrays(int arr1[], int arr2[], int arr3[]){
    printf("%d\n", arrToNum(arr1) + arrToNum(arr2) + arrToNum(arr3));
}

int main(int argc, const char * argv[]) {
    int num1[] = {"2", "4", "6"};
    int num2[] = {"1"};
    int num3[] = {"5", "3", "8", "2", "9"};
    
    addArrays(num1, num2, num3);
    
    return 0;
}
