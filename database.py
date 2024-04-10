from sqlalchemy import create_engine, MetaData, Table, Base, Session  

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "Careers"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for jobs in session.query(title).order_by(title.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(jobs.id, jobs.name))
session.close()