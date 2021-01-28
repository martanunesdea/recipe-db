/* Header file for reading in files 
 * Author: Marta
 * Date: 16/01/2021
 * Compiler: clang v11
 */

#ifndef FILE_IO_HPP
#define FILE_IO_HPP

#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector> 
#include <string>
#include "record.hpp"

#define OK      true
#define NOK     false

std::string set_name(std::string filename);


class File {
    private:
        std::string filename;
        std::ifstream file_handle;
        char delimitor;
        bool headers;
        std::vector<std::vector<std::string>> entries;
        std::vector<std::string> single_entries;
        std::vector<std::string> header_row;
        std::vector<std::string> rows;

    public:
        File() {}
        File(std::string in_filename) : filename(in_filename) {}
        File(std::string in_filename, char in_delim, bool in_headers)
            : filename(in_filename), delimitor(in_delim), headers(in_headers){}
        bool set_details(std::string name, char delimitor, bool headers);
        bool open_file();
        std::vector<std::vector<std::string>> get_all();
        bool save_record(Record *record_ptr);

};

#endif