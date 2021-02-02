#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "file_io.hpp"
#include <string>

#define OK  true

TEST_CASE("open file")
{
    std::string filename = "test.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == OK);
    REQUIRE(my_file.open_file() == OK );
}

TEST_CASE("get file contents")
{
    std::string filename = "test.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == OK);
    REQUIRE(my_file.open_file() == OK );

    std::vector<Entry> contents = my_file.get_all();
    REQUIRE(contents.size() != 0 );
}

TEST_CASE("save file")
{
    // TODO: Complete - function needs fixing    
}