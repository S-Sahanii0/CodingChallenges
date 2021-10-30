List<int> solve(List<String> arr) {
  final result = <int>[];
  var letters = [
    for (var i = 65; i <= 90; i++) String.fromCharCode(i).toLowerCase()
  ];
  for (var i = 0; i < arr.length; i++) {
    final splitted = arr[i].split('');

    var sum = 0;
    for (var j = 0; j < splitted.length; j++) {
      if (splitted[j].toLowerCase() == letters[j]) {
        sum += 1;
      }
    }
    result.add(sum);
  }
  print(result);
  return result;
}

void main(List<String> args) {
  solve(["abode", "ABc", "xyzD"]);
}
