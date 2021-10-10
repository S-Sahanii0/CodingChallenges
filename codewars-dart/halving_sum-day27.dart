int halvingSum(int n) {
  var newList = [n];
  var backup = n;
  while (backup > 1) {
    newList.add((backup / 2).floor());
    backup = (backup / 2).floor();
  }
  print(newList.reduce((v, e) => v + e));
  return newList.reduce((v, e) => v + e);
}

void main() {
  halvingSum(25);
}
