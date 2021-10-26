String jumpingNumber(int n) {
  final number = n.toString();
  if (number.length == 1) {
    return "Jumping!!";
  } else {
    bool flag = true;
    for (var i = 0; i < number.length - 1; i++) {
      if ((int.parse(number[i]) - int.parse(number[i + 1])).abs() == 1) {
        flag = true;
      } else {
        flag = false;
      }
    }
    return flag ? "Jumping!!" : "Not!!";
  }
}
