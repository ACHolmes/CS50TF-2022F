#include <cs50.h>
#include <stdio.h>
#include <math.h>

// American Express uses 15-digit numbers,
// All American Express numbers start with 34 or 37
// How does your program handle this input?
// 3400000000000620
// Compare this to the other version of credit

int sum_of_digits(int n)
{
    int sum = 0;
    while (n)
    {
        sum += (n % 10);
        n /= 10;
    }
    return sum;
}

int main(void)
{
    long number = get_long("Number: "), copy = number;
    int len = floor(log10(number)) + 1, sum = 0, digits[len], i = 1;

    printf("Length: %i\n", len);
    if (len != 13 && len != 15 && len != 16)
    {
        printf("%s\n", "INVALID");
        return 0;
    }
    bool odd = false;

    while (copy)
    {
        if (odd)
        {
            sum += sum_of_digits(2 * (copy % 10));
        }
        else
        {
            sum += (copy % 10);
        }

        digits[len - i] = (copy % 10);
        i++;
        copy /= 10;
        odd = !odd;
    }

    printf("Checksum: %i\n", sum);
    if (sum % 10 != 0)
    {
        printf("%s\n", "INVALID");
        return 0;
    }

    int start = digits[0] * 10 + digits[1];

    if (start == 34 || start == 37)
    {
        printf("%s\n", "AMEX");
    }
    else if (51 <= start && start <= 55)
    {
        printf("%s\n", "MASTERCARD");
    }

    else if (digits[0] == 4)
    {
        printf("%s\n", "VISA");
    }

    else
    {
        printf("%s\n", "INVALID");
    }

    return 0;
}