//
//  main.c
//  SetZeroesToMatrix
//
//  Created by Ruchik Dave on 3/12/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

int row[4] = {-1, -1, -1, -1};
int col[4] = {-1, -1, -1, -1};

void printMatrix(int matrix[4][4]){
    int i = 0, j = 0;
    
    for (i = 0 ; i < 4; i++){
        for (j = 0; j < 4; j++){
            printf("  %d", matrix[i][j]);
        }
        printf("\n");
    }
}

void findZeros(int matrix[4][4]){
    if (matrix == NULL){
        return;
    }
    
    int m = 0, n = 0;
    
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            if (matrix[i][j] == 0){
                row[m] = j;
                col[n] = i;
                m++;
                n++;
            }
        }
    }
}

void fillZeroes(int matrix[4][4]){
    if (matrix == NULL)
        return;
    
    for ( int i = 0; i < 4; i++)
        printf(" %d", row[i]);
    printf("\n");
    for ( int i = 0; i < 4; i++)
        printf(" %d", col[i]);
    printf ("\n");
    
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if (row[k] == j){
                    matrix[i][j] = 0;
                }
            }
            for (int l = 0; l < 4; l++){
                if (col[l] == i){
                    matrix[i][j] = 0;
                }
            }
        }
    }
    
    printMatrix(matrix);
}

int main(int argc, const char * argv[]) {
    int matrix[4][4] = {    { 1, 2,  3,  4},
                            { 5, 6,  7,  8},
                            { 9, 10, 11, 12},
                            {13, 14, 15, 16}};
    
    printMatrix(matrix);
    matrix[2][1] = 0;
    findZeros(matrix);
    fillZeroes(matrix);

    return 0;
}
