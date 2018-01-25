#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long gcd(long u, long v) {
    int shift;

    if (u == 0) return v;
    if (v == 0) return u;

    for (shift = 0; ((u | v) & 1) == 0; ++shift) {
        u >>= 1;
        v >>= 1;
    }

    while ((u & 1) == 0)
        u >>= 1;

    do {
        while ((v & 1) == 0)
            v >>= 1;

        if (u > v) {
            long t = v;
            v = u;
            u = t;
        }
        v = v - u;
    } while (v != 0);

    return u << shift;
}

long maximum_gcd_sum(vector<long> &a, vector<long> &b) {
    long g = 1;
    long s = 2;

    for (const auto& u : a) {
        for (const auto& v : b) {
            long g1 = gcd(u, v);
            if (g < g1) {
                g = g1;
                s = u + v;
            }
        }
    }

    return s;
}

int main() {
    bool in_a[1000001] = {false};
    bool in_b[1000001] = {false};

    vector<long> a;
    vector<long> b;

    int n;
    cin >> n;

    a.reserve(n);
    b.reserve(n);

    for (int i = 0; i < n; i++) {
        long t;
        cin >> t;
        if (!in_a[t]) {
          a.push_back(t);
          in_a[t] = true;
        }
    }
    for (int i = 0; i < n; i++) {
        long t;
        cin >> t;
        if (!in_b[t]) {
          b.push_back(t);
          in_b[t] = true;
        }
    }

    cout << maximum_gcd_sum(a, b) << endl;

    return 0;
}
