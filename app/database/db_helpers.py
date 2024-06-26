from app.extensions import db
from sqlalchemy import Table, Row


def fetch_records(table: Table, **kwargs) -> Row:
    """Queries database table to get records
    :table:
        The database table to query
        
    :kwargs:
        Keyword arguments to filter table records
    """
    if kwargs:
        records = table.query.filter_by(**kwargs).first()
        
    else:
        records = table.query.all()
    
    return records
   

def save_record(table: Table, **data) -> Row:
    """saves data to db and returns the record"""

    record = table(**data)

    db.session.add(record)
    db.session.commit()
    db.session.refresh(record)

    return record