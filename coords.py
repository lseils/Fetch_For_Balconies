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
    #(33.7380, -84.3720, 33.7310, -84.3640, "Grant Park", False), #dont do this one again
    #(33.7730, -84.4150, 33.7660, -84.4060, "Westside", True),
    #(33.7700, -84.4180, 33.7700, -84.4080, "Westside", True),
    #(33.7530, -84.3530, 33.7460, -84.3450, "Edgewood", False),
    #(33.7500, -84.3560, 33.7500, -84.3460, "Edgewood", False),
    #(33.7710, -84.3620, 33.7640, -84.3540, "Poncey-Highland", True),
    #(33.7680, -84.3650, 33.7680, -84.3560, "Poncey-Highland", True),
    #(33.7440, -84.4010, 33.7380, -84.3940, "Castleberry Hill", True),
    #(33.7410, -84.4040, 33.7410, -84.3950, "Castleberry Hill", True),

    # -------------------------------------------------------------------------

    #(33.7490, -84.3630, 33.7420, -84.3560, "Atlanta - Reynoldstown", True),
    #(33.7460, -84.3670, 33.7460, -84.3570, "Atlanta - Reynoldstown", True),
    #(33.7880, -84.4120, 33.7810, -84.4050, "Atlanta - West Midtown", True),
    #(33.7850, -84.4150, 33.7850, -84.4060, "Atlanta - West Midtown", True),

    #(25.8150, -80.1220, 25.8050, -80.1220, "Miami Beach - Collins Ave North", True),
    #(25.8050, -80.1220, 25.7950, -80.1220, "Miami Beach - Collins Ave Mid", True),
    #(25.7950, -80.1220, 25.7850, -80.1220, "Miami Beach - Collins Ave South", True),
    #(25.7900, -80.1300, 25.7900, -80.1200, "Miami Beach - 17th St corridor", True),
    #(25.7820, -80.1300, 25.7820, -80.1200, "Miami Beach - Lincoln Rd area", True),
    #(25.7850, -80.1300, 25.7750, -80.1290, "Miami Beach - Ocean Drive", False),

    #(33.7200, -78.8800, 33.7100, -78.8800, "Myrtle Beach - Ocean Blvd North", True),
    #(33.7100, -78.8800, 33.7000, -78.8800, "Myrtle Beach - Ocean Blvd Mid", True),
    #(33.7000, -78.8800, 33.6900, -78.8800, "Myrtle Beach - Ocean Blvd South", True),
    #(33.6900, -78.8800, 33.6800, -78.8800, "Myrtle Beach - Ocean Blvd Far South", True),
    #(33.7150, -78.8830, 33.7150, -78.8760, "Myrtle Beach - 9th Ave N", True),
    #(33.7050, -78.8830, 33.7050, -78.8760, "Myrtle Beach - 3rd Ave N", False),

    #(41.9090, -87.6770, 41.9020, -87.6700, "Chicago - Wicker Park", True),
    #(41.9020, -87.6800, 41.9020, -87.6700, "Chicago - Milwaukee Ave", True),
    #(41.9250, -87.7080, 41.9180, -87.7010, "Chicago - Logan Square", True),
    #(41.9200, -87.7100, 41.9200, -87.7000, "Chicago - Kedzie Ave", True),
    #(41.9280, -87.6480, 41.9210, -87.6410, "Chicago - Lincoln Park", True),
    #(41.9250, -87.6500, 41.9250, -87.6400, "Chicago - Clark St", False),

    #(30.2620, -97.7280, 30.2550, -97.7210, "Austin - East 6th St", True),
    #(30.2580, -97.7300, 30.2580, -97.7200, "Austin - East Cesar Chavez", True),
    #(30.2500, -97.7500, 30.2430, -97.7430, "Austin - South Congress", True),
    #(30.2460, -97.7520, 30.2460, -97.7420, "Austin - South 1st St", False),

    #(40.7178, -74.0431, 40.7108, -74.0361, "Jersey City - Downtown", True),
    #(40.7140, -74.0460, 40.7140, -74.0360, "Jersey City - Grove St", True),
    #(40.7320, -74.0630, 40.7250, -74.0560, "Jersey City - Journal Square", True),
    #(40.7280, -74.0650, 40.7280, -74.0550, "Jersey City - Bergen Ave", True),

    #(32.7480, -117.1290, 32.7410, -117.1220, "San Diego - North Park", True),
    #(32.7450, -117.1310, 32.7450, -117.1210, "San Diego - University Ave", True),
    #(32.7530, -117.1490, 32.7460, -117.1420, "San Diego - Hillcrest", True),
    #(32.7500, -117.1510, 32.7500, -117.1410, "San Diego - 5th Ave", False),

]

# Seed points: single spots known to have balconies. fetch_streetview_tiles.py
# grabs the pano at each seed, then follows Street View's pano-to-pano links
# HOPS_PER_DIRECTION drops down the road in every direction the road goes.
# (~10m between drops, so 10 hops ≈ 100m each way)
HOPS_PER_DIRECTION = 10

SEED_POINTS = [
    # (lat, lng, neighborhood, high_balcony_density)
    # (33.7490, -84.3630, "Atlanta - Seed 01", True),
    # (33.7460, -84.3670, "Atlanta - Seed 02", True),
    # (33.7880, -84.4120, "Atlanta - Seed 03", True),
    # (33.7850, -84.4150, "Atlanta - Seed 04", True)
    (33.7885, -84.4036, "Atlanta - Seed 05", True),
    (33.7887, -84.4019, "Atlanta - Seed 06", True),
    (33.7894, -84.3992, "Atlanta - Seed 07", True),
    (33.7897, -84.4013, "Atlanta - Seed 08", True),
    (33.7912, -84.4001, "Atlanta - Seed 09", True),
    (33.7767, -84.3829, "Atlanta - Seed 10", True),
    (33.7772, -84.3821, "Atlanta - Seed 11", True),
    (33.7782, -84.3827, "Atlanta - Seed 12", True),
    (33.7799, -84.3826, "Atlanta - Seed 13", True),
    (33.7815, -84.3825, "Atlanta - Seed 14", True),
    (33.7830, -84.3818, "Atlanta - Seed 15", True),
    (33.7830, -84.3801, "Atlanta - Seed 16", True),
    (33.7825, -84.3785, "Atlanta - Seed 17", True),
    (33.7826, -84.3802, "Atlanta - Seed 18", True),
    (33.7832, -84.3783, "Atlanta - Seed 19", True),
    (33.7832, -84.3793, "Atlanta - Seed 20", True)

    # (40.7178, -74.0431, "Jersey City - Seed 01", True),
    # (40.7140, -74.0460, "Jersey City - Seed 02", True),
    # (40.7320, -74.0630, "Jersey City - Seed 03", True),
    # (40.7280, -74.0650, "Jersey City - Seed 04", True),
    # (33.754314, -84.366210, "Atlanta - Seed 11", True),
    # (33.774432, -84.406103, "Atlanta - Seed 12", True),
    # (33.788077, -84.404465, "Atlanta - Seed 13", True),
    # (32.7480, -117.1290, "San Diego - Seed 01", True),
    # (32.7450, -117.1310, "San Diego - Seed 02", True),
    # (32.7530, -117.1490, "San Diego - Seed 03", True),
    # (32.7500, -117.1510, "San Diego - Seed 04", False),
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
    print(f"Seed points       : {len(SEED_POINTS)} (x{HOPS_PER_DIRECTION} hops each way)")
    print("\nPer neighborhood:")
    for hood, n in hoods.most_common():
        print(f"  {hood:<22} {n} points")