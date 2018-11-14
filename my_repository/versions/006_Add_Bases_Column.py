from sqlalchemy import *
from migrate import *


meta = MetaData()

PlateAppearance = Table(
	'PlateAppearance', meta,
	Column('Team', String(3), primary_key=True),
	Column('Year', Integer, primary_key=True),
	Column('Game_Number', Integer, primary_key=True),
	Column('Batter_Number', Integer, primary_key=True),
	Column('Pitcher', String(40)),
	Column('Strike', Integer),
	Column('Ball', Integer),
	Column('Pitches', Integer),
	Column('Outs', Integer),
	Column('Inning', Integer),
	Column('Slugging', Float),
	Column('Obp', Float),
	Column('Ops', Float),
	Column('Runs',Integer),
	Column('Bases', String(3)),
	Column('Outcome', String(120)),
)

def upgrade(migrate_engine):
	meta.bind = migrate_engine
	PlateAppearance.create()


def downgrade(migrate_engine):
   meta.bind = migrate_engine
   PlateAppearance.drop()

