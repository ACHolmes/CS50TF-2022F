#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

string prompts[8] = {"Favourite music genre, artist and song: ",
                     "Give us a fact you find interesting: ",
                     "Cats or dogs? Morning or evening?  ",
                     "Favourite book, movie, story or similar? ",
                     "Where are you from: ",
                     "Favourite place you've visited: ",
                     "Place you most want to visit: ",
                     "Favourite place on campus: "
                    };


// Group 1
int main()
{
    if (argc != 2)
    {
        printf("Usage: ./intro numPeople\n");
        return 1;
    }
    // Group 2 (Note: a function from CS50 manual may be useful to fix one of the issues here)
    int numPeople = argv[1];
    string names[numPeople];
    string promptsUsed[numPeople];
    string info[numPeople];
    for (int i = 0; i <= numPeople; i++)
    {
        names[i] = get_string("What's your name? ");
        // Group 3
        promptsUsed[i] = prompts[i];
        info[i] = get_string("%s", prompts[i]);
    }
    printf("\n");

    // Don't touch the code below!
    for (int i = 0; i < numPeople; i++)
    {
        printf("Welcome %s!", names[i]);
        printf("\033[0;34m  %s \033[0m %s\n", promptsUsed[i], info[i]);
    }

}