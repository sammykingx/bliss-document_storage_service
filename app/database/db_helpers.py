from app.extensions import db
from sqlalchemy import or_, Row, Table


def fetch_records(table: Table, **kwargs) -> Row:
    """Queries database table to get records
    :table:
        The database table to query
        
    :kwargs:
        Keyword arguments to filter table records
    """
    if kwargs:
        records = table.query.filter_by(**kwargs).all()
        
    else:
        records = table.query.all()
    
    return records

def fetch_record(table: Table, record_id: str) -> Row:
    """Queries database table to get a single record
    :table:
        The database table to query
        
    :record_id:
        The id of the record to get
    """
    record = table.query.get(record_id)
    return record
   

def save_record(table: Table, **data) -> Row:
    """saves data to db and returns the record"""

    record = table(**data)

    db.session.add(record)
    db.session.commit()
    db.session.refresh(record)

    return record


def document_filter_query(table: Table, search_input: str, doc_category:str, client_branch: str,) -> list[Row]:
    query = table.query
    conditions = []

    if search_input:
        conditions.append(table.client_id.ilike(f'%{search_input}%'))
        conditions.append(table.file_id.ilike(f'%{search_input}%'))
        conditions.append(table.doc_id.ilike(f'%{search_input}%'))
        
    if doc_category:
        conditions.append(table.doc_category.ilike(f'%{doc_category}%'))
        
    if client_branch:
        conditions.append(table.client_branch.ilike(f'%{client_branch}%'))

    if conditions:
        query = query.filter(or_(*conditions))

    results = query.all()
    return results


def fetch_recent_files(table: Table, limit: int=7, **kwargs) -> list[Row]:
    record = table.query.filter_by(**kwargs).order_by(table.upload_time.desc()).limit(limit).all()
    return record

def fetch_recent_activity(table: Table, limit: int=7) -> list[Row]:
    record = table.query.order_by(table.created_at.desc()).limit(limit).all()
    return record

def update_record(table: Table, record_id: str, **data) -> Row:
    record = table.query.get(record_id)
    for key, value in data.items():
        setattr(record, key, value)

    db.session.commit()
    db.session.refresh(record)

    return record