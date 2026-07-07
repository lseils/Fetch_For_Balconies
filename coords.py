"""
coords.py — Atlanta Street View coordinates for balcony detection dataset
Neighborhoods: Midtown, Buckhead, Old Fourth Ward, Inman Park, Downtown,
               Virginia-Highland, Buford Hwy, Grant Park, Westside,
               Edgewood, Poncey-Highland, Castleberry Hill
Grid spacing: ~20m
"""

import math

def _interpolate(lat1, lon1, lat2, lon2, step_m=20):
    R = 6371000
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2)**2
    dist = R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    n = max(int(dist / step_m), 1)
    return [
        (round(lat1 + (lat2 - lat1) * i/n, 6),
         round(lon1 + (lon2 - lon1) * i/n, 6))
        for i in range(n + 1)
    ]

_PATHS = [
    # (lat1, lon1, lat2, lon2, neighborhood, high_balcony_density)
    #(33.7800, -84.3880, 33.7720, -84.3810, "Midtown", True),
    #(33.7760, -84.3900, 33.7760, -84.3800, "Midtown", True),
    #(33.8400, -84.3900, 33.8310, -84.3800, "Buckhead", True),
    #(33.8350, -84.3950, 33.8350, -84.3830, "Buckhead", True),
    #(33.7600, -84.3700, 33.7540, -84.3620, "Old Fourth Ward", True),
    #(33.7570, -84.3730, 33.7570, -84.3630, "Old Fourth Ward", True),
    #(33.7540, -84.3580, 33.7470, -84.3510, "Inman Park", False),
    #(33.7510, -84.3600, 33.7510, -84.3520, "Inman Park", False),
    #(33.7560, -84.3930, 33.7490, -84.3860, "Downtown", True),
    #(33.7530, -84.3960, 33.7530, -84.3850, "Downtown", True),
    #(33.7810, -84.3620, 33.7740, -84.3540, "Virginia-Highland", False),
    #(33.7780, -84.3650, 33.7780, -84.3550, "Virginia-Highland", False),
    #(33.8350, -84.3380, 33.8280, -84.3280, "Buford Hwy", True),
    #(33.8310, -84.3420, 33.8310, -84.3310, "Buford Hwy", True),
    #(33.7380, -84.3720, 33.7310, -84.3640, "Grant Park", False),
]

# Build full coordinate list
COORDINATES = []
seen = set()
for lat1, lon1, lat2, lon2, hood, high_density in _PATHS:
    for lat, lng in _interpolate(lat1, lon1, lat2, lon2, step_m=20):
        key = (lat, lng)
        if key not in seen:
            seen.add(key)
            COORDINATES.append((lat, lng, hood, high_density))

# Convenience lists
PATH_COORDINATES    = [(lat, lng) for lat, lng, _, _ in COORDINATES]
BALCONY_TARGETS     = [(lat, lng) for lat, lng, _, high in COORDINATES if high]
NEGATIVE_EXAMPLES   = [(lat, lng) for lat, lng, _, high in COORDINATES if not high]

if __name__ == "__main__":
    from collections import Counter
    hoods = Counter(hood for _, _, hood, _ in COORDINATES)
    print(f"Total coordinates : {len(COORDINATES)}")
    print(f"Balcony targets   : {len(BALCONY_TARGETS)}")
    print(f"Negative examples : {len(NEGATIVE_EXAMPLES)}")
    print("\nPer neighborhood:")
    for hood, n in hoods.most_common():
        print(f"  {hood:<22} {n} points")