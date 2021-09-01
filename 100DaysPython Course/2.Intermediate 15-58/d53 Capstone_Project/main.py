import finder

location = input('City (ex: San Diego, CA): ')
price = input('Max Price (ex: 150000): ')
n_beds = int(input('Beds (ex: 1 (range 1-5)): '))+1
rental_finder = finder.Finder()
rental_finder.param(location, price, n_beds)
rental_finder.get_rentals()
rental_finder.fill_forms()
rental_finder.create_sheets(location)

# test.close()
