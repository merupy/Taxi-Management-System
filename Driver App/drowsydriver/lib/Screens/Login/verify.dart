//import 'package:flutter/cupertino.dart';
import 'dart:convert';

import 'package:drowsydriver/models/models.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
// import 'dart:convert';
import 'package:flutter_session/flutter_session.dart';
//import 'dart:convert';

// ignore: missing_return
Future<Loginn> verify(
    BuildContext context, String username, String password) async {
  var response = await http.post(
    'http://10.0.2.2:8000/api/login',
    body: {'username': username, 'password': password},
  );
  print(response.body);
  if (response.statusCode == 200) {
    Loginn drow = Loginn.fromJson(json.decode(response.body));
    // print(response.body);
    return drow;
  }
  return showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Error'),
          content: Text('Invalid username or password'),
          actions: <Widget>[
            FlatButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('Okay'),
            ),
          ],
        );
      });
}

// class UserValidator {
//   static String validate(String value) {
//     if (value.isEmpty) {
//       return "Username can't be empty";
//     }
//     return null;
//   }
// }
