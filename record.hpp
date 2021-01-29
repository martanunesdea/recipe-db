/* Header file for processed data */
#ifndef RECORD_HPP
#define RECORD_HPP

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include "entry.hpp"

#define OK  true
#define NOK false

typedef std::string word;
typedef std::string title;

class Record {
    private: 
        std::vector<Entry> entries;
        std::vector<Entry> word_matches;
        void clear_matches();
        bool changed;

    public:
        bool set_entries(std::vector<Entry>);
        std::vector<Entry> get_entries();
        int look_up_word(word);
        int look_up_title(title);
        std::vector<Entry> get_matches();
        std::vector<title> get_titles();
        bool add_entry(Entry recipe);
        void set_changed_flag(bool changed);
        bool get_changed_flag();


};


#endif