#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

void print_name(string name);

string DEFAULT = "\033[0m"; // default colour

string colors[4] = {
    "\033[0;32m", // Green
    "\033[0;31m", // Red
    "\033[0;33m", // Yellow
    "\033[0;34m" // Blue
};



int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./intro numPeople\n");
        return 1;
    }
    int numPeople = atoi(argv[1]);
    string names[numPeople];
    string partners[numPeople];
    string info[numPeople];
    for (int i = 0; i < numPeople; i++)
    {
        names[i] = get_string("What's your name? ");
        partners[i] = get_string("Who was your partner? ");
        info[i] = get_string("Tell us a bit about your partner: ");
        printf("\n");
    }
    printf("%s ---== Welcome to Andrew's CS50 lab! ==--- %s\n", colors[0], DEFAULT);
    for (int i = 0; i < numPeople; i++)
    {
        print_name(names[i]);
        printf(" was partnered with ");
        print_name(partners[i]);
        printf("\n A little bit about %s: %s\n", partners[i], info[i]);
    }

}

void print_name(string name)
{
    printf("%s%s%s", colors[rand()%4], name, DEFAULT);
}

