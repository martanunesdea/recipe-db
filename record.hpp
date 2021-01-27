/* Header file for processed data */
#ifndef RECORD_HPP
#define RECORD_HPP

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>

#define OK  true
#define NOK false

class Record {
    private: 
        std::vector<std::vector<std::string>> entries;
        std::vector<std::vector<std::string>> word_matches;
        void clear_matches();
        bool changed;

    public:
        bool set_entries(std::vector<std::vector<std::string>>);
        int look_up_word(std::string word);
        int look_up_title(std::string title);
        std::vector<std::vector<std::string>> get_matches();
        std::vector<std::string> get_titles();
        std::vector<std::vector<std::string>> get_all();
        bool add_entry(std::vector<std::string> recipe);
        void set_changed_flag(bool changed);
        bool get_changed_flag();


};


#endif