import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/models.dart'; // Correct path for models.dart


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
      // Handle error here
      print('Error fetching beaches: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
