import sqlite3

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


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

try:
    c.execute("INSERT INTO {tn} ({i1},  {i2}, {i3},  {i4}, {i5},  {i6}, {i7},  {i8},\
     {i9},  {i10}, {i11},  {i12}, {i13},  {i14}, {i15}) VALUES\
     ({fi1},  {fi2}, {fi3},  {fi4}, {fi5},  {fi6}, {fi7},  {fi8},\
     {fi9},  {fi10}, {fi11},  {fi12}, {fi13},  {fi14}, {fi15})".\
     format(
tn= table_name, i1=id1, i2=id2, i3=id3, i4=id4, i5=id5, i6=id6, i7=id7, i8=id8, i9=id9, i10=id10,
i11=id11, i12=id12, i13=id13, i14=id14, i15=id15,
fi1=f1, fi2=f2, fi3=f3, fi4=f4, fi5=f5, fi6=f6, fi7=f7, fi8=f8, fi9=f9, fi10=f10,
fi11=f11, fi12=f12, fi13=f13, fi14=f14, fi15=f15))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

conn.commit()
conn.close()
