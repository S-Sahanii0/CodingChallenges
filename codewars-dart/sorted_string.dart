String longest(String a, String b) {
  final result = a + b;
  final listOfChar = [];
  for (var i = 0; i < result.length; i++) {
    if (!listOfChar.contains(result[i])) {
      listOfChar.add(result[i]);
    }
  }
  listOfChar.sort();
  return listOfChar.join();
}
