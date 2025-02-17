// So at first, we are sorting the array because the only elements that create a problem for the median to be the elements that are greater than the mid element after sorting the maximum would be the next elements including mid after the mid element so we check that what are the total number of operations we have to make mid element as max as possible if it is <=k then yes otherwise take answer less than our current answer //

#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define int long long
using namespace std;

int n, k;
vector<int> arr;

bool check(int x) {
    int req = 0;
    for (int i = n / 2; i < n; i++) {
        if (x > arr[i]) {
            req += (x - arr[i]);
        } else {
            break;
        }
    }
    return (req <= k);
}

void solution() {
    cin >> n >> k;
    arr.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    int low = 1, high = 1e10;
    int ans = arr[n / 2];
    while (low <= high) {
        int mid = (low + high) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    cout << ans << endl;
}

int32_t main() {
    fast;
    solution();
    return 0;
}
