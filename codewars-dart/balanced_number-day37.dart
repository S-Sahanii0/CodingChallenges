String balancedNum(int numb) {
  final numbString = numb.toString().split('');
  final numbStringReversed = numbString.reversed.toList();

  if (numbString.length <= 2) {
    return "Balanced";
  } else {
    var divideBy = 0;
    var sum = 0;
    var sumReversed = 0;
    if (numbString.length % 2 == 0) {
      divideBy = ((numbString.length / 2) - 1).toInt();
    } else {
      divideBy = (numbString.length / 2).floor();
    }
    for (int i = 0; i < divideBy; i++) {
      sum += int.parse(numbString[i]);
      sumReversed += int.parse(numbStringReversed[i]);
    }
    return sum == sumReversed ? "Balanced" : "Not Balanced";
  }
}
