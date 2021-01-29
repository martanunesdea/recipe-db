/* Header file for Entry class 
 * Author: Marta
 * Date: 29/01/2021
 * Compiler: clang v11
 */

#ifndef ENTRY_HPP
#define ENTRY_HPP

#include <cstdio>
#include <vector> 
#include <string>

#define OK      true
#define NOK     false

class Entry {
    private:
        std::vector<std::string> entry;
        int entry_length;

        
    public:
        Entry() {}
        Entry(std::vector<std::string> in_entry);
        Entry(std::vector<std::string> in_entry, int in_length)
            : entry(in_entry), entry_length(in_length){}
        Entry(const Entry & in_entry);
        int size();
        std::string pos(int position);
        void add(std::string word);
        bool print();
        void clear();

};

#endif