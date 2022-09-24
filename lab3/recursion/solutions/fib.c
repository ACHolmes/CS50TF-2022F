#include <stdio.h>

int fib_n(int n);

int main(void)
{
    printf("The 5th Fibonacci number is: ");
    printf("%i\n", fib_n(5));
}

int fib_n(int n)
{
    // Your code here
    // Write a function that returns the nth Fibonacci number
    // Desired functionality: 
    // fib(0): prints 1
    // fib(1) prints 1
    // fib(2) prints 2 etc
    if (n == 0 || n == 1)
    {
        return 1;
    }
    return fib_n(n - 1) + fib_n(n - 2);
}