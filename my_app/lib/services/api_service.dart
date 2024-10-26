// lib/services/api_service.dart
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/models.dart';

class ApiService {
  final String baseUrl = 'https://your-backend-domain.com/api';

  Future<List<Beach>> fetchBeaches() async {
    final response = await http.get(Uri.parse('$baseUrl/beaches'));
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      return data.map((json) => Beach.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load beaches');
    }
  }
}
