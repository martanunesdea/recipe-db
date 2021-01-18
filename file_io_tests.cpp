#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "file_io.hpp"
#include <string>


TEST_CASE("set filename", "[classic]")
{
    std::string name = "marta";
    REQUIRE(set_name(name) == "marta");
}

TEST_CASE("open file")
{
    std::string filename = "file.txt";
    char delimitor = ',';
    bool headers = false;
    File my_file;
    REQUIRE(my_file.set_details(filename, delimitor, headers) == true);
    REQUIRE(my_file.open_file() == true );
}

TEST_CASE("process rows")
{
    File my_file;
    REQUIRE(my_file.process_rows() == true);
}