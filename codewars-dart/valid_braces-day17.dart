bool validBraces(String braces) {
  Map<String, String> mapping = {"{": "}", "(": ")", "[": "]"};

  List stack = [];
  for (var ch in braces.split("")) {
    if (stack.isEmpty || mapping.containsKey(ch)) {
      stack.add(ch);
    } else if (mapping[stack.last] == ch) {
      stack.removeLast();
    } else {
      break;
    }
  }
  return stack.isEmpty;
}

void main() {
  validBraces("[(])");
}
