/* Source code for reading in files */

#include <cstdio>
#include <iostream>
#include <istream> // for getline
#include <sstream> // for istringstream
#include "file_io.hpp"

void File::set_filename(std::string name)
{
    this->filename = name;
}

std::string File::get_filename()
{
    return this->filename;
}

bool File::set_details(std::string name, char delimitor, bool headers)
{
    this->filename = name;
    this->delimitor = delimitor;
    this->headers = headers;
    return OK;
}

bool File::open_file()
{
    std::ifstream file_handle(this->filename);

    if ( !file_handle.is_open() )
    {
        std::cout << "Couldn't open file, returning..." << std::endl;
        return NOK;
    }

    std::string row;
    std::string entry;
    bool first_line = true;
    int i = 0, j = 0;
    while (std::getline(file_handle, row))
    {
        this->rows.push_back(row);
        std::istringstream full_line(row);
        entries.push_back(std::vector<std::string> ());

        while (std::getline(full_line, entry, this->delimitor))
        {
            if (this->headers && first_line)
            {
                this->header_row.push_back(entry);
                first_line = false;
            }
            else
            {
                this->single_entries.push_back(entry);
            }
            entries[i].push_back(entry);
            j++;
        }
        i++;
        std::cout << std::endl;
    }
    return OK;
}

bool File::print_titles()
{
    std::vector<std::string> titles;
    int j = 0;
    for ( auto i = this->entries.begin(); (i < this->entries.end()); i++)
    {
        std::string x = this->entries[j][0];
        std::cout << x << "\n" << std::endl;
        j++;
    }
    return OK;
}

bool File::look_up_word(std::string word)
{
    int counter = 0;
    std::vector<std::string> matches;
    for ( auto i = 0; (i < this->entries.size()); i++)
    {
        std::vector<std::string> x = this->entries[i];
        for ( int j = 0; j < x.size(); j++ )
        {
            if ( word.compare(x[j]) == 0)
            {
                counter++;
                matches.push_back(x[0]);
                std::cout << "Matched in " << x[0] << std::endl;
            }
        }
    }
    if ( counter == 0)
    {
        std::cout << "No matches found" << std::endl;
    }
    return OK;
}