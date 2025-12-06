#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdint>
#include <cstdio>

using namespace std;

using u64 = uint64_t;

inline bool inclusive_in_range(u64 lo, u64 hi, u64 n) {
    return lo <= n && n <= hi;
}

inline bool inclusive_in_range(const pair<u64, u64> range, u64 n) {
    return inclusive_in_range(range.first, range.second, n);
}

int main() {
    std::vector<pair<u64, u64> > fresh;

    u64 lo, hi;

    // scope
    {
        FILE* fin = fopen("5.in", "r");
        u64 x, y;
        while (fscanf(fin, "%lu-%lu\n", &x, &y) > 0) {
            fresh.push_back({ x, y });
            lo = min(x, lo);
            hi = max(y, hi);
        }
        fclose(fin);
    }

    u64 res = 0;

    for (u64 i = lo; i != hi + 1; ++i) {
        for (const auto& p : fresh) {
            if (inclusive_in_range(p, i)) {
                ++res;
                goto continue_outer;
            }
        }
        // please don't kill me for the use of goto
        continue_outer:;
    }

    cout << res << endl;

    return 0;
}
