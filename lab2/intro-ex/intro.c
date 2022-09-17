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


// First mistake: we are using argc and argv[] in our code, thus we can't have int main(void),
// or even worse int main() (which works in C++)
// correct code is:
// int main(int argc, string argv[])
int main()
{
    if (argc != 2)
    {
        printf("Usage: ./intro numPeople\n");
        return 1;
    }
    // Second mistake, we can't assign argv[1] to an integer variable.
    // Note argv is declared as an array of strings. Thus to convert to an integer
    // we use the atoi function from stdlib.h
    // int numPeople = atoi(argv[1])
    int numPeople = argv[1];
    string names[numPeople];
    string promptsUsed[numPeople];
    string info[numPeople];
    for (int i = 0; i <= numPeople; i++)
    {
        names[i] = get_string("What's your name? ");
        // We have dangerous behaviour here: what if numPeople > 8, the number of prompts?
        // then prompts[i] might be invalid, since i can be at most 7 to index into the prompts array
        // to fix this, we use the % operator to ensure we never access memory we shouldn't
        // promptsUsed[i] = prompts[i % 8]
        // DESIGN POINT: This could be improved even more. 8 here is a 'magic number', when in reality it's a contstant
        // that we should be treating more carefully. What if I added a prompt? I'd have to change 8 everywhere in my code
        // best to define a constant variable to avoid these issues, potentitally using #define
        promptsUsed[i] = prompts[i];
        // Same issue as above ^, use prompts[i % 8]
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