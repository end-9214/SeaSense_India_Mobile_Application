// lib/screens/region_screen.dart
import 'package:flutter/material.dart';

class RegionScreen extends StatelessWidget {
  final List<Map<String, dynamic>> states;

  RegionScreen({required this.states});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Explore States'),
        backgroundColor: Colors.blueAccent,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2, // Display 2 items per row
            crossAxisSpacing: 10,
            mainAxisSpacing: 10,
            childAspectRatio: 0.8, // Adjust the height of each card
          ),
          itemCount: states.length,
          itemBuilder: (context, index) {
            final state = states[index];
            final imageName = state['name'].toLowerCase().replaceAll(' ', '_'); // Assume images are named based on state name
            return GestureDetector(
              onTap: () {
                // Show state info dialog
                showDialog(
                  context: context,
                  builder: (BuildContext context) {
                    return AlertDialog(
                      title: Text(state['name']),
                      content: Text(state['beaches'] ?? 'No beaches listed.'),
                      actions: [
                        TextButton(
                          onPressed: () {
                            Navigator.of(context).pop();
                          },
                          child: Text('Close'),
                        ),
                      ],
                    );
                  },
                );
              },
              child: Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(12),
                  image: DecorationImage(
                    image: AssetImage('assets/images/$imageName.jpg'), // Image path
                    fit: BoxFit.cover,
                  ),
                ),
                child: Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(12),
                    color: Colors.black.withOpacity(0.2), // Slight overlay for aesthetic
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
