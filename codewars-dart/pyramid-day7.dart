List<List<int>> pyramid(int n) {
  // your code here
  final finalList = <int>[];
  final List<List<int>> result = [];
  for (int i = 0; i < n; i++) {
    finalList..add(1);
  }
  for (int j = 0; j < finalList.length; j++) {
    result.add(finalList.take(j + 1).toList());
  }
  print(result);
  return result;
}

void main() {
  pyramid(0);
}
