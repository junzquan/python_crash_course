def build_car_profile(manufacture, model, **car_info):
    car_profile = {}
    car_profile['manufacture'] = manufacture
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car_profile = build_car_profile('subaru', 'outback',
                      color='blue', tow_package=True)

print(car_profile)
