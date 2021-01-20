#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "file_io.hpp"
#include <string>

#define OK  true

TEST_CASE("open file")
{
    std::string filename = "file.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == OK);
    REQUIRE(my_file.open_file() == OK );
}

TEST_CASE("print titles")
{
    std::string filename = "file.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == OK);
    REQUIRE(my_file.open_file() == OK );

    REQUIRE(my_file.print_titles() == OK);
}

TEST_CASE("look up word")
{
    std::string filename = "file.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == OK);
    REQUIRE(my_file.open_file() == OK );

    std::string word = "hello";
    REQUIRE(my_file.look_up_word(word) == OK);

}
