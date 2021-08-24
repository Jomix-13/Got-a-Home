from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    Demo = User(
        username="Demo", email="Demo@email.com", password="demo", profilepic="https://news.blr.com/app/uploads/sites/3/2018/07/Demo-5.jpg")
    John = User(
        username="John", email="John@email.com", password="demo", profilepic="https://media-exp1.licdn.com/dms/image/C4D03AQHrMl3CfenA2w/profile-displayphoto-shrink_200_200/0/1517529181712?e=1632960000&v=beta&t=4JAXxiLdfV1MtX1q61MOXz2rdZYqRfoE37HzX2zlq6E")
    Vero = User(
        username="Vero", email="Vero@email.com", password="demo", profilepic="https://thumbs.dreamstime.com/z/female-silhoutte-avatar-default-profile-picture-photo-placeholder-vector-illustration-130555145.jpg")
    David = User(
        username="David", email="David@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    Youssef = User(
        username="Youssef", email="Youssef@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    Messi = User(
        username="Messi", email="Messi@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    Christiano = User(
        username="Christiano", email="Christiano@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    Parthenia = User(
        username="Parthenia", email="Parthenia@email.com", password="demo", profilepic="https://thumbs.dreamstime.com/z/female-silhoutte-avatar-default-profile-picture-photo-placeholder-vector-illustration-130555145.jpg")
    MoSalah = User(
        username="MoSalah", email="MoSalah@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    Javier = User(
        username="Javier", email="Javier@email.com", password="demo", profilepic="https://www.pngitem.com/pimgs/m/35-350426_profile-icon-png-default-profile-picture-png-transparent.png")
    
    db.session.add(Demo)
    db.session.add(John)
    db.session.add(Vero)
    db.session.add(David)
    db.session.add(Youssef)
    db.session.add(Messi)
    db.session.add(Christiano)
    db.session.add(Parthenia)
    db.session.add(MoSalah)
    db.session.add(Javier)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
