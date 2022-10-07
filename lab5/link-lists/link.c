#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct node
{
    int num;
    struct node *next;
}
node;

void free_list(node* n);
void free_list_alt(node* n);
void insert_sorted(node** list, int num);

int main(void)
{
    // TODO 1: Create a linked list with at least two nodes containing two ints

    // TODO 3: Pass your linked list into your free function to free it
    
    // TODO 4: Run valgrind to check for memory errors
    
    // TODO 5: We will talk through how insert_sorted works
    node* list = malloc(sizeof(node));
    list->num = 0;
    for (int i = 0; i < 10; i++)
    {
        insert_sorted(&list, rand() % 100);
    }
    printf("Sorted list of 10 random numbers: \n");

    // TODO 6: Print the nodes using a for loop

    // TODO 7: free this list

}

void free_list(node* n)
{
    // TODO 2: Write free_list, which should free every node in your linked list
    return;
}

void insert_sorted(node** list, int num)
{
    node* n = malloc(sizeof(node));
    n->num = num;
    if (list == NULL || num < (*list)->num)
    {
        n->next = *list;
        *list = n;
    }
    else
    {
        node *ptr = *list;
        while (ptr->next != NULL && num > ptr->next->num)
        {
            ptr = ptr->next;
        }
        n->next = ptr->next;
        ptr->next = n;
    }
    return;
}

void free_list_alt(node* n)
{
    // TODO 8 (bonus): If you wrote free_list recursively, write it iteratively, and vice versa!
    return;
}