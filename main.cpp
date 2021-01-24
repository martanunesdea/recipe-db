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
void print_titles(File *my_file)
{
    auto titles = my_file->get_titles();

    for ( int i = 0; i < titles.size(); i++ )
    {
        std::cout << i+1 << ". " << titles[i] << std::endl;
    }
    std::cout << std::endl;
}

void print_all(File *my_file)
{
    auto records = my_file->get_all();

    for ( int i = 0; i < records.size(); i++ )
    {
        auto line = records[i];
        for ( int j = 0; j < line.size(); j++ )
        {
            std::cout << line[j] << " ";
        } 
        std::cout << "\n\n";
    }

    std::cout << std::endl;  

}
void print_matches(File *my_file)
{
    auto matches = my_file->get_matches();
    for ( int i = 0; i < matches.size(); i++)
    {
        std::cout << matches[i][0] << std::endl;
        for ( int j = 1; j < matches[i].size(); j++)
        {
            std::cout << "\t" << j << ". " << matches[i][j] << std::endl;
        }
    }
    std::cout << std::endl;
}
void look_up_word(File *my_file)
{
    // look up ingredient "pasta"
    std::string ingredient;
    std::cout << "Enter an ingredient to look up in recipe list: " << std::endl;
    std::cin >> ingredient;

    if ( my_file->look_up_word(ingredient) > 0 )
        print_matches(my_file);
    else std::cout << "Sorry, no matches found\n";

}

void look_up_recipe(File *my_file)
{
    std::string recipe;
    std::cout << "Enter the recipe name to look up: " << std::endl;
    std::cin >> recipe;

    if ( my_file->look_up_title(recipe) > 0 )
        print_matches(my_file);
    else std::cout << "Sorry, no matches found\n";
}

int main()
{
    // std::string filename = get_user_filename();
    File my_file;
    get_file_details(&my_file);


    if ( my_file.open_file() != OK )
    {
        std::cout << "Sorry, couldn't open file " << std::endl;
    }

    while ( true )
    {
        char input;
        std::cout << "\n\nPlease enter a selection from the menu: \n";
        std::cout << "A. Print all record titles\n";
        std::cout << "B. Print all record titles and details\n";
        std::cout << "C. Look up ingredient in recipes\n";
        std::cout << "D. Look up recipe\n";
        std::cout << "E. Add recipe\n";
        std::cout << "F. Edit recipe\n";
        std::cout << "Q. Quit\n";
        std::cin >> input;
        
        switch(input)
        {
            case 'A':
                print_titles(&my_file);
                break;
            case 'B':
                print_all(&my_file);
                break;
            case 'C':
                look_up_word(&my_file);
                break;
            case 'D':
                look_up_recipe(&my_file);
                break;
            case 'E': 
                // add new recipe
                break;
            case 'F':
                // edit recipe
                break;
            case 'Q':
                std::cout << "Quitting...\n\n";
                return 0;
        }
                
    }

}