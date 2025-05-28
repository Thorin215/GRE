import re  # For regular expression matching
from geopy.distance import geodesic  # For geographic distance calculation
import math

def geo_reward(content, sol):
    threshold = 
    def parse_coordinates(text):
        # Unified parsing function supporting two formats:
        # 1. Key-value pairs (e.g., "Latitude: 40.7, Longitude: -73.9")
        # 2. List format (e.g., [40.7, -73.9])
        text = text.strip()
        
        # Try to extract key-value pairs
        lat_match = re.search(
            r'(?:Latitude)\s*[=:]?\s*(-?\d+\.?\d*)', 
            text, 
            re.IGNORECASE
        )
        lon_match = re.search(
            r'(?:Longitude)\s*[=:]?\s*(-?\d+\.?\d*)', 
            text, 
            re.IGNORECASE
        )
        if lat_match and lon_match:
            return float(lat_match.group(1)), float(lon_match.group(1))
        
        # Try to extract list format
        numbers = re.findall(r'-?\d+\.?\d*', text)
        if len(numbers) >= 2:
            return float(numbers[0]), float(numbers[1])
        
        return None, None

    # Parse ground truth (sol)
    try:
        sol_answer = re.search(r'<answer>(.*?)</answer>', sol, re.DOTALL)
        sol_text = sol_answer.group(1).strip() if sol_answer else sol
        lat_gt, lon_gt = parse_coordinates(sol_text)
        if lat_gt is None or lon_gt is None:
            return 0.0
    except:
        return 0.0

    # Parse predicted answer (content)
    content_answer = re.search(r'<answer>(.*?)</answer>', content, re.DOTALL)
    if not content_answer:
        return 0.0
    answer_text = content_answer.group(1).strip()
    
    lon_pred, lat_pred = parse_coordinates(answer_text)
    print(lat_gt, lon_gt, lat_pred, lon_pred)
    if lat_pred is None or lon_pred is None:
        return 0.0

    # Validate coordinate ranges
    if not (-90 <= lat_pred <= 90) or not (-180 <= lon_pred <= 180):
        return 0.0

    # Calculate geographic distance
    try:
        distance = geodesic((lat_gt, lon_gt), (lat_pred, lon_pred)).kilometers
        print(distance)
    except:
        return 0.0

    # Reward function using natural exponent
    return 2 / (1 + math.e ** (distance / threshold))


content = "<think> The provided street view includes a clear display of a building address, allowing for an immediate inference into its location. Given \"1 Sutton Place East,\" Sutton Place is often associated with the Upper East Side in Manhattan, New York. \"East\" refers to its location relative to Central Park East and the other buildings adjacent to Sutton Place. However, pinpointing exact coordinates without API access is not possible within this structured output environment.</think> <answer> \"Longitude\" : -73.992210, \"Latitude\" : 40.749602 </answer>"
sol = "<answer> [40.756624, -73.960998] </answer>"
print(geo_reward(content, sol))