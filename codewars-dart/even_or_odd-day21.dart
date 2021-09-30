String evenOrOdd(String number) {
  List<int> arr = number.split("").map((e) => int.parse(e)).toList();
  if (arr.length > 1) {
    int sumOfOdd = arr.where((element) => element % 2 != 0).isNotEmpty
        ? arr
            .where((element) => element % 2 != 0)
            .reduce((value, element) => value + element)
        : 0;
    int sumOfEven = arr.where((element) => element % 2 == 0).isNotEmpty
        ? arr
            .where((element) => element % 2 == 0)
            .reduce((value, element) => value + element)
        : 0;

    return sumOfEven == sumOfOdd
        ? "Even and Odd are the same"
        : sumOfEven > sumOfOdd
            ? "Even is greater than Odd"
            : "Odd is greater than Even";
  } else {
    return arr.first % 2 == 0
        ? "Even is greater than Odd"
        : "Odd is greater than Even";
  }
}

void main() {
  evenOrOdd("193");
}
