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


def document_filter_query(table: Table, search_input: str, doc_category:str, client_branch: str) -> list[Row]:
    query = table.query
    conditions = []

    if search_input:
        conditions.append(table.client_id.ilike(f'%{search_input}%'))
        conditions.append(table.file_id.ilike(f'%{search_input}%'))
        conditions.append(table.doc_id.ilike(f'%{search_input}%'))
    if doc_category:
        conditions.append(table.category.ilike(f'%{doc_category}%'))
    if client_branch:
        conditions.append(table.branch.ilike(f'%{client_branch}%'))

    if conditions:
        query = query.filter(or_(*conditions))

    results = query.all()
    return results