#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int check_format(uint8_t header[]);
int get_block_size(uint8_t header[]);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1

    // Open input file for reading
    // TODO #2

    // Read header into an array
    // TODO #3
    
    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(uint8_t header[])
{
    // TODO #4
    return 0;
}

int get_block_size(uint8_t header[])
{
    // TODO #7
    return 0;
}