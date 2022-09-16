#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 16
#define AMEX_LENGTH 15
#define INVALID_LENGTH 14
#define MIN_LENGTH 13

int main(void)
{
    // obtain cc number from user
    bool is_word = false;
    int cc_len;
    string cc_num;
    do
    {
        is_word = false;
        cc_num = get_string("Number: ");
        cc_len = strlen(cc_num);
        if (cc_len <= 0)
            is_word = true;

        for(int i = 0; i < cc_len; i++)
        {
            if (!isdigit(cc_num[i]))
            {
                is_word = true;
                break;
            }
        }
    }
    while(is_word);

    // check to make sure card is not too long or short
    if (cc_len < MIN_LENGTH || cc_len > MAX_LENGTH || cc_len == INVALID_LENGTH)
    {
        printf("INVALID\n");
        return 0;
    }

    // check to make sure every digit is valid
    // variable to hold the checksum
    int checksum = 0;

    // read the string, right-to-left
    for(int counter = 1; counter <= cc_len; counter++)
    {
        // extract the character, convert to actual integer value
        int digit = (cc_num[cc_len - counter]) - '0';

        // every second digit, right to left, needs to be doubled
        if (counter % 2 == 0)
        {
            // if the doubled value > 10, add the two digits together
            // the first digit is always 1 if this happens
            checksum += (digit < 5) ? (2 * digit) : ((2 * digit) % 10) + 1;
        }
        else
        {
            checksum += digit;
        }
    }

    // check to make sure checksum is valid
    if ((checksum % 10) != 0)
    {
        printf("INVALID\n");
    }

    // NOTE: We can check the checksum separately - we require a valid checksum for all card types
    // We cannot check the length and the first one/two digits separately - as this leads to problems
    // Where we have a valid length and valid leading digits, but not the length that correspond
    // to the corresponding digits

    // perform VISA checks (starts with 4, is either 13 or 16 digits)
    else if (cc_num[0] == '4' && (cc_len == MIN_LENGTH || cc_len == MAX_LENGTH))
    {
        printf("VISA\n");
    }

    // perform MASTERCARD check (starts with 51-55, is 16 digits)
    else if (cc_num[0] == '5' && (cc_num[1] >= '1' && cc_num[1] <= '5') && cc_len == MAX_LENGTH)
    {
        printf("MASTERCARD\n");
    }

    // perform AMEX check (starts with 34 or 37, is 15 digits)
    else if (cc_num[0] == '3' && (cc_num[1] == '4' || cc_num[1] == '7') && cc_len == AMEX_LENGTH)
    {
        printf("AMEX\n");
    }

    // otherwise must not be MASTERCARD, VISA, or AMEX
    else
    {
        printf("INVALID\n");
    }

    return 0;
}