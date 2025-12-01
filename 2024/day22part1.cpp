#include <cstdio>
#include <vector>
using namespace std;

inline long mix(long a, long b) {
    return a ^ b;
}

inline long prune(long x) {
    return x & 0xFFFFFF;
}

int main() {
    vector<long> secretNumbers;
    long in;

    while (scanf("%ld\n", &in) > 0) {
        secretNumbers.push_back(in);
    }

    for (long i = 0; i < 2000; ++i) {
        for (long& i : secretNumbers) {
            i = prune(mix(i, i << 6));
            i = prune(mix(i, i >> 5));
            i = prune(mix(i, i << 11));
        }
    }

    long sum = 0;
    for (const long i : secretNumbers) {
        sum += i;
    }
    printf("%ld\n", sum);
    return 0;
}

