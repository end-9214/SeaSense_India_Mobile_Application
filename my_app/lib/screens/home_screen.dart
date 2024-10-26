// lib/screens/home_screen.dart
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: Text('SeaSense India'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: Stack(
        children: [
          // Background image
          Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/images/beach_background.jpg'), // Ensure the image is placed correctly in your assets
                fit: BoxFit.cover,
              ),
            ),
          ),
          // Content with description and buttons
          Container(
            padding: const EdgeInsets.all(16.0),
            color: Colors.black.withOpacity(0.3), // Dark overlay for text contrast
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Welcome to SeaSense India 🌊',
                  style: Theme.of(context)
                      .textTheme
                      .titleLarge!
                      .copyWith(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 28,
                        shadows: [
                          Shadow(
                            offset: Offset(2, 2),
                            blurRadius: 4.0,
                            color: Colors.black45,
                          ),
                        ],
                      ),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 16),
                Text(
                  'Plan your perfect beach trip with real-time weather alerts, activity suggestions, and beautiful coastal views. Discover the best spots along the Southern, Eastern, and Western coasts of India.',
                  style: Theme.of(context)
                      .textTheme
                      .bodyMedium!
                      .copyWith(
                        color: Colors.white.withOpacity(0.95), // Lighter text color for better visibility
                        fontSize: 18,
                        fontWeight: FontWeight.w500,
                        shadows: [
                          Shadow(
                            offset: Offset(1, 1),
                            blurRadius: 3.0,
                            color: Colors.black38,
                          ),
                        ],
                      ),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 32),
                // Southern Coast Button
                ElevatedButton(
                  onPressed: () {
                    // Navigate to the Southern Coast screen or perform action
                  },
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 16),
                    backgroundColor: Colors.deepOrangeAccent.withOpacity(0.8),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('🏝️', style: TextStyle(fontSize: 24)),
                      SizedBox(width: 8),
                      Text(
                        'Southern Coast',
                        style: TextStyle(
                          fontSize: 20,
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 16),
                // East Coast Button
                ElevatedButton(
                  onPressed: () {
                    // Navigate to the East Coast screen or perform action
                  },
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 16),
                    backgroundColor: Colors.purpleAccent.withOpacity(0.8),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('🌅', style: TextStyle(fontSize: 24)),
                      SizedBox(width: 8),
                      Text(
                        'East Coast',
                        style: TextStyle(
                          fontSize: 20,
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 16),
                // Western Coast Button
                ElevatedButton(
                  onPressed: () {
                    // Navigate to the Western Coast screen or perform action
                  },
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 16),
                    backgroundColor: Colors.lightBlueAccent.withOpacity(0.8),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('🏖️', style: TextStyle(fontSize: 24)),
                      SizedBox(width: 8),
                      Text(
                        'Western Coast',
                        style: TextStyle(
                          fontSize: 20,
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
