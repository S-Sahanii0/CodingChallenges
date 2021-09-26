stray(List<int> numbers) {
  for (int i = 0; i < numbers.length; i++) {
    if (numbers[i] != numbers[i + 1]) {
      if (i == 0) {
        return numbers[i];
      } else {
        return numbers[i + 1];
      }
    }
  }
}

void main() {
  print(stray([1, 1, 2]));
  print(2 ^ 3);
  stray([1, 1, 2]);
}
