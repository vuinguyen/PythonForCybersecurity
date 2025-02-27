company_name = input('What is your company name>> ')
number_of_employees = input('How many employees are there?>> ')
location = input('What is your location: city OR country OR state?>> ')
lowest_price = input('How much is your lowest priced policy?>> ')
highest_price = input('How much is your highest priced policy?>> ')

print(f'\nWe at {company_name} are located in {location}. Our {number_of_employees} employees will help you find')
print(f'the right policy to meet your needs and budget from ${lowest_price} to ${highest_price} a month!')