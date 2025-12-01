#include <iostream>
#include <vector>
using namespace std;

int main() {

    string line;

    vector<int> list1;
    vector<int> list2;

    int x;
    int y;

    while (cin) {
        cin >> x;
        cin >> y;
        
        list1.push_back(x);
        list2.push_back(y);
    }


    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    int abs_diff = 0;
    for (auto a = list1.cbegin(), b = list2.cbegin(); a != list1.cend(); ++a, ++b) {
        cout << *a << ' ' << *b << endl;
        abs_diff += (*a > *b ? *a - *b : *b - *a);
    }

    cout << abs_diff << endl;

}