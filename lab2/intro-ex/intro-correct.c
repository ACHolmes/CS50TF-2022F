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

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./intro numPeople\n");
        return 1;
    }
    int numPeople = atoi(argv[1]);
    string names[numPeople];
    string promptsUsed[numPeople];
    string info[numPeople];
    for (int i = 0; i < numPeople; i++)
    {
        names[i] = get_string("What's your name? ");
        promptsUsed[i] = prompts[i % 8];
        info[i] = get_string("%s", prompts[i % 8]);
    }
    printf("\n");
    for (int i = 0; i < numPeople; i++)
    {
        printf("Welcome %s!", names[i]);
        printf("\033[0;34m  %s \033[0m %s\n", promptsUsed[i], info[i]);
    }

}

