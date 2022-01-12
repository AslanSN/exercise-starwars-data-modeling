# StarWars blog database with Python's SQLAlchemy 

## 💻 Instalation

1. Get inside the environment `$ pipenv shell`

2. Install all dependencies `$ pipenv install`

3. Open the file `diagram.png` to check out your UML diagram!


## 📝Instructions received

Your Job is to update the `src/models.py` file with the code needed to replicate the Starwars data model.

The project is using the SQLAlchemy Python library to generate the database.

- Your project must have a table `User` that will represent your blog users.
- Your blog users will be able to login and save their favorite planets and characters.
- The database should store the user favorites.
- The database should store characters and planets.
- What other tables do you think a blog like this might have?
- What properties should go inside the user? or inside the Character or Favorite table?
- What are the relationships between those tables?
- Please add at least 4 models with all of its properties.
- Generate the diagram.png file at the end by running `$ python3 models.py` on the console.

# My Code

For this exercise I just settled 5 tables:

## 1. `User` 

This table must match loading demands as a pasword and an email, that, of course, are `not nullable`.
```JavaScript
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    surname = Column(String(250))
    email = Column(String(60), nullable=False)
    password = Column(String(30), nullable = False)
    subscription_date = Column(String(60))
```
 The user is the main Father table which has 2 children, for this I setted up two relationships with them as `one to many`:
```JavaScript
    fav_planet = relationship('Favorite planet', back_populates='FavPlanet.favPl_id', primaryjoin='User.id==FavPlanet.favPl_id', lazy='dynamic')
    fav_char = relationship('Favorite character', back_populates='FavChar.favCh_id', primaryjoin='User.id==FavChar.favCh_id', lazy='dynamic')
```
> ### --`User` children--
> ### 2. `FavChar`
> Son of User it determines which characters of the Star Wars world are favorited by the user.
>
>```JavaScript
>class FavChar(Base):
>   __tablename__ = 'Favorite character'
>    favChr_id = Column(Integer, primary_key=True, autoincrement=True)
>    user_favChr_id = Column(Integer, ForeignKey(User.id))
>    fav_character = Column(Integer, ForeignKey(Character.char_id))
> ```
> ### 3. `FavPlanet`
>Also son of User it deploys a planet that is favorited by the User, being many of them.
>```JavaScript
> class FavPlanet(Base):
>   __tablename__ = 'Favorite planet'
>    favPl_id = Column(Integer, primary_key=True, autoincrement=True)
>    user_favPl_id = Column(Integer, ForeignKey(User.id))
>     fav_planet = Column(Integer, ForeignKey(Planet.planet_id))
>```
> As you can observe, in those two you have an `id` for each planet or char faved, and `user_..._id` that connects it with the main planet or char which is stored there.
>
>For those 2 tables work it is, indeed, needed two other independent tables, brothers of User, with the thata of each character and each planet.
### `User` Brothers
## 4. `Planet`
It just stores each planet individually which its proper `id` and `planet_name`.
```JavaScript
class Planet(Base):
    __tablename__ = 'Planet'
    planet_id = Column(Integer, primary_key=True, autoincrement=True)
    planet_name = Column(String(30))
```
## 5. `Character`
As the one before, it stores the chacacter with his name, surname, born planet and the planet actually living in.

```JavaScript
class Character(Base):
    __tablename__ = 'Character'
    char_id = Column(Integer, primary_key=True, autoincrement=True)
    char_name = Column(String(200))
    char_surName = Column(String(200))
    char_planet = Column(Integer, ForeignKey(Planet.planet_id))
    planet_now = Column(String(30))    
```

>_That's all folks,_
>
>_thank you for reading!_
>
>_**AslanSN**_