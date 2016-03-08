//
//  main.c
//  LevelOrderTraversal
//
//  Created by Ruchik Dave on 3/8/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

/**************************************************************
                      9
                    /   \
                  5       11
               /    \      / \
              2      7    10  15
            /       / \
           1       4    6
         /
        3
 **************************************************************/

#include <stdio.h>

struct Node {
    int val;
    struct Node * left;
    struct Node * right;
};

struct Node * createNode(int val){
    struct Node * node = (struct Node *)malloc (sizeof(struct Node));
    
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    
    return node;
}

struct Node * createAboveBST(struct Node * root){
    if (root == NULL){
        printf("Error: No root node\n");
        return root;
    }
    
    root->left = createNode(5);
    root->left->left = createNode(2);
    root->left->left->left = createNode(1);
    
    root->left->right = createNode(7);
    root->left->right->left = createNode(4);
    root->left->right->left->left = createNode(3);
    
    root->left->right->right = createNode(6);
    
    root->right = createNode(11);
    root->right->left = createNode(10);
    root->right->right = createNode(15);
    
    return root;
}

int height(struct Node* root){
    if (root == NULL){
        return 0;
    }
    int lheight = height(root->left);
    int rheight = height(root->right);
        
    if (lheight > rheight)
        return lheight+1;
    else
        return rheight+1;

}

void printLevelOrder(struct Node * root, int height){
    if (root == NULL)
        return;
    else if (height == 1)
        printf ("%d ", root->val);
    else if (height > 1) {
        printLevelOrder(root->left, height-1);
        printLevelOrder(root->right, height-1);
    }
}

void levelOrderTraversal(struct Node* root){
    int h = height(root);
    
    printf ("%d\n", h);
    
    for(int i = 1; i < h+1; i++)
        printLevelOrder(root, i);
}

int main(int argc, const char * argv[]) {
    struct Node * root = createNode(9);
    
    root = createAboveBST(root);
    levelOrderTraversal(root);
    
    printf("\n");
    
    return 0;
}

