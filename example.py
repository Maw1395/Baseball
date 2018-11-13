import sqlalchemy as db

engine = db.create_engine('sqlite:///project.db')
connection = engine.connect()
metadata = db.MetaData()
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)
sqlite_file = 'project.db'
table_name = 'PlateAppearance'
id1="Team" 
id2="Year"
id3="Game_Number" 
id4="Pitcher" 
id5="Strike" 
id6="Ball" 
id7="Pitches" 
id8="Outs" 
id9="Inning" 
id10="Slugging" 
id11="Obp" 
id12="Ops" 
id13="War" 
id14="Hand" 
id15="Outcome" 

f1="ARZ"
f2=1
f3=1
f4="BET"
f5=1
f6=1
f7=1
f8=1
f9=1
f10=1
f11=1
f12=1
f13=1
f14="L"
f15="hit"

connection.execute(PlateAppearance.insert().values(Team= f1,
Year = f2,
Game_Number = f3,
Pitcher= f4,
Strike = f5,
Ball= f6,
Pitches = f7,
Outs = f8,
Inning = f9,
Slugging = f10,
Obp = f11,
Ops = f12,
War = f13,
Hand = f14,
Outcome=f15))