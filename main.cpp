#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> h(n);
        for (int i = 0; i < n; i++)
        {
            cin >> h[i];
        }

        vector<int> k(n);
        for (int i = 0; i < n; i++)
        {
            cin >> k[i];
        }
        int maxDist = 2 * (*max_element(h.begin(), h.end())) + 1;
        // going to create the DP
        vector<int> dp(maxDist);

        fill(dp.begin(), dp.end(), 10000000);
        dp[0] = 0;

        for (int i = 1; i <= dp.size(); i++)
        {
            for (int j = 0; j < k.size(); j++)
            {
                if (k[j] < i && (dp[i - k[j]] + 1) < dp[i]) dp[i] = dp[i - k[j]] + 1;
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            count += dp[h[i]];
        }

        cout << count << endl;

    }
    return 0;
}
