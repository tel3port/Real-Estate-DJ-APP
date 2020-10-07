x_list = [
    'assisted-living-housing.residentials.us',
    'auction-listings.residentials.us',
    'beach-front.residentials.us',
    'country-houses-usa.residentials.us',
    'couples-housing.residentials.us',
    'eviction-apartments.residentials.us',
    'family-houses.residentials.us',
    'foreclosure-houses.residentials.us',
    'la-suburbs.residentials.us',
    'new-apartments.residentials.us',
    'pet-friendly-apartments.residentials.us',
    'private-houses.residentials.us',
    'rent-to-own.residentials.us',
    'residentials.us.capterra-reviews.us',
    'seniors-housing.residentials.us',
    'short-term-rentals.residentials.us',
    'starter-homes.residentials.us',
    'student-housing.residentials.us',
    'unemployed-housing.residentials.us',
    'veterans-housing.residentials.us',
          ]

for x in x_list:
    if'residentials.us' in x:
        print("ALLOWED_HOSTS = [")
        print(f'"{"127.0.0.1"}",')
        print(f'"{x}",')
        print(f'"www.{x}",')
        print("]")
        print()
