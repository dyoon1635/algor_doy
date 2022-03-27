#include <iostream>
#include <queue>
#include <deque>
using namespace std;

int n, t ,p;
int rock[100001];

int main() {
    priority_queue<int> pq;
    scanf("%d %d %d", &n, &t, &p);
    for (int i=0; i<n; i++) scanf("%d", &rock[i]);

    int res = 0, sum = 0, sz = 0;
    for (int i=0; i<n; i++) {
        if (t - p*i < 0) break;

        sum += rock[i];
        pq.push(rock[i]);
        sz ++;

        while(!pq.empty() && sum > t) {
            sum -= pq.top();
            pq.pop();
            sz --;
        }

        if (sum > t) break;
        res = max(res, sz);
        sum += p;
    }
    cout<<res<<endl;
    return 0;
}
