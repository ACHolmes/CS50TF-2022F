#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 45

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int main(void)
{
    // Placeholder
    char placeholder[LENGTH] = "placeholder";
    // Node initialization (don't worry about this notation)
    node n = {.word = "Appears", .next = NULL};
    
    // TODO 1: Print the word stored in n
    printf("%s\n", n.word);

    // TODO 2: Use malloc to create a new node
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Memory error");
        return 1;
    }

    // TODO 3: Store the word "twice" in your new node using strcpy
    strcpy(new->word, "twice");

    // TODO 4: print it by acessing the node with TWO DIFFERENT NOTATIONS
    printf("%s\n", (*new).word);
    printf("%s\n", new->word);


    // TODO 5: free any malloced memory
    free(new);
}