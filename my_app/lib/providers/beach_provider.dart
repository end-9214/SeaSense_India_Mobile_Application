// lib/providers/beach_provider.dart
import 'package:flutter/material.dart';
import '../models/models.dart';
import '../services/api_service.dart';

class BeachProvider with ChangeNotifier {
  final ApiService apiService;
  List<Beach> _beaches = [];
  bool _isLoading = true;

  BeachProvider(this.apiService) {
    fetchBeaches();
  }

  List<Beach> get beaches => _beaches;
  bool get isLoading => _isLoading;

  Future<void> fetchBeaches() async {
    try {
      _beaches = await apiService.fetchBeaches();
    } catch (e) {
      print('Error fetching beaches: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
