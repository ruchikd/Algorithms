//
//  main.c
//  treeSamples
//
//  Created by Ruchik Dave on 3/1/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

struct node {
    int val;
    struct node * left;
    struct node * right;
};

typedef struct node NODE;

NODE * createNode(int val){
    NODE * node = malloc(sizeof(NODE));
    
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    
    return node;
}

NODE * addToTree(NODE * root, int val){
    NODE * temp = root;
    NODE * newNode = NULL;
    
    if(root == NULL){
        root = createNode(val);
        
        return root;
    }
    
    if(temp->val >= val){
        if (temp->left == NULL){
            newNode = createNode(val);
            temp->left = newNode;
            
            return root;
        }
        addToTree(temp->left, val);
    }else{
        if (temp->right == NULL){
            newNode = createNode(val);
            temp->right = newNode;
            
            return root;
        }
        addToTree(temp->right, val);
    }
    
    return root;
}

void postorderTraversal(NODE * root){
    if (root == NULL)
        return;
    
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    printf("%d ", root->val);
}

void preorderTraversal(NODE * root){
    if (root == NULL)
        return;
    
    printf("%d ", root->val);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

void inorderTraversal(NODE * root){
    if (root == NULL)
        return;
    
    inorderTraversal(root->left);
    printf("%d ", root->val);
    inorderTraversal(root->right);
}

int main(int argc, const char * argv[]) {
    NODE * root = createNode(5);
    
    root = addToTree(root, 3);
    root = addToTree(root, 6);
    root = addToTree(root, 1);
    root = addToTree(root, 8);
    root = addToTree(root, 2);
    root = addToTree(root, 7);
    root = addToTree(root, 4);
    
    inorderTraversal(root);
    printf("\n");
    preorderTraversal(root);
    printf("\n");
    postorderTraversal(root);
    
    return 0;
}
