from sqlalchemy import *
from migrate import *

meta = MetaData()

PlateAppearance = Table(
	'PlateAppearance', meta,
	Column('Team', String(3), primary_key=True),
	Column('Year', Integer, primary_key=True),
	Column('Game_Number', Integer, primary_key=True),
	Column('Pitcher', String(40)),
	Column('Strike', Integer),
	Column('Ball', Integer),
	Column('Pitches', Integer),
	Column('Outs', Integer),
	Column('Inning', Integer),
	Column('Slugging', Float),
	Column('Obp', Float),
	Column('Ops', Float),
	Column('War', Float),
	Column('Hand', String(1)),
	Column('Outcome', String(120)),
)
'''
PithcerGeneralStats = Table(
	'PithcerGeneralStats', meta,
	Column('Team', String(40), primary_key=True),
	Column('Year', String(40)),
	Column('Game_Number', String(40)),
	Column('Pitcher', String(40)),
	Column('Strike', String(40)),
	Column('Ball', String(40)),
	Column('Pitches', String(40)),
	Column('Outs', String(40)),
	Column('Inning', String(40)),
	Column('Slugging', String(40)),
	Column('Obp', String(40)),

	)
'''
def upgrade(migrate_engine):
	meta.bind = migrate_engine
	PlateAppearance.create()


def downgrade(migrate_engine):
   meta.bind = migrate_engine
   PlateAppearance.drop()
