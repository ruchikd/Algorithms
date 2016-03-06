//
//  main.c
//  FindDupWithinKDistance
//
//  Created by Ruchik Dave on 3/6/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void findDupList(int arr[], distance){
    int start = 0, end = 0;
    
    if ((distance <= 0) || (arr == NULL))
        printf ("Error in input\n");
        return;
    
    for (int i = 0; i < sizeof(arr); i++){
        start = i+1;
        end = i + distance;
        for (int j = start; j < end; j++){
            if (arr[j] == NULL){
                continue;
            }
            if (arr[i] == arr[j]){
                printf ("%d ", arr[i]);
            }
        }
    }
    printf("\n");
    return;
}

int main(int argc, const char * argv[]) {
    int arr[] = {1, 2, 4, 5, 3, 9, 8, 3, 5, 6, 2};
    
    findDupList(NULL, 0);
    
    return 0;
}
