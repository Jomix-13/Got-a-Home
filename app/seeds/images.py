from app.models import db, Image


def seed_images():
    image1 = Image(homeId = 1, image = "https://www.google.com/search?q=houses+brentwood+ca&rlz=1C1CHBF_enUS915US916&sxsrf=ALeKk00GM9Mt7tQMY3ppVhT9VEVgxqunAg:1629741062621&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjYmvPI2sfyAhXrJzQIHXNIBWkQ_AUoAXoECAEQAw&biw=1920&bih=937#imgrc=eBt3yxLw6FX0dM")
    image2 = Image(homeId = 2, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2F1960513237%2F09d1bf99525689daecfb8ebddb93a754l-m0xd-w1020_h770_q80.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F384-Fletcher-Ln_Brentwood_CA_94513_M17121-70538&tbnid=vJXzSpEB30kAlM&vet=12ahUKEwjN_YvK2sfyAhUYgZ4KHf_mA5QQMygBegUIARC9AQ..i&docid=qHAAVOee__uxQM&w=1020&h=677&q=houses%20brentwood%20ca&ved=2ahUKEwjN_YvK2sfyAhUYgZ4KHf_mA5QQMygBegUIARC9AQ")
    image3 = Image(homeId = 3, image = "https://www.google.com/search?q=houses+brentwood+ca&rlz=1C1CHBF_enUS915US916&sxsrf=ALeKk00GM9Mt7tQMY3ppVhT9VEVgxqunAg:1629741062621&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjYmvPI2sfyAhXrJzQIHXNIBWkQ_AUoAXoECAEQAw&biw=1920&bih=937#imgrc=DFYqBTSFeYxqWM")
    image4 = Image(homeId = 4, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F10%2Fmbphoto%2F938%2FgenMid.40863938_4.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2FCA%2FBrentwood%2F402-Princess-Way-94513%2Fhome%2F142978165&tbnid=OEm4Gx8Fs_gtrM&vet=12ahUKEwjN_YvK2sfyAhUYgZ4KHf_mA5QQMygDegUIARDBAQ..i&docid=Py4iDrguBRahGM&w=623&h=414&q=houses%20brentwood%20ca&ved=2ahUKEwjN_YvK2sfyAhUYgZ4KHf_mA5QQMygDegUIARDBAQ")
    image5 = Image(homeId = 5, image = "https://www.google.com/search?q=houses+brentwood+ca&rlz=1C1CHBF_enUS915US916&sxsrf=ALeKk00GM9Mt7tQMY3ppVhT9VEVgxqunAg:1629741062621&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjYmvPI2sfyAhXrJzQIHXNIBWkQ_AUoAXoECAEQAw&biw=1920&bih=937#imgrc=y-72H8IsS521QM")
    image6 = Image(homeId = 6, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2Fd0584eb510510c8bdfaa058bf73062ad-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fbrentwood-ca%2F&tbnid=X4oacPQM71hfrM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygGegUIARDIAQ..i&docid=5p1BSrLhCocesM&w=596&h=446&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygGegUIARDIAQ")
    image7 = Image(homeId = 7, image = "https://www.google.com/imgres?imgurl=http%3A%2F%2Fd2kcmk0r62r1qk.cloudfront.net%2FimageSponsors%2Fxlarge%2F2020_01_15_05_53_55_vista_dorado_plan_2_ext.jpeg&imgrefurl=https%3A%2F%2Fwww.buzzbuzzhome.com%2Fus%2Fvista-dorado&tbnid=zzoqeYal_fqfHM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygIegUIARDNAQ..i&docid=_NR7bjCqiys9OM&w=1920&h=658&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygIegUIARDNAQ")
    image8 = Image(homeId = 8, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F145275fc4b27f414a8a29e51e929ff5f-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fbrentwood-ca%2Fbank-owned%2F&tbnid=JUZX0poXwqorKM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygJegUIARDPAQ..i&docid=5ptTU_y_m0DTNM&w=596&h=446&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygJegUIARDPAQ")
    image9 = Image(homeId = 9, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.55places.com%2Fareas%2Fphotos%2Foriginal%2F1e9b345b9939a8591703ee0b1c5fd408.jpg&imgrefurl=https%3A%2F%2Fwww.55places.com%2Fcalifornia%2Fcommunities%2Fsummerset&tbnid=-lwNoaTKMT5jCM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygKegUIARDRAQ..i&docid=4Kaz8Zgez7sF8M&w=800&h=533&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygKegUIARDRAQ")
    image10 = Image(homeId = 10, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Fp_e%2FISyrvis4e4ualb0000000000.jpg&imgrefurl=https%3A%2F%2Fpropertywalls.blogspot.com%2F2019%2F02%2Fproperty-for-sale-in-brentwood-ca.html&tbnid=GhAWmRwXeKZpOM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygLegUIARDTAQ..i&docid=r9nXkcHJ0EtoyM&w=596&h=446&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygLegUIARDTAQ")
    image11 = Image(homeId = 11, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2F9a99434f71cc471fe82e0b7484d532bdl-m2253837391xd-w1020_h770_q80.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F568-Caraway-Dr_Brentwood_CA_94513_M28134-96502&tbnid=ZpxvAwzTHr0a8M&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygMegUIARDVAQ..i&docid=FtHXQ-M8CFEr_M&w=1020&h=679&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygMegUIARDVAQ")
    image12 = Image(homeId = 12, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.caldecott.com%2Fimages%2Flist_photos%2FMAXEBRDI40892796.jpg&imgrefurl=https%3A%2F%2Fwww.caldecott.com%2F%3Fpage%3Dcity_search%26city%5B%5D%3DBrentwood%26pref_beds%3D0%26pref_baths%3D0%26pref_home%3Dyes%26pref_condo%3Dyes%26action%3Dnewsearch&tbnid=olUQPetFxRadOM&vet=12ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygOegUIARDZAQ..i&docid=gXv6ZDAhw0KJfM&w=1280&h=853&q=houses%20brentwood%20ca&ved=2ahUKEwiiufm-28fyAhUCg54KHXJ8BVAQMygOegUIARDZAQ")
    image13 = Image(homeId = 13, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F88d4a7bb4fd93dcb8433fca46bac143b-p_h.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Fhomedetails%2F322-Lark-Ln-Alamo-CA-94507%2F64781792_zpid%2F&tbnid=9SmOqoayhIN4sM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygAegUIARCuAQ..i&docid=o8Sbkc8YJlbQGM&w=550&h=413&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygAegUIARCuAQ")
    image14 = Image(homeId = 14, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.elliman.com%2Fcalifornia%2Flocalimagereader.ashx%3Fimageurl%3Dhttps%253A%252F%252Fmediall.rapmls.com%252Fsfarmls%252Flistingpics%252Fbigphoto%252F2020%252F02%252F18%252Fc377e26f-236e-4da8-a8a5-71c29b450d24.jpg%26imagecache%3Dtrue&imgrefurl=https%3A%2F%2Fwww.elliman.com%2Fcalifornia%2Fsales%2Fdetail%2F512-l-680-82_494916%2F10-serenity-lane-white-gate-alamo-ca-94507&tbnid=6TEXkQndwFk2JM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygCegUIARCyAQ..i&docid=t9Us1tx5HRpbYM&w=1500&h=1000&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygCegUIARCyAQ")
    image15 = Image(homeId = 15, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fap.rdcpix.com%2F351583364%2Fa9371e91cdbfd078a98dc9bf9bc98e7el-m0xd-w1020_h770_q80.jpg&imgrefurl=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F396-Golden-Grass-Dr_Alamo_CA_94507_M26774-59884&tbnid=9OHSSZsZjI8wPM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygEegUIARC3AQ..i&docid=cNjpKOu701GgGM&w=1020&h=679&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygEegUIARC3AQ")
    image16 = Image(homeId = 16, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fd2787ndpv5cwhz.cloudfront.net%2Ffdec741b1168d2a4588ba2235259e103ba066451_original.jpg&imgrefurl=https%3A%2F%2Fwww.compass.com%2Flisting%2F331-corrie-place-alamo-ca-94507%2F207194946283866897%2F&tbnid=TWzLh9l5Iah_OM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygFegUIARC5AQ..i&docid=Dn7bpwDcPsHqxM&w=1280&h=853&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygFegUIARC5AQ")
    image17 = Image(homeId = 17, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fnyc3.digitaloceanspaces.com%2Ftheochomesearch%2F2018%2F02%2F170-tracy-ln_386255.jpg&imgrefurl=http%3A%2F%2Fwww.theochomesearch.com%2Fhouses-for-sale-in-alamo-ca&tbnid=bQPPefRv4Ny3yM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygIegUIARC_AQ..i&docid=eA0WRub00h1boM&w=1280&h=854&itg=1&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygIegUIARC_AQ")
    image18 = Image(homeId = 18, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F10%2Fmbphoto%2F126%2FgenMid.40919126_0.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2FCA%2FAlamo%2F950-Forest-Ln-94507%2Fhome%2F2098530&tbnid=C7tfpCI9yq29jM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygLegUIARDHAQ..i&docid=lhrIWemBHTKr8M&w=623&h=414&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygLegUIARDHAQ")
    image19 = Image(homeId = 19, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmediavault.point2.com%2Fp2h%2Flisting%2Fd867%2F3c0e%2Ff593%2F9621efd98093392847cc%2Fnwm_large.jpg&imgrefurl=https%3A%2F%2Fwww.point2homes.com%2FUS%2FReal-Estate-Listings%2FCA%2FAlamo.html&tbnid=UoRVMZ2BH-WE0M&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygOegUIARDOAQ..i&docid=CwmHLXN6YAOeXM&w=420&h=280&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygOegUIARDOAQ")
    image20 = Image(homeId = 20, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphotos.zillowstatic.com%2Ffp%2F1710561b09e379a9df936ebf498cb4ea-p_e.jpg&imgrefurl=https%3A%2F%2Fwww.zillow.com%2Falamo-ca%2F&tbnid=TLMLmV7A1HnMkM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygTegUIARDYAQ..i&docid=14mpvUfBw6_7WM&w=596&h=446&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygTegUIARDYAQ")
    image21 = Image(homeId = 21, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fssl.cdn-redfin.com%2Fphoto%2F10%2Fbigphoto%2F954%2F40935954_0.jpg&imgrefurl=https%3A%2F%2Fwww.redfin.com%2FCA%2FAlamo%2F1632-Via-Romero-94507%2Fhome%2F607143&tbnid=2zygTG9VtxGiNM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygbegUIARDzAQ..i&docid=Fe2Wjp5YAewd1M&w=1280&h=853&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygbegUIARDzAQ")
    image22 = Image(homeId = 22, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm1.cbhomes.com%2Fp%2F8%2F40963105%2Fc0Ab6de55d1d491%2Fs23cc.jpg&imgrefurl=https%3A%2F%2Fwww.coldwellbankerhomes.com%2Fca%2Falamo%2F&tbnid=-qkcboVS-42ZGM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygeegUIARD5AQ..i&docid=ssrTKDwTsC_s3M&w=308&h=205&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMygeegUIARD5AQ")
    image23 = Image(homeId = 23, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm1.cbhomes.com%2Fp%2F8%2F40960758%2F9B9403E3D697400%2Fs23cc.jpg&imgrefurl=https%3A%2F%2Fwww.coldwellbankerhomes.com%2Fca%2Falamo%2F&tbnid=qpz8Krks-L4WJM&vet=12ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMyguegUIARCbAg..i&docid=ssrTKDwTsC_s3M&w=308&h=205&q=houses%20alamo%20ca&ved=2ahUKEwjx-_SE3cfyAhV4JDQIHTxwCtsQMyguegUIARCbAg")
    image24 = Image(homeId = 24, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fpi.movoto.com%2Fp%2F12%2F40826813_0_Jr7eVu_p.jpeg&imgrefurl=https%3A%2F%2Fwww.movoto.com%2Fpleasanton-ca%2F1181-germano-way-pleasanton-ca-94566-12_40390139%2F&tbnid=0nEfC2AjGxe3TM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygBegUIARC1AQ..i&docid=fXkLvUreANk9wM&w=480&h=359&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygBegUIARC1AQ")
    image25 = Image(homeId = 25, image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fhomefoliomedia.com%2Fwp-content%2Fuploads%2F2015%2F01%2F1926-Clover-Court-Pleasanton.jpg&imgrefurl=https%3A%2F%2Fhomefoliomedia.com%2Fopen-house-1926-clover-ct-pleasanton-ca-94588%2F&tbnid=sJSUgMgOhCVpPM&vet=12ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygCegUIARC3AQ..i&docid=FTNvqtbc2rh3_M&w=3456&h=2304&q=pleasanton%20ca%20houses&ved=2ahUKEwik8oD83sfyAhUGr54KHZEcDygQMygCegUIARC3AQ")
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