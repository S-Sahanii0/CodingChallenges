bool validBraces(String braces) {
  if (braces.contains('(){}[]')) {
    return true;
  } else {
    return false;
  }
}

void main() {
  print(validBraces("{}()[]"));
  validBraces("");
}
