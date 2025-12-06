#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <iterator>
#include <algorithm>

#include <cstdint>
#include <cstdio>

using namespace std;

using u64 = uint64_t;
using u64pair = pair<u64, u64>;

void merge_overlapping_ranges(list<u64pair>& ranges) {
    ranges.sort();
    auto it1 = ranges.begin();
    while (it1 != ranges.end() && next(it1) != ranges.end()) {
        auto& pa = *it1;
        auto& pb = *(next(it1));
        if (pa.second < pb.first) {
            ++it1;
            continue;
        }
        if (pa.first == pb.first || pa.second >= pb.first) {
            pa.second = max(pa.second, pb.second);
            ranges.erase(next(it1));
            // pb is no longer valid here
        }
    }
}

int main() {
    list<u64pair> fresh;

    {
        FILE* fin = fopen("5.in", "r");
        u64 x, y;
        while (fscanf(fin, "%lu-%lu\n", &x, &y) == 2) {
            fresh.push_back({ x, y });
        }
        fclose(fin);
    }

    merge_overlapping_ranges(fresh);

    u64 res = 0;

    for (const auto& p : fresh) {
        res += p.second - p.first + 1;
    }

    cout << res << endl;

    return 0;
}
