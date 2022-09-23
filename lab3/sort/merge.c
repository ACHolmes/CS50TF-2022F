#include <stdio.h>

void print_merged(int left[], int left_len, int right[], int right_len);

int main(void)
{
    int left[3] = {1, 3, 6};
    int right[4] = {2, 3, 5, 7};
    print_merged(left, 3, right, 4);
}

void print_merged(int left[], int left_len, int right[], int right_len)
{
    int i = 0, j = 0;
    while (i < left_len && j < right_len)
    {
        if (left[i] < right[j])
        {
            printf("%i ", left[i]);
            i++;
        }
        else
        {
            printf("%i ", right[j]);
            j++;
        }
    }
    while (i < left_len)
    {
        printf("%i ", left[i]);
        i++;
    }
    while (j < right_len)
    {
        printf("%i ", right[j]);
        j++;
    }
    printf("\n");

}