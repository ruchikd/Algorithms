//
//  main.c
//  AddArrToTree
//
//  Created by Ruchik Dave on 3/14/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

struct Node {
    int val;
    struct Node * lChild;
    struct Node * rChild;
};

struct Node * AddToTree(int arr[], int start, int end){
    if ( end < start)
        return NULL;
    
    int mid = (start + end)/2;
    struct Node * node = (struct Node *)malloc(sizeof(struct Node));
    node->val = arr[mid];
    node->lChild = AddToTree(arr, start, mid-1);
    node->rChild = AddToTree(arr, mid+1, end);
    
    return node;
}

void inorder(struct Node * node){
    if (node == NULL){
        return;
    }
    
    inorder(node->lChild);
    printf(" %d", node->val);
    inorder(node->rChild);
}

int main(int argc, const char * argv[]) {
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    
    struct Node * root = (struct Node *)malloc(sizeof(struct Node));
    root = AddToTree(arr, 0, 9);
    
    inorder(root);

    return 0;
}
