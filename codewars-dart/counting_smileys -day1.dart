int countSmileys(List<String> arr) {
  List smileys = [];
  List smileysWithNose = [];
  List smileysWithNoNose = [];
  // your code here
  for (int i = 0; i < arr.length; i++) {
    if (arr[i].contains(new RegExp(r'^[\;|\:]')) &&
        arr[i].contains(new RegExp(r'[D|\)]$'))) {
      smileys.add(arr[i]);
    }
  }

  print(smileys);

  for (int j = 0; j < smileys.length; j++) {
    if (smileys[j].contains(new RegExp(r'[\~\-]'))) {
      smileysWithNose.add(smileys[j]);
    }
  }

  print(smileysWithNose);

  for (int j = 0; j < smileys.length; j++) {
    if (smileys[j].length == 2) {
      smileysWithNoNose.add(smileys[j]);
    }
  }

  print(smileysWithNoNose);

  List finalSmileys = smileysWithNoNose +
      smileysWithNose.where((element) => element.length == 3).toList();
  print(finalSmileys);

  return finalSmileys.length;
}

void main() {
  countSmileys([':)', ';(', ';}', ':-D']);
}
