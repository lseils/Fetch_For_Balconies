"""
coords_extra.py — Additional Street View coordinates for balcony detection dataset
Locations chosen for mid-rise buildings (3-8 stories) with prominent balconies
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
    # -------------------------------------------------------------------------
    # ATLANTA ADDITIONS (mid-rise, Beltline corridor)
    # -------------------------------------------------------------------------
    (33.7490, -84.3630, 33.7420, -84.3560, "Atlanta - Reynoldstown", True),
    (33.7460, -84.3670, 33.7460, -84.3570, "Atlanta - Reynoldstown", True),
    (33.7880, -84.4120, 33.7810, -84.4050, "Atlanta - West Midtown", True),
    (33.7850, -84.4150, 33.7850, -84.4060, "Atlanta - West Midtown", True),
    (33.7510, -84.3470, 33.7440, -84.3400, "Atlanta - Edgewood Ave", True),
    (33.7480, -84.3500, 33.7480, -84.3400, "Atlanta - Edgewood Ave", False),

    # -------------------------------------------------------------------------
    # MIAMI BEACH, FL
    # Collins Ave — dense condo corridor, balconies on almost every unit
    # -------------------------------------------------------------------------
    (25.8150, -80.1220, 25.8050, -80.1220, "Miami Beach - Collins Ave North", True),
    (25.8050, -80.1220, 25.7950, -80.1220, "Miami Beach - Collins Ave Mid", True),
    (25.7950, -80.1220, 25.7850, -80.1220, "Miami Beach - Collins Ave South", True),
    (25.7900, -80.1300, 25.7900, -80.1200, "Miami Beach - 17th St corridor", True),
    (25.7820, -80.1300, 25.7820, -80.1200, "Miami Beach - Lincoln Rd area", True),
    # Ocean Drive — Art Deco, lower density balconies, good negative mix
    (25.7850, -80.1300, 25.7750, -80.1290, "Miami Beach - Ocean Drive", False),

    # -------------------------------------------------------------------------
    # MYRTLE BEACH, SC
    # Ocean Blvd — wall-to-wall balcony-facing condos, extremely dense
    # -------------------------------------------------------------------------
    (33.7200, -78.8800, 33.7100, -78.8800, "Myrtle Beach - Ocean Blvd North", True),
    (33.7100, -78.8800, 33.7000, -78.8800, "Myrtle Beach - Ocean Blvd Mid", True),
    (33.7000, -78.8800, 33.6900, -78.8800, "Myrtle Beach - Ocean Blvd South", True),
    (33.6900, -78.8800, 33.6800, -78.8800, "Myrtle Beach - Ocean Blvd Far South", True),
    # Side streets — mix of balcony and non-balcony
    (33.7150, -78.8830, 33.7150, -78.8760, "Myrtle Beach - 9th Ave N", True),
    (33.7050, -78.8830, 33.7050, -78.8760, "Myrtle Beach - 3rd Ave N", False),

    # -------------------------------------------------------------------------
    # NEW ORLEANS, LA
    # Magazine St / Uptown — wrought iron balconies, distinct style
    # -------------------------------------------------------------------------
    (29.9350, -90.1050, 29.9280, -90.1000, "New Orleans - Magazine St", True),
    (29.9600, -90.0650, 29.9530, -90.0580, "New Orleans - French Quarter", True),
    (29.9530, -90.0700, 29.9530, -90.0600, "New Orleans - Bourbon St", True),
    (29.9480, -90.0750, 29.9480, -90.0650, "New Orleans - Royal St", True),
    # Garden District — lower rise, some balconies
    (29.9280, -90.0950, 29.9210, -90.0880, "New Orleans - Garden District", False),

    # -------------------------------------------------------------------------
    # CHICAGO, IL
    # Wicker Park / Logan Square — 3-6 story courtyard apartments
    # -------------------------------------------------------------------------
    (41.9090, -87.6770, 41.9020, -87.6700, "Chicago - Wicker Park", True),
    (41.9020, -87.6800, 41.9020, -87.6700, "Chicago - Milwaukee Ave", True),
    (41.9250, -87.7080, 41.9180, -87.7010, "Chicago - Logan Square", True),
    (41.9200, -87.7100, 41.9200, -87.7000, "Chicago - Kedzie Ave", True),
    # Lincoln Park — mix of high and mid rise
    (41.9280, -87.6480, 41.9210, -87.6410, "Chicago - Lincoln Park", True),
    (41.9250, -87.6500, 41.9250, -87.6400, "Chicago - Clark St", False),

    # -------------------------------------------------------------------------
    # AUSTIN, TX
    # East 6th / South Congress — newer mid-rise, modern balcony styles
    # -------------------------------------------------------------------------
    (30.2620, -97.7280, 30.2550, -97.7210, "Austin - East 6th St", True),
    (30.2580, -97.7300, 30.2580, -97.7200, "Austin - East Cesar Chavez", True),
    (30.2500, -97.7500, 30.2430, -97.7430, "Austin - South Congress", True),
    (30.2460, -97.7520, 30.2460, -97.7420, "Austin - South 1st St", False),

    # -------------------------------------------------------------------------
    # JERSEY CITY, NJ
    # Journal Square / Downtown — dense mid-rise residential
    # -------------------------------------------------------------------------
    (40.7178, -74.0431, 40.7108, -74.0361, "Jersey City - Downtown", True),
    (40.7140, -74.0460, 40.7140, -74.0360, "Jersey City - Grove St", True),
    (40.7320, -74.0630, 40.7250, -74.0560, "Jersey City - Journal Square", True),
    (40.7280, -74.0650, 40.7280, -74.0550, "Jersey City - Bergen Ave", True),

    # -------------------------------------------------------------------------
    # SAN DIEGO, CA
    # North Park / Hillcrest — 3-5 story apartments, clear imagery
    # -------------------------------------------------------------------------
    (32.7480, -117.1290, 32.7410, -117.1220, "San Diego - North Park", True),
    (32.7450, -117.1310, 32.7450, -117.1210, "San Diego - University Ave", True),
    (32.7530, -117.1490, 32.7460, -117.1420, "San Diego - Hillcrest", True),
    (32.7500, -117.1510, 32.7500, -117.1410, "San Diego - 5th Ave", False),
]

# Build full coordinate list
COORDINATES_EXTRA = []
seen = set()
for lat1, lon1, lat2, lon2, location, high_density in _PATHS:
    for lat, lng in _interpolate(lat1, lon1, lat2, lon2, step_m=20):
        key = (lat, lng)
        if key not in seen:
            seen.add(key)
            COORDINATES_EXTRA.append((lat, lng, location, high_density))

# Convenience lists
PATH_COORDINATES_EXTRA  = [(lat, lng) for lat, lng, _, _ in COORDINATES_EXTRA]
BALCONY_TARGETS_EXTRA   = [(lat, lng) for lat, lng, _, high in COORDINATES_EXTRA if high]
NEGATIVE_EXAMPLES_EXTRA = [(lat, lng) for lat, lng, _, high in COORDINATES_EXTRA if not high]

if __name__ == "__main__":
    from collections import Counter
    locations = Counter(loc for _, _, loc, _ in COORDINATES_EXTRA)
    print(f"Total coordinates : {len(COORDINATES_EXTRA)}")
    print(f"Balcony targets   : {len(BALCONY_TARGETS_EXTRA)}")
    print(f"Negative examples : {len(NEGATIVE_EXAMPLES_EXTRA)}")
    print("\nPer location:")
    for loc, n in locations.most_common():
        print(f"  {loc:<45} {n} points")