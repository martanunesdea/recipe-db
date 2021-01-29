#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "file_io.hpp"
#include "record.hpp"

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
void print_titles(Record *my_record)
{
    auto titles = my_record->get_titles();

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
        Entry line = records[i];
        for ( int j = 0; j < line.size(); j++ )
        {
            std::cout << line.pos(j) << " ";
        } 
        std::cout << "\n\n";
    }

    std::cout << std::endl;  

}
void print_matches(Record *my_record)
{
    auto matches = my_record->get_matches();
    for ( int i = 0; i < matches.size(); i++)
    {
        std::cout << matches[i].pos(0) << std::endl;
        for ( int j = 1; j < matches[i].size(); j++)
        {
            std::cout << "\t" << j << ". " << matches[i].pos(j) << std::endl;
        }
    }
    std::cout << std::endl;
}
void look_up_word(Record *my_record)
{
    std::string ingredient;
    std::cout << "Enter an ingredient to look up in recipe list: " << std::endl;
    std::cin >> ingredient;

    if ( my_record->look_up_word(ingredient) > 0 )
        print_matches(my_record);
    else std::cout << "Sorry, no matches found\n";

}

void look_up_recipe(Record *my_record)
{
    word recipe;
    std::cout << "Enter the recipe name to look up: " << std::endl;
    std::cin >> recipe;

    if ( my_record->look_up_title(recipe) > 0 )
        print_matches(my_record);
    else std::cout << "Sorry, no matches found\n";
}

void add_new_recipe(Record *record_ptr)
{
    std::string recipe_title;
    Entry recipe;

    std::cout << "Enter the recipe name to enter: " << std::endl;
    std::cin >> recipe_title;
    recipe.add(recipe_title);
    
    std::string ingredient;
    while ( true )
    {
        std::cout << "Enter ingredient name or enter Q to quit: " << std::endl;
        std::cin >> ingredient;
        if ( ingredient == "Q" || ingredient == "q" )
        {
            break;
        }
        recipe.add(ingredient);
    }

    if ( record_ptr->add_entry(recipe) != OK )
    {
        std::cout << "Error committing new changes...\n";
    }
    else {
        std::cout << "New recipe added.\n";
    }

    record_ptr->set_changed_flag(true);
    
}

void save_changes(Record *record_ptr, File *file_ptr)
{
    if ( record_ptr->get_changed_flag() )
    {
        file_ptr->save_record(record_ptr);
    }
}



int main()
{
    File my_file;
    get_file_details(&my_file);
    Record my_record;

    if ( my_file.open_file() != OK )
    {
        std::cout << "Sorry, couldn't open file\n";
        return 0;
    }

    if ( my_record.set_entries(my_file.get_all()) != true )
    {
        std::cout << "Error in processing data\n";
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
        std::cout << "Q. Quit\n";
        std::cin >> input;
        
        switch(input)
        {
            case 'A':
                print_titles(&my_record);
                break;
            case 'B':
                print_all(&my_file);
                break;
            case 'C':
                look_up_word(&my_record);
                break;
            case 'D':
                look_up_recipe(&my_record);
                break;
            case 'E': 
                add_new_recipe(&my_record);
                break;
            case 'Q':
                save_changes(&my_record, &my_file);
                std::cout << "Quitting...\n\n";
                return 0;
        }
                
    }

}