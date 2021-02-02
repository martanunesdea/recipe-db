/* Source code file for Entry class 
 * Author: Marta
 * Date: 29/01/2021
 * Compiler: clang v11
 */

#include "entry.hpp"
#include <iostream>


Entry::Entry(const Entry & in_entry)
{
    this->entry = in_entry.entry;
    this->entry_length = this->entry.size();
}


Entry::Entry(std::vector<std::string> in_entry)
{
    this->entry = in_entry;
    this->entry_length = in_entry.size();
}

std::string Entry::pos(int position)
{
    return this->entry[position];

}

int Entry::size()
{
    this->entry_length = this->entry.size();
    return this->entry_length;
}

void Entry::add(std::string word)
{
    this->entry.push_back(word);
}

void Entry::erase(std::string ingredient)
{
   this->entry.erase(std::remove(this->entry.begin(), this->entry.end(), ingredient), this->entry.end());
}

void Entry::clear()
{
    this->entry = {};
    this->entry_length = 0;
}

bool Entry::print()
{
    std::cout << "Recipe with length: "<< this->entry_length << std::endl;
    for ( int i  = 0; i < this->entry_length; ++i )
    {
        std::cout << this->entry[i] << std::endl;
    }
    return OK;
}