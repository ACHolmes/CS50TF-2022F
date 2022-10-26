#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <stdbool.h>
// #include "helper.h"

#define LENGTH 20

typedef struct pokemon
{
    char name[LENGTH];
    int type;
    int stage;
    int generation;
    bool legendary;
    struct pokemon* next;
} pokemon;

#define SIZE 18

bool do_nothing(void)
{
    printf("it did something");
    return true;
}

// bool load_dictionary(pokemon dictionary[], int size, char* filename)
// {
    
// }
