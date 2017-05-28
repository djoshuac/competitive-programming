#include <vector>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int main() {
    long n, s, t, g, seed, p;
    cin >> n >> s >> t;
    vector<long> r(n);

    long zero = (0 + n - t) % n;
    s = (s + n - t) % n;
    t = 0;
    cin >> r[zero] >> g >> seed >> p;
    for (long i = (zero + 1) % n; i != zero; i = (i + 1) % n) {
        r[i] = (static_cast<long long>(r[(i + n - 1) % n]) * g + seed) % p;
    }

    if (s == t) {
      cout << 0 << endl;
      return 0;
    }

    auto getLow = [&](long i)->long{
        return (i - r[i]);
    };
    auto getHigh = [&](long i)->long{
        return (i + r[i]);
    };

    long l0 = s;
    long h0 = s;
    long l, low, h, high;
    l = getLow(s);
    h =  getHigh(s);
    long distance = 1;

    while (l < l0 || h > h0) {
        long l1 = l0;
        long h1 = h0;
        l0 = l;
        h0 = h;
        if (l0 == 0 || h0 == 0) {
            cout << distance << endl;
            return 0;
        }

        distance++;
        for (long i = h0; i != h1; i = (i - 1 + n) % n) {
            high = getHigh(i);
            if (high > h) {
                h = high;
            }
            low = getLow(i);
            if (low < l) {
                l = low;
            }

            if (low <= 0 || high >= n) {
                cout << distance << endl;
                return 0;
            }
        }

        for (long i = l0; i != l1; i = (i + 1) % n) {
            high = getHigh(i);
            if (high > h) {
                h = high;
            }
            low = getLow(i);
            if (low < l) {
                l = low;
            }

            if (low <= 0 || high >= n) {
                cout << distance << endl;
                return 0;
            }
        }
    }

    cout << -1 << endl;
    return 0;
}
