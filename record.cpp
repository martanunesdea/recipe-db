/* Source file for Record class */
#include "record.hpp"


void Record::clear_matches()
{
    this->word_matches = {};

}
bool Record::set_entries(std::vector<std::vector<std::string>> data)
{
    this->entries = data;
    return true;
}

int Record::look_up_word(std::string word)
{
    this->clear_matches();
    int counter = 0;
    std::vector<std::string> x;
    for ( auto i = 0; (i < this->entries.size()); i++)
    {
        x = this->entries[i];
        for ( int j = 0; j < x.size(); j++ )
        {
            if ( word.compare(x[j]) == 0)
            {
                counter++;
                this->word_matches.push_back(x);
            }
        }
    }
    return counter;
}

int Record::look_up_title(std::string title)
{
    this->clear_matches();
    int counter = 0;
    std::vector<std::string> x;
    for ( auto i = 0; (i < this->entries.size()); i++ )
    {
        x = this->entries[i];
        if ( title.compare(x[0]) == 0)
        {
            counter++;
            this->word_matches.push_back(x);
        }
    }
    return counter;
}

std::vector<std::vector<std::string>> Record::get_matches()
{    
    return this->word_matches;
}

std::vector<std::string> Record::get_titles()
{
    std::vector<std::string> titles;
    for ( int i = 0; i < this->entries.size(); i++)
    {
        titles.push_back(this->entries[i][0]);
    }
    return titles;
}