from app.models import db, Home


def seed_homes():
    home1 = Home(price = 1500000, stAddress = "683 Hamilton ct.", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.94605, longitude = -121.68965, lotSize = 3600, beds = 5, bath = 3.5, status = "For sale",userId='2')
    home2 = Home(price = 1000000, stAddress = "1537 Park Street", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.93249, longitude = -121.69218, lotSize = 3200, beds = 4, bath = 2.5, status = "Rent",userId='2')
    home3 = Home(price = 950000, stAddress = "2054 Park Street", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.93249, longitude = -121.69218, lotSize = 3000, beds = 3, bath = 1.5, status = "Sale pending",userId='2')
    home4 = Home(price = 900000, stAddress = "1258 Nelm Street", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.9312285992078, longitude = -121.691996556812, lotSize = 2800, beds = 2, bath = 1, status = "For sale",userId='2')
    home5 = Home(price = 850000, stAddress = "1505 Alexander Avenue", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 38.006211594551, longitude = -121.859342026557, lotSize = 2600, beds = 4, bath = 2.5, status = "Rent",userId='2')
    home6 = Home(price = 800000, stAddress = "2700 EAST LELAND ROAD", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 38.0104880312425, longitude = -121.874341810101, lotSize = 2400, beds = 3, bath = 1.5, status = "Sale pending",userId='2')
    home7 = Home(price = 700000, stAddress = "200 Griffith Ln.", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.9294572258095, longitude = -121.70755693297, lotSize = 2000, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home8 = Home(price = 650000, stAddress = "855 Minnesota Ave", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.929660327068, longitude = -121.707814425022, lotSize = 1800, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home9 = Home(price = 600000, stAddress = "140 Birch St.	", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.9323342719326, longitude = -121.691309940913, lotSize = 1600, beds = 2, bath = 1, status = "For sale",userId='1')
    home10 = Home(price = 550000, stAddress = "6651 Lone Tree Way	", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.9628145530703, longitude = -121.730503024968, lotSize = 1400, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home11 = Home(price = 500000, stAddress = "850 Second St.", city = "Brentwood", state = "CA", zipCode = 94513, latitude = 37.9371308864179, longitude = -121.69473862298, lotSize = 1200, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home12 = Home(price = 1000000, stAddress = "100 Wilson Rd.	", city = "Alamo", state = "CA", zipCode = 94507, latitude = 37.8692068526901, longitude = -122.029577379648, lotSize = 3200, beds = 2, bath = 1, status = "For sale",userId='1')
    home13 = Home(price = 950000, stAddress = "180 Hemme Ave.", city = "Alamo", state = "CA", zipCode = 94507, latitude = 37.8419380048982, longitude = -122.028706451038, lotSize = 3000, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home14 = Home(price = 900000, stAddress = "3001 Miranda Ave.", city = "Alamo", state = "CA", zipCode = 94507, latitude = 37.8574452806154, longitude = -122.020986235694, lotSize = 2800, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home15 = Home(price = 1000000, stAddress = "603 MAIN ST", city = "Pleasenton", state = "CA", zipCode = 94566, latitude = 37.663268408909, longitude = -121.875692572034, lotSize = 3200, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home16 = Home(price = 950000, stAddress = "400 OLD BERNAL AVE.", city = "Pleasenton", state = "CA", zipCode = 94566, latitude = 37.6584814021871, longitude = -121.881318186829, lotSize = 3000, beds = 2, bath = 1, status = "For sale",userId='1')
    home17 = Home(price = 900000, stAddress = "218 Ray St", city = "Pleasenton", state = "CA", zipCode = 94566, latitude = 37.6643927538384, longitude = -121.872735118422, lotSize = 2800, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home18 = Home(price = 850000, stAddress = "2244 Water Street", city = "Pleasenton", state = "CA", zipCode = 94566, latitude = 37.6286637312728, longitude = -121.808003410722, lotSize = 2600, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home19 = Home(price = 750000, stAddress = "1458 Logan Lane", city = "Hyward", state = "CA", zipCode = 94540, latitude = 37.628953555491, longitude = -122.064904956194, lotSize = 2200, beds = 2, bath = 1, status = "For sale",userId='1')
    home20 = Home(price = 700000, stAddress = "25800 Carlos Bee Blvd", city = "Hyward", state = "CA", zipCode = 94542, latitude = 37.6599135526149, longitude = -122.057053551656, lotSize = 2000, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home21 = Home(price = 650000, stAddress = "20103 Lake Chabot Rd", city = "Hyward", state = "CA", zipCode = 94546, latitude = 37.7000175080745, longitude = -122.088762830557, lotSize = 1800, beds = 3, bath = 1.5, status = "Sale pending",userId='1')
    home22 = Home(price = 600000, stAddress = "900 North Point St", city = "San Francisco", state = "CA", zipCode = 94109, latitude = 37.8063546851947, longitude = -122.422786827482, lotSize = 1600, beds = 2, bath = 1, status = "For sale",userId='1')
    home23 = Home(price = 1000000, stAddress = "2950 Kovar Road", city = "San Francisco", state = "CA", zipCode = 94117, latitude = 37.7260152437399, longitude = -122.403335786721, lotSize = 3200, beds = 2, bath = 1, status = "For sale",userId='1')
    home24 = Home(price = 950000, stAddress = "538 Vineyard Drive", city = "San Francisco", state = "CA", zipCode = 94117, latitude = 37.8040782986359, longitude = -122.410628402489, lotSize = 3000, beds = 4, bath = 2.5, status = "Rent",userId='1')
    home25 = Home(price = 900000, stAddress = "1574 Geneva Street", city = "San Francisco", state = "CA", zipCode = 94117, latitude = 37.7134348967612, longitude = -122.42986562648, lotSize = 2800, beds = 3, bath = 1.5, status = "Sale pending",userId='1')


    db.session.add(home1)
    db.session.add(home2)
    db.session.add(home3)
    db.session.add(home4)
    db.session.add(home5)
    db.session.add(home6)
    db.session.add(home7)
    db.session.add(home8)
    db.session.add(home9)
    db.session.add(home10)
    db.session.add(home11)
    db.session.add(home12)
    db.session.add(home13)
    db.session.add(home14)
    db.session.add(home15)
    db.session.add(home16)
    db.session.add(home17)
    db.session.add(home18)
    db.session.add(home19)
    db.session.add(home20)
    db.session.add(home21)
    db.session.add(home22)
    db.session.add(home23)
    db.session.add(home24)
    db.session.add(home25)

    db.session.commit()


def undo_homes():
    db.session.execute('TRUNCATE homes RESTART IDENTITY CASCADE;')
    db.session.commit()