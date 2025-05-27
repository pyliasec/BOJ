#include <iostream>
#include <unordered_map>
using namespace std;
int main(){
    int n, cn = 1;
    while (cin >> n && n) {
        unordered_map<string,int> mp;
        string s, t;
        int m = 0, nxt[40], c = 0;
        bool vis[40] = {0};
        for (int i = 0; i < n; i++) {
            cin >> s >> t;
            if (!mp.count(s)) mp[s] = m++;
            if (!mp.count(t)) mp[t] = m++;
            nxt[mp[s]] = mp[t];
        }
        for (int i = 0; i < m; i++) {
            if (!vis[i]) {
                int u = i;
                do { vis[u] = true; u = nxt[u]; } while (!vis[u]);
                c++;
            }
        }
        cout << cn++ << " " << c << "\n";
    }
    return 0;
}