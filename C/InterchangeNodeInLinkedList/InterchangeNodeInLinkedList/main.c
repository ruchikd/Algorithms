//
//  main.c
//  InterchangeNodeInLinkedList
//
//  Created by Ruchik Dave on 3/7/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>

struct Node {
    int val;
    struct Node * next;
};

struct Node * createNode (int val){
    struct Node * node = (struct Node *)malloc(sizeof(struct Node));
    
    node->val = val;
    node->next = NULL;
    
    return node;
}

void printAllList(struct Node * head){
    if (head == NULL){
        printf("Error: Linked List given is NULL\n");
        return;
    }
    
    struct Node * temp = head;
    
    while (temp != NULL){
        printf ("%d ", temp->val);
        temp = temp->next;
    }
    printf("\n");
}

struct Node * interchangeNodes(struct Node * head){
    if (head == NULL)
        return head;
    
    struct Node * temp = head;
    
    while (temp != NULL){
        if (temp->next == NULL)
            return head;
        
        int tempVal;
        
        tempVal = temp->val;
        temp->val = temp->next->val;
        temp->next->val = tempVal;
        
        temp = temp->next->next;
    }
    
    return head;
}

int main(int argc, const char * argv[]) {
    struct Node * head = createNode(0);
    struct Node * refNode = head;
    
    for (int i = 1; i < 100; i++){
        struct Node *temp = createNode(i);
        refNode->next = temp;
        refNode = temp;
    }
    
    printAllList(head);
    
    head = interchangeNodes(head);
    printAllList(head);
    
    return 0;
}
