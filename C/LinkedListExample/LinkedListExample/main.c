//
//  main.c
//  LinkedListExample
//
//  Created by Ruchik Dave on 3/6/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

struct Node{
    int val;
    struct Node * next;
};

struct Node * createNode(int val){
    struct Node * node = (struct Node *)malloc(sizeof(struct Node));
    node->val = val;
    node->next = NULL;
    
    return node;
}

void appendToLinkedList(struct Node * head, int val){
    if (head == NULL)
        return;
    
    struct Node * node = head;
    while (node->next != NULL){
        node = node->next;
    }
    
    struct Node * newNode = createNode(val);
    node->next = newNode;
}

void addInBetween(struct Node * head, int val, int addval){
    if (head == NULL)
        return;
    
    struct Node * node = head;
    while (node != NULL){
        if (node->val == val){
            struct Node * temp = node->next;
            struct Node * addNode = createNode(addval);
            node->next = addNode;
            addNode->next = temp;
        }
        node = node->next;
    }
}

struct Node* delNode(struct Node * head, int val){
    if (head == NULL)
        return head;
    
    if (head->val == val){
        while (head->next != NULL){
            if (head->val != val)
                break;
            struct Node* newHead = head->next;
            free(head);
            head = NULL;
            head = newHead;
        }
    }
    
    struct Node * node = head;
    while(node->next != NULL){
        if(node->next->val == val){
            if (node->next->next == NULL){
                free(node->next);
                node->next = NULL;
                
                return head;
            }else{
                struct Node * temp = node->next;
                node->next = temp->next;
                free(node);
                node = NULL;
            }
        }
        node = node->next;
    }
    
    return head;
}

int main(int argc, const char * argv[]) {
    int i = 1;
    struct Node * head = createNode(0);
    struct Node * nextNode = createNode(0);
    head->next = nextNode;
    
    while (i != 25){
        appendToLinkedList(head, i);
        i++;
    }
    
    addInBetween(head, 21, 30);
    
    head = delNode(head, 0);
    
    struct Node * temp = head;
    while (temp != NULL){
        printf ("%d ", temp->val);
        temp = temp->next;
    }
    printf("\n");

    return 0;
}
