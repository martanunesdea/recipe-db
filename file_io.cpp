/* Source code for reading in files */

#include <cstdio>
#include <iostream>
#include <istream> // for getline
#include <sstream> // for istringstream
#include "file_io.hpp"
#include "catch.hpp"

void File::set_filename(std::string name)
{
    this->filename = name;
}

std::string File::get_filename()
{
    return this->filename;
}

void File::set_details(std::string name, char delimitor, bool headers)
{
    this->filename = name;
    this->delimitor = delimitor;
    this->headers = headers;
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

    while (std::getline(file_handle, row))
    {
        this->rows.push_back(row);
        std::istringstream full_line(row);
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
            std::cout << entry << ' ';
        }
        std::cout << std::endl;
    }
    return OK;
}

bool File::process_rows()
{
    return OK;
}

std::string set_name(std::string filename)
{
    return filename;
}
