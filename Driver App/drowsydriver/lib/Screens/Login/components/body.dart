import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:drowsydriver/Screens/Login/components/background.dart';
import 'package:drowsydriver/Screens/Profiel/profile.dart';
import 'package:drowsydriver/components/rounded_button.dart';
import 'package:drowsydriver/components/rounded_input_field.dart';
import 'package:drowsydriver/components/rounded_password_field.dart';
import 'package:drowsydriver/models/models.dart';
import 'package:flutter/material.dart';

import 'package:flutter_svg/svg.dart';

import '../verify.dart';

class Body extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _BodyState();
  }
}

class _BodyState extends State<Body> {
  final TextEditingController username = TextEditingController();
  final TextEditingController password = TextEditingController();
  final _formKey = GlobalKey<FormState>();
  bool _autoValidate = false;

  bool _passwordVisible;
  @override
  void initState() {
    _passwordVisible = false;
  }

  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      body: Background(
        child: SingleChildScrollView(
          child: Form(
            autovalidate: _autoValidate,
            key: _formKey,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text(
                  "LOGIN",
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
                SizedBox(height: size.height * 0.03),
                SvgPicture.asset(
                  "assets/icons/login.svg",
                  height: size.height * 0.35,
                ),
                SizedBox(height: size.height * 0.03),
                TextFormField(
                  decoration: InputDecoration(
                      border: OutlineInputBorder(), labelText: "Username"),
                  validator: (String value) {
                    if (value.length == 0) {
                      return 'Text is empty';
                    } else {
                      return null;
                    }
                  },
                  controller: username,
                  // hintText: "Your Username",
                ),
                Padding(
                  padding: EdgeInsets.only(
                    top: 20.0,
                  ),
                ),
                TextFormField(
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: "Password",
                      suffixIcon: IconButton(
                          icon: Icon(_passwordVisible
                              ? Icons.visibility
                              : Icons.visibility_off),
                          onPressed: () {
                            setState(() {
                              _passwordVisible = !_passwordVisible;
                            });
                          })),
                  obscureText: !_passwordVisible,
                  controller: password,
                  // hintText: "Your Username",
                ),
                RaisedButton(
                  child: Text("Login"),
                  onPressed: () async {
                    if (_formKey.currentState.validate()) {
                      fetchData();
                    } else {
                      setState(() {
                        _autoValidate = true;
                      });
                    }
                  },
                ),
                SizedBox(height: size.height * 0.03),
              ],
            ),
          ),
        ),
      ),
    );
  }

  void fetchData() async {
    Loginn data = await verify(context, username.text, password.text);
    if (data != null) {
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(
              builder: (context) =>
                  Profile(data, username.text, password.text)));
    } else {
      print("Helo");
    }
  }
}
