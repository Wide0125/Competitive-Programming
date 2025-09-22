#include <iostream>
#include <vector>

int main() {
    int t {};
    std::cin >> t;
    for (int testcase {0}; testcase < t; ++testcase){
        int n {};
        std::cin >> n;

        std::vector<int> array (2 * n, 1);

        for (int i {n}; i > 1; --i) {
            if (i % 2 == n % 2) {
                array[n - i] = i;
                array[i] = i;
            }
            else {
                array[n - i + n] = i;
                array[n + i] = i;
            }
        }

        for (auto a: array) {
            std::cout << a << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}
