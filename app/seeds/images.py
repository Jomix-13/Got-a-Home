from app.models import db, Image


def seed_images():
    image1 = Image(homeId = 1, image = "https://static01.nyt.com/images/2020/08/17/realestate/17WYG-CA-slide-28EI/17WYG-CA-slide-28EI-articleLarge.jpg?quality=75&auto=webp&disable=upscale")
    image2 = Image(homeId = 2, image = "https://www.nwhm.com/sites/default/files/2021-03/epic_IMG_854x650px.jpg")
    image3 = Image(homeId = 3, image = "https://saddletreehomes.com/wp-content/uploads/2020/05/14317_SpyglassHill_003-1024x684.jpg")
    image4 = Image(homeId = 4, image = "https://www.nwhm.com/sites/default/files/2021-03/epic_IMG_854x650px.jpg")
    image5 = Image(homeId = 5, image = "https://saddletreehomes.com/wp-content/uploads/2020/05/14317_SpyglassHill_003-1024x684.jpg")
    image6 = Image(homeId = 6, image = "https://saddletreehomes.com/wp-content/uploads/2020/05/14317_SpyglassHill_003-1024x684.jpg")
    image7 = Image(homeId = 7, image = "https://mcgaryhomes.com/Pics/new_construction.jpg")
    image8 = Image(homeId = 8, image = "https://www.buyboiserealestate.com/images/house_double_story14_bbre_755.jpg")
    image9 = Image(homeId = 9, image = "https://static01.nyt.com/images/2020/08/17/realestate/17WYG-CA-slide-28EI/17WYG-CA-slide-28EI-articleLarge.jpg?quality=75&auto=webp&disable=upscale")
    image10 = Image(homeId = 10, image = "https://nh.rdcpix.com/01ceffa66fadbefa6339314d8c9ffeade-f346180339od-w480_h360.jpg")
    image11 = Image(homeId = 11, image = "https://nh.rdcpix.com/04de69b065fe626168b4698e4e7f7351e-f1721549850od-w480_h360.jpg")
    image12 = Image(homeId = 12, image = "https://ap.rdcpix.com/1960513237/09d1bf99525689daecfb8ebddb93a754l-m0xd-w1020_h770_q80.jpg")
    image13 = Image(homeId = 13, image = "https://www.compass.com/ucfe-assets/homepage/homepage-v1.24.1/assets/hero_high_res.jpeg")
    image14 = Image(homeId = 14, image = "https://static01.nyt.com/images/2021/03/15/realestate/15WYG-CA-slide-DWG2/15WYG-CA-slide-DWG2-articleLarge.jpg?quality=75&auto=webp&disable=upscale")
    image15 = Image(homeId = 15, image = "https://www.rocketmortgage.com/resources-cmsassets/RocketMortgage.com/Article_Images/Large_Images/TypesOfHomes/types-of-homes-hero.jpg")
    image16 = Image(homeId = 16, image = "https://res.cloudinary.com/culturemap-com/image/upload/ar_4:3,c_fill,g_faces:center,w_980/v1620066223/photos/320158_original.jpg")
    image17 = Image(homeId = 17, image = "https://www.landonhomes.com/2017/wp-content/uploads/2021/02/697-Middleton-Exterior-1.jpg")
    image18 = Image(homeId = 18, image = "https://harbourhomes.com/revslider/media/12d6b-cypress-copper-rim_0018_DSC_3498.jpg")
    image19 = Image(homeId = 19, image = "http://d2kcmk0r62r1qk.cloudfront.net/imageSponsors/xlarge/2020_01_15_05_53_55_vista_dorado_plan_2_ext.jpeg")
    image20 = Image(homeId = 20, image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdiL8kK1woke8HDhehvrrgLGbhB472Hw0dYQ&usqp=CAU")
    image21 = Image(homeId = 21, image = "https://hmbtx.com/wp-content/uploads/2015/08/pexels-photo-186077.jpeg")
    image22 = Image(homeId = 22, image = "https://www.mountainluxury.com/thumbs/600x400/uploads/farmington.jpg")
    image23 = Image(homeId = 23, image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReyZGQx5HDeoGVf8r_-UM-dc1-VQar9vbc2rkve7Q2mX3MN8GkaeVJgY1hAs9dPtsw7pg&usqp=CAU")
    image24 = Image(homeId = 24, image = "https://static-30.sinclairstoryline.com/resources/media/8adb65ae-1a1f-481e-89ba-f7885a77852b-large16x9_ParadeofHomes025.jpg?1559755550687")
    image25 = Image(homeId = 25, image = "https://www.communie.com/wp-content/uploads/2011/11/WRIGHT-HOMES-COVER.jpg")
    image26 = Image(homeId = 1, image = "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.homevaluespleasanton.com%2Fwp-content%2Fuploads%2F2015%2F12%2Fhomes-for-sale-in-pleasanton-ca-1.jpg&imgrefurl=http%3A%2F%2Fwww.homevaluespleasanton.com%2Fpleasanton%2F&tbnid=r9YP0WPSEXTToM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygDegUIARC5AQ..i&docid=Ys_FrAW7cenSMM&w=1950&h=1604&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygDegUIARC5AQ")
    image27 = Image(homeId = 2, image = "https://www.gannett-cdn.com/presto/2020/07/24/PNAS/b6698e6b-0637-4261-af41-048c57659d69-Trace_Construction_Outdoor_Living_Photo_by_Reed_Brown.jpg")
    image28 = Image(homeId = 3, image = "https://image.cnbcfm.com/api/v1/image/103500764-GettyImages-147205632-2.jpg?v=1529471066")
    image29 = Image(homeId = 4, image = "https://www.texomashomepage.com/wp-content/uploads/sites/41/2019/10/get-paid-to-test-out-luxury-homes.jpg?strip=1")
    image30 = Image(homeId = 5, image = "https://lh3.googleusercontent.com/proxy/mqsvc_XHc8VSZVB7ljKx6aB72u0NdhucAbj2oi67sPtnJiCXE8mgHQiSNczAD_1XIsZbu7hSwFam0Rv10KrB6Yp86nnex63zuPLNsw3ItJvoJpJ0EhghdZBQFcw8r8E")
    image31 = Image(homeId = 6, image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw9owHEOiMdwdOXCCqQWo1-3rk5X-wwRZ7SmzzOMBN7aPA7Ju89mDjEilgzBs6aDxKPg0&usqp=CAU")
    image32 = Image(homeId = 7, image = "https://www.thepinnaclelist.com/wp-content/uploads/2017/01/01-Luxury-Residence-924-Bel-Air-Rd-Bel-Air-CA-USA-640x360.jpg")
    image33 = Image(homeId = 8, image = "http://img1.wsimg.com/isteam/ip/e83f947d-9616-42e7-a632-65939bf6ba3b/14480715_176731126067508_7289057717853478081_o.jpg")
    image34 = Image(homeId = 9, image = "https://www.texasrealestate.com/wp-content/uploads/LuxuryHome_640x390.jpeg")
    image35 = Image(homeId = 10, image = "https://www.thepinnaclelist.com/wp-content/uploads/2019/06/00-2057-Ridge-Mountain-Drive-Anmore-BC-Canada-640x360.jpg")
    image36 = Image(homeId = 11, image = "https://mediavault.point2.com/p2h/listing/ba37/465f/4a4d/e31ab890bcd5b010599a/nwm_large.jpg")
    image37 = Image(homeId = 12, image = "https://i.pinimg.com/originals/d9/fc/a8/d9fca87f5059063e16e0dbce74504034.jpg")
    image38 = Image(homeId = 13, image = "https://i.pinimg.com/originals/c7/58/43/c7584365f991ea6236fd1f19653f06a2.jpg")
    image39 = Image(homeId = 14, image = "https://robbreport.com/wp-content/uploads/2018/10/g-1.jpg?w=1000")
    image40 = Image(homeId = 15, image = "http://www.luxxu.net/blog/wp-content/uploads/2017/08/Luxury-Homes-That-Give-Modern-Living-A-Whole-New-Meaning-Heber-Utah.jpg")
    image41 = Image(homeId = 16, image = "http://cdn.home-designing.com/wp-content/uploads/2020/04/Luxury-house-exterior.jpg")
    image42 = Image(homeId = 17, image = "https://miro.medium.com/max/1200/1*H2Ypw3QkhETdVpS48EtEZg.jpeg")
    image43 = Image(homeId = 18, image = "https://img.gtsstatic.net/reno/imagereader.aspx?imageurl=https%3A%2F%2Fsir.azureedge.net%2F1253i215%2F6prs620zmsqp4vjnga995y9f27i215&option=N&h=472&permitphotoenlargement=false")
    image44 = Image(homeId = 19, image = "https://luxport-dev.s3.amazonaws.com/145277/1985-hicks-ave--san-jose-ca-usa-16-EXT.jpg")
    image45 = Image(homeId = 20, image = "https://i.pinimg.com/originals/90/bc/ff/90bcfff812ebf6b9c1bae2f5651d6ab0.jpg")
    image46 = Image(homeId = 21, image = "https://i.ytimg.com/vi/fuEefM4VAP8/hqdefault.jpg")
    image47 = Image(homeId = 22, image = "https://lh3.googleusercontent.com/proxy/oJ7lkGWtX7IaRftpqPpv_puW6iHA8aIIh-HqC9LoIJVoBfUDoMTeBdQDGU7bBJW8BuiIVX06vT8OLorLUQVcnLKDYdrZCmlygkCziV0HUsknO01CrlS-HO-t15wzKi0")
    image48 = Image(homeId = 23, image = "https://i.pinimg.com/originals/30/5d/1e/305d1ef6a4a7ff7be6b84bc0426ddfc5.jpg")
    image49 = Image(homeId = 24, image = "https://i2.wp.com/www.christiesrealestate.com/blog/wp-content/uploads/2020/09/arizona-contemporary.jpg?fit=1920%2C1280&ssl=1")
    image50 = Image(homeId = 25, image = "http://www.christies.com/media-library/images/features/articles/2015/10/28/luxury-living-contemporary/Massachusetts-Main.jpg")

    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.add(image9)
    db.session.add(image10)
    db.session.add(image11)
    db.session.add(image12)
    db.session.add(image13)
    db.session.add(image14)
    db.session.add(image15)
    db.session.add(image16)
    db.session.add(image17)
    db.session.add(image18)
    db.session.add(image19)
    db.session.add(image20)
    db.session.add(image21)
    db.session.add(image22)
    db.session.add(image23)
    db.session.add(image24)
    db.session.add(image25)
    db.session.add(image26)
    db.session.add(image27)
    db.session.add(image28)
    db.session.add(image29)
    db.session.add(image30)
    db.session.add(image31)
    db.session.add(image32)
    db.session.add(image33)
    db.session.add(image34)
    db.session.add(image35)
    db.session.add(image36)
    db.session.add(image37)
    db.session.add(image38)
    db.session.add(image39)
    db.session.add(image40)
    db.session.add(image41)
    db.session.add(image42)
    db.session.add(image43)
    db.session.add(image44)
    db.session.add(image45)
    db.session.add(image46)
    db.session.add(image47)
    db.session.add(image48)
    db.session.add(image49)
    db.session.add(image50)

    db.session.commit()


def undo_images():
    db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE;')
    db.session.commit()