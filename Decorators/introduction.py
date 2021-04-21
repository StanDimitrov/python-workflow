
base_rate = 1000
total_rate = 0
bill =0
occupancy_input = int(input('How many guests your are - 1,2 or 3?'))
room_choise = input('What is your room choice - S for sea_view_room, G for garden_view_room, D for standard_view_room')
booking_choice = int(input('How long do you want to stay?'))

if occupancy_input == 1:
    if room_choise == 'S':
        sea_view_rate = base_rate * 0.25 # 1000*0.25
        base_rate = base_rate + sea_view_rate
        print(base_rate)

    elif room_choise == 'G':
        garden_view_rate = base_rate * 0.30 # 1000*0.30
        base_rate = base_rate + garden_view_rate
        print(base_rate)

    elif room_choise == 'D':
        print(base_rate)


if occupancy_input == 2:
    if room_choise == 'S':
        occupancy_rate = base_rate * 0.20 # 0.20% per defaulf occupancy tax
        sea_view_rate = base_rate * 0.25 # 1000*0.25 sea view tax
        base_rate = base_rate + occupancy_rate + sea_view_rate # 1000 + 0.20% occupancy tax + 0.25 sea_view_tax
        print(base_rate)

    elif room_choise == 'G':
        occupancy_rate = base_rate * 0.20 # 0.20$ per default occupancy tax
        garden_view_rate = base_rate * 0.10 # 1000*0.10 garden view tax
        base_rate = base_rate + occupancy_rate + garden_view_rate # 1000 + 0.20 occupancy tax + 0.10 garden_view_tax
        print(base_rate)

    elif room_choise == 'D':
        occupancy_rate = base_rate * 0.20 # 0.20$ per default occupancy tax
        base_rate = base_rate + occupancy_rate
        print(base_rate)

if occupancy_input == 3:
    if room_choise == 'S':
        occupancy_rate = base_rate * 0.30 # 0.30$ per default occupancy tax
        sea_view_rate = base_rate * 0.25 # 0.25% per default sea_view_rate
        base_rate = base_rate + occupancy_rate + sea_view_rate
        print(base_rate)

    elif room_choise == 'G':
        occupancy_rate = base_rate * 0.30 # 0.30% per default occupancy tax
        garden_view_rate = base_rate * 0.10 # 0.10% per default garden_view_tax
        base_rate = base_rate + occupancy_rate + garden_view_rate
        print(base_rate)

    elif room_choise == 'D':
        occupancy_rate = base_rate * 0.30 # 0.30% per default occupancy tax
        base_rate = base_rate + occupancy_rate
        print(base_rate)

bill = booking_choice * base_rate
stay_tax = bill * 0.10
total_rate = bill + stay_tax
print(total_rate)