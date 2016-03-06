#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Word {
    char *string;
    int index;
};

struct Word* createDuplicate(char *arr[], int size){
    struct Word dupList[size];
    struct Word* listEle = NULL;
    
    for (int i = 0; i < size; i++){
        listEle = (struct Word*)malloc(sizeof(struct Word));
        listEle->string = (char*)malloc(strlen(arr[i]));
        strcpy(listEle->string, arr[i]);
        listEle->index = i;
        dupList[i] = *listEle;
    }
    
    return dupList;
}

// Compare two characters. Used in qsort() for sorting an array of
// characters (Word)
int compChar(const void* a, const void* b)
{
    return *(char*)a - *(char*)b;
}

// Compare two words. Used in qsort() for sorting an array of words
int compStr(const void* a, const void* b)
{
    struct Word* a1 = (struct Word *)a;
    struct Word* b1 = (struct Word *)b;
    return strcmp(a1->string, b1->string);
}

void printAnagram(char *arr[], int size){
    for (int i = 0; i < size; i++){
        printf(" %s", arr[i]);
    }
    printf("\n");
    struct Word* dupArr = createDuplicate(arr, size);
    
    for (int i = 0; i < size; ++i){
        qsort(dupArr[i].string, strlen(dupArr[i].string), sizeof(char), compChar);
    }
    for (int i = 0; i < size; i++){
        printf("%s ", dupArr[i].string);
        printf("%d\n", dupArr[i].index);
    }
}

int main(){
    char *arr[] = {"cat", "dog", "act", "god", "dgo", "tca"};
    int size = sizeof(arr)/sizeof(arr[0]);
    
    printAnagram(arr, size);
}