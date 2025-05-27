#include <stdio.h>
#include <string.h>
int main(){
    int n, cn = 1;
    while (scanf("%d", &n) == 1 && n) {
        char a[11], b[11], nm[40][11];
        int m = 0, to[40], v[40] = {0}, i, j, x, y, c = 0;
        for (i = 0; i < n; i++) {
            scanf("%s %s", a, b);
            x = y = -1;
            for (j = 0; j < m; j++) if (strcmp(nm[j], a) == 0) x = j;
            if (x < 0) { x = m; strcpy(nm[m++], a); }
            for (j = 0; j < m; j++) if (strcmp(nm[j], b) == 0) y = j;
            if (y < 0) { y = m; strcpy(nm[m++], b); }
            to[x] = y;
        }
        for (i = 0; i < m; i++) {
            if (!v[i]) {
                int u = i;
                do { v[u] = 1; u = to[u]; } while (!v[u]);
                c++;
            }
        }
        printf("%d %d\n", cn++, c);
    }
    return 0;
}