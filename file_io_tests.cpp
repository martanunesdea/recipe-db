#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "file_io.hpp"
#include <string>
TEST_CASE("set filename", "[classic]")
{
    std::string name = "marta";
    REQUIRE(set_name(name) == "marta");
}