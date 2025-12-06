#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <utility>

#include <cstdint>
#include <cstdio>

using namespace std;

using u64 = uint64_t;
using u64pair = pair<u64, u64>;

vector<u64pair> merge_overlapping_ranges(vector<u64pair> ranges) {
    sort(ranges.begin(), ranges.end());
    auto it1 = ranges.begin();
    while (it1 != ranges.end() && it1 + 1 != ranges.end()) {
        auto& pa = *it1;
        auto& pb = *(it1 + 1);
        if (pa.second < pb.first) {
            ++it1;
            continue;
        }
        if (pa.first == pb.first || pa.second >= pb.first) {
            pa.second = std::max(pa.second, pb.second);
            ranges.erase(it1 + 1);
            // pb is no longer valid here
        }
    }
    return ranges;
}

inline bool inclusive_in_range(u64 lo, u64 hi, u64 n) {
    return lo <= n && n <= hi;
}

inline bool inclusive_in_range(const u64pair range, u64 n) {
    return inclusive_in_range(range.first, range.second, n);
}

int main() {
    std::vector<u64pair> fresh;

    {
        FILE* fin = fopen("5.in", "r");
        u64 x, y;
        while (fscanf(fin, "%lu-%lu\n", &x, &y) == 2) {
            fresh.push_back({ x, y });
        }
        fclose(fin);
    }

    fresh = merge_overlapping_ranges(fresh);

    u64 res = 0;

    for (const auto& p : fresh) {
        res += p.second - p.first + 1;
    }

    cout << res << endl;

    return 0;
}
