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
    image27 = Image(homeId = 2, image = "https://www.google.com/imgres?imgurl=http%3A%2F%2Fparkerrealestateteam.com%2Ffiles%2F2011%2F08%2FLaurel-Creek-300-600x400.jpg&imgrefurl=http%3A%2F%2Fparkerrealestateteam.com%2Flisting%2F5934-laurel-creek-dr-pleasanton-ca-94588%2F&tbnid=8B4LpjtFCjXLyM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygFegUIARC9AQ..i&docid=rTGfdDKJIQQgyM&w=600&h=400&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygFegUIARC9AQ")
    image28 = Image(homeId = 3, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fpi.movoto.com%2Fp%2F12%2F40855618_0_miAZe3_p.jpeg&imgrefurl=https%3A%2F%2Fwww.movoto.com%2Fpleasanton-ca%2F387-mullin-ct-pleasanton-ca-94566%2Fpid_i3hgvaf38g%2F&tbnid=Q8afqUih7B950M&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygGegUIARC_AQ..i&docid=Qzeh0zHeUCyCFM&w=480&h=318&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygGegUIARC_AQ")
    image29 = Image(homeId = 4, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2F3347ba7ff7e15b55d41af32c963a36a0l-m569551847od-w480_h360.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FPleasanton_CA&tbnid=ZOCMgq7PjTnKlM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygHegUIARDBAQ..i&docid=ArKoC5m3qymZJM&w=480&h=317&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygHegUIARDBAQ")
    image30 = Image(homeId = 5, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmediavault.point2.com%2Fp2h%2Flisting%2F9819%2Fb21f%2F6f82%2F2df61a80412627854bfd%2Fwm_large.jpg&imgrefurl=https%3A%2F%2Fwww.propertyshark.com%2Fhomes%2FUS%2FReal-Estate-Listings%2FCA%2FPleasanton%2FWalnut-Glen.html&tbnid=LtdMUocJOF7c0M&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygJegUIARDGAQ..i&docid=pTvzXPvURszqfM&w=420&h=279&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygJegUIARDGAQ")
    image31 = Image(homeId = 6, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2Ff5e1fc3cc19cc6cbb52878bec27e7d4a-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fpleasanton-ca%2F&tbnid=AwOS38I2h0_VpM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygLegUIARDKAQ..i&docid=U6pqDLNU3khVuM&w=596&h=446&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygLegUIARDKAQ")
    image32 = Image(homeId = 7, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.cbhomes.com%2Fp%2F806%2F40674347%2F68d7a7be97564f3%2Foriginal.jpg&imgrefurl=https%3A%2F%2Fwww.coldwellbankerhomes.com%2Fca%2Fpleasanton%2F3720-w-ruby-hill-drive%2Fpid_593703%2F&tbnid=W877yyKGBZSGFM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygUegUIARDdAQ..i&docid=iGtOSui4NR8ahM&w=1024&h=768&itg=1&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygUegUIARDdAQ")
    image33 = Image(homeId = 8, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F10%2Fbigphoto%2F158%2F40942158_2.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2FCA%2FPleasanton%2F3053-Ferndale-Ct-94588%2Fhome%2F977965&tbnid=pz4LuPbhXNwHuM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygVegUIARDfAQ..i&docid=iDhEmiAnJ1vK3M&w=1280&h=853&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygVegUIARDfAQ")
    image34 = Image(homeId = 9, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Frentpath-res.cloudinary.com%2Ft_rp%2Ccs_tinysrgb%2Cfl_force_strip%2Cw_400%2Ch_240%2Cc_fill%2Cq_auto%3Alow%2Cdpr_1.0%2Ce_improve%2Fe_unsharp_mask%3A50%2F80c0cc3f24ec14ec7f584a505c48d438&imgrefurl=https%3A%2F%2Fwww.rent.com%2Fcalifornia%2Fpleasanton-houses&tbnid=z30jbZ6VGVtq3M&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygiegUIARCEAg..i&docid=PxZe1ZKjm2FpAM&w=400&h=240&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygiegUIARCEAg")
    image35 = Image(homeId = 10, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F45%2Fmbphoto%2F555%2FgenMid.OC19065555_2.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2FCA%2FHayward%2F29073-Eden-Shores-Dr-94545%2Fhome%2F2110938&tbnid=sgXSlp0q37AjCM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygAegUIARC4AQ..i&docid=NCmOkn99s353uM&w=623&h=414&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygAegUIARC4AQ")
    image36 = Image(homeId = 11, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2Fff5e60b27a6916a5b0efd8708645bf1cl-m2250613961od-w480_h360.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FHayward_CA&tbnid=xWIh0NyQnP2l3M&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygBegUIARC6AQ..i&docid=Ompxe5s_KVr4dM&w=480&h=292&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygBegUIARC6AQ")
    image37 = Image(homeId = 12, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F34c9e118cdd7d02a61b2cbaf4808f43d-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fhayward-ca%2F&tbnid=JyIZu1EQthbYnM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygCegUIARC9AQ..i&docid=wpkLfjFqWH6h8M&w=596&h=446&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygCegUIARC9AQ")
    image38 = Image(homeId = 13, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F139be8cce0add48fbe2fa255335ea791-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fhayward-ca%2Fnew-homes%2F&tbnid=kSOEyyUYP0EOsM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygFegUIARDFAQ..i&docid=zIBlRjkDtYQkQM&w=596&h=446&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygFegUIARDFAQ")
    image39 = Image(homeId = 14, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F022862c52875fceadb4068b9885c948b-cc_ft_1536.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fhomedetails%2F595-Olympic-Ave-Hayward-CA-94544%2F52978618_zpid%2F&tbnid=w4vnkaPa54JhQM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygHegUIARDJAQ..i&docid=wS6eFTykhkfk2M&w=1278&h=852&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygHegUIARDJAQ")
    image40 = Image(homeId = 15, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F55d50499e4b0b8db603593d1%2F1440109273577-5XBBV0LQF8H24OT3TY6E%2FMcConaghy%2BHouse.jpg%3Fformat%3D1500w&imgrefurl=https%3A%2F%2Fwww.haywardareahistory.org%2Fmcconaghy-house&tbnid=GAW2E_VKErlI5M&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygJegUIARDOAQ..i&docid=lrllcJPbVyE2MM&w=1500&h=1125&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygJegUIARDOAQ")
    image41 = Image(homeId = 16, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F10%2Fmbphoto%2F178%2FgenMid.40964178_1_0.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2Fcity%2F8439%2FCA%2FHayward%2Fvintage&tbnid=XBX2ZVrlqkhb3M&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygMegUIARDWAQ..i&docid=j-yVDUwraVY-nM&w=623&h=414&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygMegUIARDWAQ")
    image42 = Image(homeId = 17, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2F048f859f1f0671ed28e547daa90132d6l-m2691809627od-w480_h360.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FHayward_CA&tbnid=rPlZJLEMIHBloM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygPegUIARDeAQ..i&docid=Ompxe5s_KVr4dM&w=480&h=320&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygPegUIARDeAQ")
    image43 = Image(homeId = 18, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.trulia.com%2Fpictures%2Fthumbs_5%2Fzillowstatic%2Ffp%2Fd738e336a5b880e0f7a2e11f97436449-full.jpg&imgrefurl=https%3A%2F%2Fwww.trulia.com%2FCA%2FHayward%2F&tbnid=1slHlzyp7BNA5M&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygRegUIARDkAQ..i&docid=X7FuPGdA3amKZM&w=1024&h=683&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygRegUIARDkAQ")
    image44 = Image(homeId = 19, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.trulia.com%2Fpictures%2Fthumbs_5%2Fzillowstatic%2Ffp%2F0ddb6b3738674ad58ed4abccabb1df83-full.jpg&imgrefurl=https%3A%2F%2Fwww.trulia.com%2FCA%2FHayward%2F&tbnid=nfYg83ie0VIVyM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygSegUIARDnAQ..i&docid=X7FuPGdA3amKZM&w=1024&h=684&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygSegUIARDnAQ")
    image45 = Image(homeId = 20, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmediavault.point2.com%2Fp2h%2Flisting%2F8f79%2Fd46c%2Fcbcb%2F917a3bc2d2d3e8a60c98%2Fnwm_large.jpg&imgrefurl=https%3A%2F%2Fwww.point2homes.com%2FUS%2FReal-Estate-Listings%2FCA%2FHayward.html&tbnid=0bX2KvVzk45AYM&vet=12ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygkegUIARCfAg..i&docid=0fBU7Yz3yCvAwM&w=420&h=280&q=houses%20hayward%20ca&ved=2ahUKEwjA783q4MfyAhUWiZ4KHRffCbUQMygkegUIARCfAg")
    image46 = Image(homeId = 21, image = "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.bcre.com%2Fuploads%2Fagent-23%2FSunnyside_San_Francisco_Home.jpg&imgrefurl=http%3A%2F%2Fwww.bcre.com%2Fsunnyside-san-francisco-homes-for-sale.php&tbnid=7YSbhqIandxIxM&vet=12ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygDegUIARDGAQ..i&docid=0lcbzkG8O4OypM&w=720&h=480&q=san%20francisco%20ca%20houses&ved=2ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygDegUIARDGAQ")
    image47 = Image(homeId = 22, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F31%2F2c%2Fbc%2F312cbca2aa5a3469bdecc45ad5ed8e29.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F425519864787739644%2F&tbnid=YDYW8a5CXsuHTM&vet=12ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygQegUIARDkAQ..i&docid=3Im8svlu5iV-cM&w=1600&h=1200&q=san%20francisco%20ca%20houses&ved=2ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygQegUIARDkAQ")
    image48 = Image(homeId = 23, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.gtsstatic.net%2Freno%2Fimagereader.aspx%3Fimageurl%3Dhttps%253A%252F%252Fsir.azureedge.net%252F1253i215%252Fvxkwb14xztb94famsbrhdhghs6i215%26option%3DN%26h%3D472%26permitphotoenlargement%3Dfalse&imgrefurl=https%3A%2F%2Fwww.sothebysrealty.com%2Feng%2Fsales%2Fsan-francisco-ca-usa&tbnid=1r0oRLMBDd9BJM&vet=12ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygXegUIARDzAQ..i&docid=U0rWO7Wv_zPO7M&w=708&h=472&q=san%20francisco%20ca%20houses&ved=2ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygXegUIARDzAQ")
    image49 = Image(homeId = 24, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.gtsstatic.net%2Freno%2Fimagereader.aspx%3Fimageurl%3Dhttps%253A%252F%252Fsir.azureedge.net%252F1194i215%252Fe2hqw4bj2gej4kpym7cg2387v0i215%26option%3DN%26h%3D472%26permitphotoenlargement%3Dfalse&imgrefurl=https%3A%2F%2Fwww.sothebysrealty.com%2Feng%2Fsales%2Fsan-francisco-ca-usa&tbnid=if8kxHUCHCPFGM&vet=12ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygOegUIARDfAQ..i&docid=U0rWO7Wv_zPO7M&w=708&h=472&q=san%20francisco%20ca%20houses&ved=2ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygOegUIARDfAQ")
    image50 = Image(homeId = 25, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2Fba93366da8597c2d2c293dede92c83a6l-b4066334792od-w480_h360.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FForest-Hill_San-Francisco_CA&tbnid=xqV0LdbT2uG_uM&vet=12ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygmegUIARCkAg..i&docid=EEsUcAJiT0tIEM&w=480&h=320&q=san%20francisco%20ca%20houses&ved=2ahUKEwiwmKil48fyAhVHIzQIHUDhAuMQMygmegUIARCkAg")

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