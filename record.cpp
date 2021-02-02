/* Source file for Record class */
#include "record.hpp"
#include <cstdlib>
#include <iostream>
void Record::clear_matches()
{
    this->word_matches = {};

}

bool Record::set_entries(std::vector<Entry> data)
{
    this->entries = data;
    return OK;
}

std::vector<Entry> Record::get_entries()
{
    return this->entries;
}


void Record::set_changed_flag(bool changes)
{
    this->changed = changes;
}

bool Record::get_changed_flag()
{
    return this->changed;
}


int Record::look_up_word(word in_word)
{
    this->clear_matches();

    int counter = 0;
    for ( auto i = 0; (i < this->entries.size()); i++)
    {
        Entry x = this->entries[i];
        for ( int j = 0; j < x.size(); j++ )
        {
            if ( in_word.compare(x.pos(j)) == 0)
            {
                counter++;
                this->word_matches.push_back(x);
            }
        }
    }
    return counter;
}

int Record::look_up_title(title in_title)
{
    this->clear_matches();
    int counter = 0;
    for ( auto i = 0; (i < this->entries.size()); ++i )
    {
        Entry x = Entry(this->entries[i]);
        if ( in_title.compare(x.pos(0)) == 0)
        {
            counter++;
            std::cout << "found a match\n";
            this->word_matches.push_back(x);
        }
    }
    return counter;
}

std::vector<Entry> Record::get_matches()
{    
    return this->word_matches;
}

std::vector<std::string> Record::get_titles()
{
    std::vector<std::string> titles;
    for ( int i = 0; i < this->entries.size(); i++)
    {
        titles.push_back((this->entries[i]).pos(0));
    }
    return titles;
}

bool Record::add_entry(Entry recipe)
{
    this->entries.push_back(recipe);
    return OK;
}

bool Record::update_entry(Entry recipe)
{
    std::string recipe_title = recipe.pos(0);
    bool updated = false;
    for ( int i = 0; i < this->entries.size(); i++)
    {
        Entry x = Entry(this->entries[i]);
        if ( recipe_title.compare(x.pos(0)) == 0)
        {
            this->entries[i] = recipe;
            this->changed = true;
            updated = true;
            break;
        }
    }

    return updated;
}
