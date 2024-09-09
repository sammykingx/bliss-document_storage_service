# Bliss Cloud Document Storage Service

This project is a cloud-based document storage service utilizing AWS S3. It allows users to upload, store, and manage documents securely in the cloud. The service provides a user-friendly web application interface for interacting with the document storage, ensuring easy access and management of documents.

## Features
- Secure Upload: Upload documents securely to AWS S3.
- Document Management: Retrieve, update, and delete documents.
- Scalability: Leverage AWS S3’s scalable storage infrastructure.
- Access Control: Manage access permissions for stored documents.
- Metadata Handling: Store and retrieve document metadata.

## Architecture

The Document Storage Service is built using the Model-View-Controller (MVC) architecture to ensure a clear separation of concerns and facilitate maintainability. The core components of the system include:

- Model: Represents the data layer of the application. It includes the definitions for document data and metadata, as well as interactions with the AWS S3 storage and the database. The model layer ensures data integrity and provides an abstraction over the storage mechanisms.

- View: The user interface layer of the application. It is built using modern web technologies to provide a responsive and intuitive experience for end-users. The view layer handles the presentation of data and user interactions, such as uploading documents and viewing document lists.

- Controller: The business logic layer of the application. It handles user requests, processes input data, interacts with the model to perform CRUD (Create, Read, Update, Delete) operations, and returns the appropriate views. The controller ensures that the correct operations are performed and that the application responds appropriately to user actions.

- AWS S3: Provides the underlying storage infrastructure. AWS S3 is used for storing documents securely and scalably. It offers high availability, durability, and performance for document storage needs.

- Database: The service employs PostgreSQL for its robust performance, reliability, and advanced features. PostgreSQL is chosen for its superior capabilities in handling complex queries, high transaction rates, and large volumes of data. The database design follows best practices to ensure optimized performance

- Authentication and Authorization: This component manages user authentication and access control. It ensures that only authorized users can access and manipulate the documents. Secure methods are used to handle user credentials and session management.


## Getting Started

### Prerequisites
- Python (v3.8 or higher)
- AWS Account

## Installation

- Clone the repository:
```bash
git clone https://github.com/sammykingx/bliss-document_storage_service.git
```
- Change directory `cd` to document-storage-service or open folder with code

- Create Virtual environment:
```bash
# for windows
$ python -m venv venv

# for mac or debian based linux distro
$ python3 -m venv venv
```

- Activate virtual envitonment
```bash
# for windows
$ venv\Scripts\activate

# for mac or debian based distros
$ source venv/bin/activate
```

- Install Project dependencies
```bash
$ pip install -r requirements.txt
```


## Configuration

- Create a `.env` file in the project root directory and provide values for the following variables:
```
APP_SECRET_KEY = ""
SERIALIZER_KEY = ""
DB_URL = ""
SMTP_HOST = ""
SMTP_PORT = ""
SMTP_MAIL = ""
SMTP_PWD = ""
USE_SSL = ""
```
- Create a `.flaskenv` file and provide values for the following variables.
```bash
FLASK_APP = 
FLASK_DEBUG= 
```

- Run the application:
```bash
$ flask run
```

Once the application is running, you can access the web interface to manage your documents.