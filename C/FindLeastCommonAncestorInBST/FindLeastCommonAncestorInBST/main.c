//
//  main.c
//  FindLeastCommonAncestorInBST
//
//  Created by Ruchik Dave on 3/7/16.
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

/**************************************************************
 Complexity of below algorithm is O(h^2) where h = height of tree
 It can be further optimised to O(h) by using dictionary or hash
 table. Implementation is available in python section of same project
 **************************************************************/


#include <stdio.h>

struct listNode {
    int val;
    struct listNode * next;
};

struct Node {
    int val;
    struct Node * left;
    struct Node * right;
    struct Node * parent;
};

struct Node * createNode(int val){
    struct Node * node = (struct Node *)malloc (sizeof(struct Node));
    
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    node->parent = NULL;
    
    return node;
}

struct listNode * createListNode(int val){
    struct listNode * node = (struct listNode*)malloc(sizeof(struct listNode));
    
    node->val = val;
    node->next = NULL;
    
    return node;
}

struct Node * createAboveBST(struct Node * root){
    if (root == NULL){
        printf("Error: No root node\n");
        return root;
    }
    
    root->left = createNode(5);
    root->left->parent = root;
    root->left->left = createNode(2);
    root->left->left->parent = root->left;
    root->left->left->left = createNode(1);
    root->left->left->left->parent = root->left->left;
    
    root->left->right = createNode(7);
    root->left->right->parent = root->left;
    root->left->right->left = createNode(4);
    root->left->right->left->parent = root->left->right;
    root->left->right->left->left = createNode(3);
    root->left->right->left->left->parent = root->left->right->left;
    
    root->left->right->right = createNode(6);
    root->left->right->right->parent = root->left->right;
    
    root->right = createNode(11);
    root->right->parent = root;
    root->right->left = createNode(10);
    root->right->left->parent = root->right;
    root->right->right = createNode(15);
    root->right->right->parent = root->right;
    
    return root;
}

void inorderTraversal(struct Node * root){
    if (root == NULL){
        return;
    }
    
    inorderTraversal(root->left);
    printf("%d ", root->val);
    inorderTraversal(root->right);
    
}

int findLeastCommonAncester(struct Node* node1, struct Node* node2){
    struct Node * node1Temp = node1;
    struct Node * node2Temp = node2;
    
    while (node1Temp != NULL){
        while (node2Temp != NULL){
            if(node2Temp->val == node1Temp->val){
                return node2Temp->val;
            }
            node2Temp = node2Temp->parent;
        }
        node2Temp = node2;
        node1Temp = node1Temp->parent;
    }
    
    return -1;
}

int main(int argc, const char * argv[]) {
    struct Node * root = createNode(9);
    
    root = createAboveBST(root);
    
    inorderTraversal(root);
    printf("\n");
    
    int lca = findLeastCommonAncester(root->left->left->left, root->left->right);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    lca = findLeastCommonAncester(root->left->left->left, root->right->right);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    lca = findLeastCommonAncester(root->left->left->left, NULL);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    lca = findLeastCommonAncester(root->left->left->left, root);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    struct Node * newNode = createNode(50);
    lca = findLeastCommonAncester(root->left->left->left, newNode);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    lca = findLeastCommonAncester(NULL, NULL);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    lca = findLeastCommonAncester(root, root);
    if (lca != -1)
        printf ("Least Common ancestor = %d\n", lca);
    else
        printf ("Either one of the nodes is NULL or nodes are from different trees\n");

    return 0;
}
