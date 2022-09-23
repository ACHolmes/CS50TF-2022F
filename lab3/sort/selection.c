#include <stdio.h>

#define LENGTH 7

int main(void)
{
    int numbers[] = {1, 4, -2, 3, 5, 2, 7};
    // Selection sort
    for (int i = 0; i < LENGTH; i++)
    {
        int min = i;
        for (int j = i; j < LENGTH; j++)
        {
            if (numbers[j] < numbers[min])
            {
                min = j;
            }
        }
        // Switch the lowest to the front of the unsorted portion
        int temp = numbers[min];
        numbers[min] = numbers[i];
        numbers[i] = temp;
    }
    // Printing result
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
}