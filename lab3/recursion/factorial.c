#include <stdio.h>

int factorial(int n);
int factorial_iter(int n);

int main(void)
{
    printf("Recursive method, 5! = %i\n", factorial(5));
    printf("Iterative method, 5! = %i\n", factorial_iter(5));
}

int factorial(int n)
{
    // Implement a recursive function that returns n!
    // 1! = 1
    // 2! = 2 * 1 = 2
    // 3! = 3 * 2 * 1 = 6
    return 1;
}

int factorial_iter(int n)
{
    int result = 1;
    for (int i = 2; i <= n; i++)
    {
        result *= i;
    }
    return result;
}