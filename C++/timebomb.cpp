// Timebomb
// Using C++
// https://open.kattis.com/problems/timebomb

#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(int argc, char** argv)
{
    int n;
    string line;
    vector<string> data(10,"");
    map<std::string, int> dict = {
            {"**** ** ** ****", 0},
            {"  *  *  *  *  *", 1},
            {"***  *****  ***", 2},
            {"***  ****  ****", 3},
            {"* ** ****  *  *", 4},
            {"****  ***  ****", 5},
            {"****  **** ****", 6},
            {"***  *  *  *  *", 7},
            {"**** ***** ****", 8},
            {"**** ****  ****", 9}};

    for(int l = 0; l < 5; ++l)
    {
        getline(cin, line);
        n = line.size()/4 + 1;
        for(int i = 0; i < n; ++i)
        {
            data[i] += line.substr(i*4, 3);
        }
    }

    int ans = 0;

    for(int i = 0; i < n; ++i)
    {
        if(dict.find(data[i]) != dict.end())
        {
            ans *= 10;
            ans += dict[data[i]];
        }
        else
        {
            cout << "BOOM!!";
            return 0;
        }
    }

    if(ans%6 == 0)
    {
        cout << "BEER!!";
    }
    else
    {
        cout << "BOOM!!";
    }

    return 0;

}
