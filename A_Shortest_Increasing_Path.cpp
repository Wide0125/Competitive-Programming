#include <iostream>

int main() {
    int t {};
    std::cin >> t;

    for (int i {0}; i < t; ++i) {
        int x {};
        std::cin >> x;
        int y {};
        std::cin >> y;

        if (y > x) {
            std::cout << 2 << '\n';
            continue;
        }
        if (y < x - 1 and y > 1) {
            std::cout << 3 << '\n';
            continue;
        }
        else {std::cout << -1 << '\n';}
    }

    return 0;
}
