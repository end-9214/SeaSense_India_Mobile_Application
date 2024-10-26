// lib/main.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/beach_provider.dart';
import 'services/api_service.dart';
import 'screens/beach_list_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => BeachProvider(ApiService()),
      child: MaterialApp(
        title: 'SeaSense India',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: BeachListScreen(),
      ),
    );
  }
}
