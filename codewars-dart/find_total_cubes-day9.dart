import 'dart:math';

int findNb(int m) {
  var total = 0;
  var cube = 0;

  while (total < m) {
    cube += 1;
    total += cube * cube * cube;
  }
  if (total == m) {
    return cube;
  } else {
    return -1;
  }
}

void main() {
  findNb(91716553919377);
}
