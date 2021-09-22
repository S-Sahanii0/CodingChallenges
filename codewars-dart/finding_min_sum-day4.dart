int minSum(arr) {
  // your code here
  List sortedList = arr as List;
  var sortedListAscending = sortedList..sort();
  var sortedListDescending = List.from(sortedListAscending).reversed.toList();

  final multiplicationList = [];
  for (int i = 0; i < sortedList.length / 2; i++) {
    var multiplication = sortedListAscending[i] * sortedListDescending[i];
    multiplicationList.add(multiplication);
  }

  print(multiplicationList.reduce((value, element) => value + element));
  return multiplicationList.reduce((value, element) => value + element);
}

void main() {
  minSum([5, 4, 2, 3]);
}
