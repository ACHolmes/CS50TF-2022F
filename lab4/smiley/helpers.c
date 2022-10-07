#include "helpers.h"
#include "rand.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if(image[i][j].rgbtBlue == 0)
            {
                image[i][j].rgbtBlue = rand() % 256;
                image[i][j].rgbtGreen = rand() % 256;
                image[i][j].rgbtRed = rand() % 256;
            }
        }
    }
}
