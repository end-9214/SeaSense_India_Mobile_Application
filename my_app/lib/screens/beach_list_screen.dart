// lib/screens/beach_list_screen.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/beach_provider.dart';
import 'beach_detail_screen.dart';
import '../models/models.dart';

class BeachListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final beachProvider = Provider.of<BeachProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('SeaSense India'),
      ),
      body: beachProvider.isLoading
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: beachProvider.beaches.length,
              itemBuilder: (context, index) {
                final beach = beachProvider.beaches[index];
                return ListTile(
                  leading: Image.network(beach.imageUrl, width: 60, fit: BoxFit.cover),
                  title: Text(beach.name),
                  subtitle: Text(beach.description),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => BeachDetailScreen(beach: beach),
                      ),
                    );
                  },
                );
              },
            ),
    );
  }
}
