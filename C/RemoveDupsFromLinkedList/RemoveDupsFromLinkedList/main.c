//
//  main.c
//  RemoveDupsFromLinkedList
//
//  Created by Ruchik Dave on 3/13/16.
//  Copyright © 2016 Ruchik Dave. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node * next;
};

struct Node * createNew(int val){
    struct Node * node = (struct Node *)malloc(sizeof(struct Node*));
    
    node->val = val;
    node->next = NULL;
    
    return node;
}

void addToList(struct Node * head, int val){
    if (head == NULL)
        return;
    
    struct Node * temp = head;
    
    
    while (temp != NULL){
        if (temp->val == val){
            struct Node * newNode = createNew(val);
            if (temp->next == NULL){
                temp->next = newNode;
            }else{
                newNode->next = temp->next;
                temp->next = newNode;
            }
            temp = newNode->next;
        }else{
            temp = temp->next;
        }
    }
}

void removeDupsFromList(struct Node * head){
    if (head == NULL)
        return;
    
    struct Node * temp = head;
    
    int arr[15];
    memset(arr, "-1", sizeof(int)*15);
    
    struct Node * previous = NULL;
    int j = 0;
    
    while(temp != NULL){
        for (int i = 0 ; i < 15; i++){
            if (arr[i] == temp->val){
                previous->next = temp->next;
                free(temp);
            }
        }
        arr[j] = temp->val;
        j++;
        previous = temp;
        temp = temp->next;
    }
}

void printList(struct Node * n){
    printf("\n");
    while (n != NULL){
        printf("%d ", n->val);
        n = n->next;
    }
    printf("\n");
}

int main(int argc, const char * argv[]) {
    struct Node * head = createNew(0);
    struct Node * temp = head;
    
    for (int i = 1; i < 10; i++){
        struct Node * newNode = createNew(i);
        temp->next = newNode;
        temp = temp->next;
    }
    
    printList(head);
    addToList(head, 0);
    printList(head);
    removeDupsFromList(head);
    printList(head);

    return 0;
}
