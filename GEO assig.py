import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def match_closest_points(array1, array2):
    matches = []
    for point1 in array1:
        lat1, lon1 = point1
        closest_point = None
        min_distance = float('inf')
        for point2 in array2:
            lat2, lon2 = point2
            distance = haversine(lat1, lon1, lat2, lon2)
            if distance < min_distance:
                min_distance = distance
                closest_point = point2
        matches.append((point1, closest_point))
    return matches

array1 = [(42.3601, -71.0589), (34.0522, -118.2437)]
array2 = [(40.7128, -74.0060), (37.7749, -122.4194)]

print(match_closest_points(array1, array2))

