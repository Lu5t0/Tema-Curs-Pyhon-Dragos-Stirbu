from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase,sessionmaker

engine= create_engine("mysql://root:6791101290.D@localhost:3306/zoo")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String,unique=True, nullable=False)
    email = Column(String,unique=True)
    hashed_password = Column(String,nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# session.add(User(username="admin", email="admin@yahoo.com", hashed_password="parola"))
# session.commit()

class Species(Base):
    __tablename__ = "species"
    species_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)

species_list = [
    Species(name='Leu', category='Mamifer', description='Animal de pradă, regăsit în savană'),
    Species(name='Elefant', category='Mamifer', description='Cel mai mare animal terestru, herbivor'),
    Species(name='Pinguin', category='Pasăre'),
    Species(name='Tigru', category='Mamifer', description='Carnivor, prădător în jungle'),
    Species(name='Girafă', category='Mamifer', description='Animal cu gât lung, în savană'),
    Species(name='Cameleon', category='Reptilă', description='Reptilă cu capacitatea de a-și schimba culoarea'),
    Species(name='Delfin', category='Mamifer', description='Animal acvatic, foarte inteligent'),
    Species(name='Șarpe', category='Reptilă', description='Animal fără membre, cu corp lung și subțire'),
    Species(name='Urs', category='Mamifer', description='Animal puternic, omnivor, în pădure'),
    Species(name='Vultur', category='Pasăre', description='Prădător zburător, cu zbor înalt')
]
# session.add_all(species_list)
# session.commit()

# for sp in session.query(Species).all():
#     print(sp.name)

# mamifers = session.query(Species.name).filter(Species.category == 'Mamifer').all()
# print(mamifers)

# species_to_update = session.query(Species).filter(Species.name == 'Pinguin').first()
#
# if species_to_update:
#     species_to_update.description = 'Animal adaptat pentru mediul polar, cu corp acoperit de penaj și capabil să înoate'
#     session.commit()
#     print(f'Descrierea pentru {species_to_update.name} a fost actualizată.')
# else:
#     print("Specia nu a fost găsită.")


# session.query(Species).filter(Species.category == 'Pasăre').delete()
# session.commit()
# print("Toate speciile din categoria 'Pasare' au fost șterse.")