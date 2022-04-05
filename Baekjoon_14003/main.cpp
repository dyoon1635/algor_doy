// https://yabmoons.tistory.com/561
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

int n;
vector<int> nums, L;

void init() {
    cin>>n;
    for (int i=0; i<n; i++) {
        int tmp;
        cin>>tmp;
        nums.push_back(tmp);
    }
}

void LIS() {
    int index[n] = {0,};
    L.push_back(nums[0]);
    for (int i=1; i<nums.size(); i++) {
        if (L.back() < nums[i]) {
            L.push_back(nums[i]);
            index[i] = L.size() - 1;
        }
        else {
            vector<int>::iterator idx = lower_bound(L.begin(), L.end(), nums[i]);
            *idx = nums[i];
            index[i] = idx - L.begin();
        }
    }
    cout<<L.size()<<endl;
    vector<int> res;
    for (int idx = n-1, i=L.size()-1 ; idx>=0; idx--) {
        if (i == -1) break;
        if (i == index[idx]) {
            res.push_back(idx);
            i--;
        }
    }
    while(!res.empty()) {
        cout<<nums[res.back()]<<" ";
        res.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    init();
    LIS();
    return 0;
}
