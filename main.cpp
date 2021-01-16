#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

const bool OK = true;
const bool NOK = false;

std::string get_user_filename()
{
    std::string filename;

    std::cout << "Enter the name of the file you wish to process: " << std::endl;
    std::cin >> filename;

    std::cout << "Opening file: " << filename << std::endl;
    // check if file exists in directory
    return filename;
}


char get_file_delimitor()
{
    char delimitor;
    std::cout << "Enter the type of delimitor: " << std::endl;
    std::cin >> delimitor;
    return delimitor;
}

void ask_for_headers(void)
{
    char has_headers;
    std::cout << "Does the file have headers? (y/n)" << std::endl;
    std::cin >> has_headers;
    if ( has_headers == 'y' )
    {
        // mark headers flag;
    }
    else {
        std::cout << "proceeding with normal file processing..." << std::endl; 
        return;
    }  
}

int main()
{
    std::cout << "Welcome to the file processing program" << std::endl;
    std::string filename = get_user_filename();
    char delim = get_file_delimitor();

    ask_for_headers();
    // ask if file has headers
    // std::string headers;
    // std::cout << "If the file has headers, please enter these in sequence separated by space" << std::endl;
    // std::cout << "Otherwise enter 'N' " << std::endl;
    // std::getline(std::cin, headers);

    std::ifstream file(filename);

    //std::vector<std::string> file_lines;
    //std::vector<std::string> words;
    if (file.is_open())
    {
        std::string line;
        while ( std::getline(file,line) )
        {
            std::istringstream full_line(line);
            std::string word;
            while( std::getline(full_line, word, delim))
            {
                std::cout << word << ' ';
            }
            std::cout << std::endl;
        }
        file.close();
    }
    else std::cout << "Unable to open file"; 


    /* 
    for ( std::string x: words) {
        std::cout << x << " " << std::endl;
    } */

}