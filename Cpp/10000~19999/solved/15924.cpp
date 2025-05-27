#include <iostream>
#include <string>
using namespace std;
typedef long long ll;
const int mod = 1e9 + 9;
int n, m;
string a[3003];
ll dp[3003][3003];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;

    for (int i = 0; i < n; i++) cin >> a[i];
    dp[n - 1][m - 1] = 1;
    for(int i = n - 1; i >= 0; i--) {
        for(int j = m - 1; j >= 0; j--) {
            char c = a[i][j];
            if (c == 'X') continue;
            if (c == 'E') dp[i][j] = dp[i][j + 1];
            else if(c == 'S') dp[i][j] = dp[i+1][j];
            else dp[i][j] = (dp[i][j + 1] + dp[i + 1][j]) % mod;
        }
    }
    ll r = 0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            r = (r + dp[i][j]) % mod;
    cout << r << '\n';

}