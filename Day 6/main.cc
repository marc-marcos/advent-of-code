#include <iostream>
#include <set>
#include <string.h>

// c4 ultimo
// c3 penultimo
// c2 antepenultimo
// c1 ante-antepenultimo

using namespace std;

int main() {
  char c1, c2, c3, c4;
  char c;
  int n = 4;

  cin >> c1 >> c2 >> c3 >> c4;

  while (cin >> c) {
    c1 = c2;
    c2 = c3;
    c3 = c4;
    c4 = c;

    set<char> c = {c1, c2, c3, c4};
    n++;
    if (c.size() < 4) {
      cout << n << endl;
    }
  }
}
