bool XO(String str) {
  var regExpForX = new RegExp("x");
  int countForX = regExpForX.allMatches(str).length;
  var regExpForO = new RegExp("o");
  int countForO = regExpForO.allMatches(str).length;
  if (countForO == countForX) {
    return true;
  } else {
    print("no");
    return false;
  }
}

void main() {
  XO("xxooo");
}
