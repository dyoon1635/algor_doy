#include <stdio.h>
#include <queue>
using namespace std;

int main() {
    int n, len1 = 1, len2 = 1, num;
    priority_queue<int> pq1, pq2;
    scanf("%d", &n);

    scanf("%d", &num);
    pq1.push(num);
    printf("%d\n", num);

    scanf("%d", &num);
    pq1.push(num);
    int tmp = pq1.top();
    pq2.push(-tmp);
    pq1.pop();
    printf("%d\n",pq1.top());

    for (int i=2; i<n; i++) {
        scanf("%d", &num);
        if (num > -pq2.top()) { pq2.push(-num); len2++; }
        else { pq1.push(num); len1++; }

        if (len1 - len2 > 1) {
            tmp = pq1.top();
            pq2.push(-tmp); len2 ++;
            pq1.pop(); len1 --;
        }
        if (len2 > len1) {
            tmp = pq2.top();
            pq1.push(-tmp); len1 ++;
            pq2.pop(); len2 --;
        }

        printf("%d\n", pq1.top());
    }
    return 0;
}
