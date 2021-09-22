import 'dart:math' as Math;

List<List<String>> howmuch(int m, int n) {
  // your code
  int min = Math.min(m, n);
  int max = Math.max(m, n);

  final List<List<String>> solution = [];

  for (int i = min; i <= max; i++) {
    if ((i - 2) % 7 == 0 && (i - 1) % 9 == 0) {
      solution.add([
        "M: $i",
        "B: ${((i - 2) / 7).round()}",
        "C: ${((i - 1) / 9).round()}"
      ]);
    }
  }

  print(solution);
  return solution;
}

void main() {
  howmuch(1, 100);
}
