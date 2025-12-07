/**
 * This solution is extremely slow for some reason and I would not recommend running it
 */

#include <vector>
#include <string>

#include <iostream>
#include <fstream>

using namespace std;

int n, m;

int traverse(vector<string>& data, int beam, int pos)
{
    if (!(0 <= beam && beam < m)) return 0;
    if (pos >= n) return 1;

    if (data[pos][beam] == '^')
        return traverse(data, beam - 1, pos + 1) + traverse(data, beam + 1, pos + 1);
    else
        return traverse(data, beam, pos + 1);
}

int main()
{
    vector<string> data;

    {
        ifstream ifs("7.in");

        string line;

        while (getline(ifs, line) && !line.empty()) {
            data.push_back(line);
        }
    }

    n = data.size();
    m = data[0].size();

    int beam;
    beam = data[0].find('S');

    cout << traverse(data, beam, 1) << endl;

    return 0;

}