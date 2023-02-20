import 'Package:flutter/material.dart';
import 'package:drowsydriver/Screens/Login/components/body.dart';
import 'package:drowsydriver/Screens/Login/verify.dart';
import 'package:drowsydriver/models/models.dart';

class Profile extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _Profile();
  final Loginn saveData;
  final String username;
  final String password;
  Profile(this.saveData, this.username, this.password);
}

class _Profile extends State<Profile> {
  List<Text> text = [];

  @override
  void initState() {
    //print(widget.save_data)
    tiles();
    super.initState();
  }

  @override
  Widget build(context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.username),
          centerTitle: true,
          automaticallyImplyLeading: false,
          actions: <Widget>[
            FlatButton(
              child: Text(
                'Logout',
                style: TextStyle(color: Colors.white),
              ),
              onPressed: () {
                Navigator.push(
                    context, MaterialPageRoute(builder: (context) => Body()));
              },
            ),
          ],
        ),
        body: Container(
          color: Colors.white,
          child: ListView.builder(
            itemCount: widget.saveData.records.length,
            itemBuilder: (BuildContext context, index) {
              return Container(
                child: Column(
                  children: <Widget>[
                    Card(
                        margin: EdgeInsets.all(10),
                        child: Container(
                            padding: EdgeInsets.symmetric(vertical: 10),
                            child: Center(
                                child: Text(widget.saveData.records[index])))),
                  ],
                ),
              );
            },
          ),
        ) //Text("$widget.save")
        );
  }

  List tiles() {
    for (int i = 0; i < widget.saveData.records.length; i++) {
      print(widget.saveData.records[i]);
      text.add(Text(widget.saveData.records[i]));
    }
    return text;
  }
}
