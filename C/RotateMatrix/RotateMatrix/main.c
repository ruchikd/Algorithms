//
//  main.c
//  RotateMatrix
//
//  Created by Ruchik Dave on 4/24/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

void printMatrix(int matrix[][4], int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void RotateMatrix(int matrix[][4], int n){
    for (int layer = 0; layer < n/2; ++layer){
        printf("\n");
        int first = layer;
        printf("first = layer = %d\n", first);
        int last = n - 1 - layer;
        printf("last = %d\n", last);
        
        for (int i = first; i < last; ++i){
            printf("\n");
            int offset = i - first;
            printf("offset = %d\n", offset);
            int top = matrix[first][i];
            printf("top = %d \t\t\t=\t matrix[%d][%d] = %d\n", top, first, i, matrix[first][i]);
            
            printf("matrix[%d][%d] = %d \t=\t matrix[%d][%d] = %d\n", first, i, matrix[first][i], last-offset, first, matrix[last- offset][first]);
            matrix[first][i] = matrix[last- offset][first];
            
            printf("matrix[%d][%d] = %d \t=\t matrix[%d][%d] = %d\n", last-offset, first, matrix[last-offset][first], last, last - offset, matrix[last][last - offset]);
            matrix[last-offset][first] = matrix[last][last - offset];
        
            printf("matrix[%d][%d] = %d \t=\t matrix[%d][%d] = %d\n", last, last - offset, matrix[last][last - offset], i, last, matrix[i][last]);
            matrix[last][last - offset] = matrix[i][last];
            
            printf("matrix[%d][%d] = %d \t=\t top = %d\n", i, last, matrix[i][last], top);
            matrix[i][last] = top;
        }
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int matrix[4][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12},{13,14,15,16}};
    int n = 4;
    printMatrix(matrix, n);
    RotateMatrix(matrix, n);
    printf("\n");
    printMatrix(matrix, n);
    return 0;
}
