// lib/screens/beach_detail_screen.dart
import 'package:flutter/material.dart';
import '../models/models.dart';

class BeachDetailScreen extends StatelessWidget {
  final Beach beach;

  BeachDetailScreen({required this.beach});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(beach.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Image.network(beach.imageUrl, fit: BoxFit.cover),
            SizedBox(height: 16),
            Text(beach.name, style: Theme.of(context).textTheme.titleLarge),
            SizedBox(height: 8),
            Text(beach.description, style: Theme.of(context).textTheme.bodyMedium),
          ],
        ),
      ),
    );
  }
}
