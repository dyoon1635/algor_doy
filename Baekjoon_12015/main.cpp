#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
vector<int> nums, L;

void init() {
    cin>>n;
    for (int i=0; i<n; i++) {
        int tmp;
        cin>>tmp;
        nums.push_back(tmp);
    } //sort(nums.begin(), nums.end());
}

void LIS() {
    L.push_back(nums[0]);
    for (int i=1; i<nums.size(); i++) {
        if (L.back() < nums[i])
            L.push_back(nums[i]);
        else
            *(lower_bound(L.begin(), L.end(), nums[i])) = nums[i];
    }
    cout<<L.size()<<endl;
}

int main() {
    init();
    LIS();
    return 0;
}
