// lib/models/models.dart
class Beach {
  final int id;
  final String name;
  final String description;
  final String imageUrl;

  Beach({
    required this.id,
    required this.name,
    required this.description,
    required this.imageUrl,
  });

  factory Beach.fromJson(Map<String, dynamic> json) {
    return Beach(
      id: json['id'],
      name: json['name'],
      description: json['description'],
      imageUrl: json['image_url'],
    );
  }
}
