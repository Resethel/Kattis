// Using c++
// https://open.kattis.com/problems/twostones


#include <iostream>

int main()
{
    int stones;
    std::cin >> stones;
    std::cout << ((!(stones % 2)) ? "Bob" : "Alice");
}
