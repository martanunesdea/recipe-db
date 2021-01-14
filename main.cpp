#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>

const bool OK = true;
const bool NOK = false;

std::string get_user_filename()
{
    std::string filename;

    std::cout << "Enter the name of the file you wish to process: " << std::endl;
    std::cin >> filename;

    std::cout << "Got file with name: " << filename << std::endl;
    // check if file exists in directory
    return filename;
}


int main()
{
    std::cout << "Welcome to the file processing program" << std::endl;
    // get user
    std::string filename = get_user_filename();
    
    std::ifstream file(filename);

    std::string line;
    if (file.is_open())
    {
        while ( std::getline(file,line) )
        {
            std::cout << line << '\n';
        }
        file.close();
    }
    else std::cout << "Unable to open file"; 

}