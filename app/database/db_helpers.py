from app.extensions import db
from sqlalchemy import Table


def fetch_records(table: Table, **kwargs) -> tuple:
    """Queries database table to get records
    :table:
        The database table to query
        
    :kwargs:
        Keyword arguments to filter table records
    """
    if kwargs:
        records = db.session.execute(
            db.select(table)
            .filter_by(**kwargs)
        ).first()
        
    else:
        records = db.session.execute(db.select(table)).all()
        

def save_record(table: Table, **data) -> Table:
    """saves data to db and returns the record"""

    record = table(**data)

    db.session.add(record)
    db.session.commit()
    db.session.refresh(record)

    return record