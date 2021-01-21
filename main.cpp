#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "file_io.hpp"

void get_file_details(File *file_ptr)
{
    std::string filename;
    char delimitor;
    char headers;

    std::cout << "Welcome to the file processing program" << std::endl;
    std::cout << "Name of file to open: " << std::endl;
    std::cin >> filename;

    std::cout << "Delimitor used in file [,] or [-] or [|] " << std::endl;
    std::cin >> delimitor;

    std::cout << "Does it have headers in first row (y/n) " << std::endl;
    std::cin >> headers;

    file_ptr->set_details(filename, delimitor, headers);

    return;
}

int main()
{
    // std::string filename = get_user_filename();
    File my_file;
    get_file_details(&my_file);


    if ( my_file.open_file() == OK )
    {
        // my_file.print_titles();
    }

    // look up ingredient "pasta"
    std::string ingredient;
    std::cout << "Enter an ingredient to look up in recipe list: " << std::endl;
    std::cin >> ingredient;

    if ( my_file.look_up_word(ingredient) > 0 )
        my_file.print_matches(); 
    else std::cout << "Sorry, no matches found\n";


    // look up by recipe name
    int results = my_file.look_up_title("pesto");
    if ( results > 0 )
        my_file.print_matches();
    // print all all recipes stored
    my_file.print_titles();

    

}