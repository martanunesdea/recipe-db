/* Source code for reading in files */

#include <cstdio>
#include <iostream>
#include <istream> // for getline
#include <sstream> // for istringstream
#include <fstream>
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
    while (std::getline(file_handle, row))
    {
        this->rows.push_back(row);
        std::istringstream full_line(row);
        // entries.push_back(first_entry);
        Entry first_entry;
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
            first_entry.add(entry);
        }
        entries.push_back(first_entry);
        first_entry.clear();

    }
    return OK;
}

std::vector<Entry> File::get_all()
{
    return this->entries;
}

/* write to file */ 
bool File::save_record(Record *record_ptr)
{
    std::vector<Entry> entries = record_ptr->get_entries();
    std::ofstream file;
    file.open(this->filename);

    for ( int i = 0; i < entries.size(); i++ )
    {
        Entry x = entries[i];
        for ( int j = 0; j < x.size(); j++)
        {
            file << entries[i].pos(j) << this->delimitor;
        }
        file << "\n";
    }
    file.close();
    return OK; 
}
