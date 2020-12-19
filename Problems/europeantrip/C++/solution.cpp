// Using C++
// https://open.kattis.com/problems/europeantrip

#include <cmath>
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;
typedef long double ld;

ld dist(ld x1, ld y1, ld x2, ld y2)
{
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2));
}

ld distSum(ld x1, ld y1, ld x2, ld y2, ld x3, ld y3, ld x, ld y)
{
    ld sum = 0;
    sum += dist(x1, y1, x, y);
    sum += dist(x2, y2, x, y);
    sum += dist(x3, y3, x, y);
    return sum;
}

int main()
{
    ld x1, y1;
    ld x2, y2;
    ld x3, y3;

    // Input
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // Getting the
    ld x = (x1+x2+x3) / 3;
    ld y = (y1+y2+y3) / 3;

    ld best = distSum(x1, y1, x2, y2, x3, y3, x, y);

    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    ld t = 1000;
    while(t > .00001)
    {
        bool flag = false;
        for(int i = 0; i < 4; i++)
        {
            ld nextx = x + t * dx[i];
            ld nexty = y + t * dy[i];
            ld val = distSum(x1, y1, x2, y2, x3, y3, nextx, nexty);
            if(val < best)
            {
                flag = true;
                best = val;
                x = nextx;
                y = nexty;
            }
        }

        if(!flag)
        {
            t /= 2;
        }
    }

    // Printing
    cout << fixed << setprecision(5);
    cout << x << " " << y << endl;
}
