CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name varchar(20) NOT NULL
    email varchar(30)  UNIQUE NOT NULL,
    password varchar(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE files(
    id SERIAL PRIMARY KEY,
    file_name varchar(20) NOT NULL,
    file_type varchar(20) NOT NULL,
    file_size int NOT NULL,
    file_path TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_id int REFRENCES users(id) ON DELETE  CASCADE,
    folder_id int REFRENCES folders(id) on DELETE Set NULL,
    version int DEFAULT 1,
    shared_with int[] NOT NULL
    
    
    
);
