class Loginn {
  List<String> records = [];
  // Loginn({this.username, this.password});
  Loginn.fromJson(Map<String, dynamic> drowsiness) {
    //print(drowsiness['serilizer']);
    int size = drowsiness['serilizer'].length;

    for (int i = 0; i <= size - 1; i++) {
      records.add(drowsiness['serilizer'][i]['drowsiness']);
    }
  }
}
