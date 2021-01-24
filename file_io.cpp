/* Source code for reading in files */

#include <cstdio>
#include <iostream>
#include <istream> // for getline
#include <sstream> // for istringstream
#include "file_io.hpp"

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
    }
    return OK;
}

std::vector<std::vector<std::string>> File::get_all()
{
    return this->entries;
}