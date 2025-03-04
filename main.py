
from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

user_db = []



@app.post("/Register")
def register(user: User):
    for reg_user in user_db:
        if reg_user.email ==  user.email: 
            raise HTTPException(staus_code = 400, detail = "User Alread Exists")
    user_db.append(user)
    return {"message": f"User {user.name}Registered"}


@app.post("/Login")
def login(user: User):
    for reg_user in user_db:
        if reg_user.email == user.email and reg_user.password == user.password:
            return {"message": f"User {user.name} has successfully logged in"}
        else:
            raise HTTPException(status_code = 400, detail = "Invalid Credentials. Passowrd or Email is incorrect")
@app.post("/Logout")
def logout(user: User):
    return {"message": f"User {user.name} has successfully logged out"}

@app.post("/UploadFfile")
def upload_file():
    pass

@app.get("/listfiles")
def list_files():
    pass

@app.put("/movefile")
def move_file():
    pass

@app.post("/copyfile")
def copy_file():
    pass

@app.post("renamefile")
def reanem_file():
    pass

@app.get("/DownloadFile")
def download_file():
    pass

@app.delete("/DeleteFile")
def delete_file():
    pass

@app.post("/CreateFolder")
def create_folder():
    pass

@app.post("/sharefile")
def share_file():
    pass

@app.put("/sharepermissions")
def share_permissions():
    pass
@app.get("/fileverison")
def file_verison():
    pass

@app.post("/revertFileVersion")
def revert_file_version():
    pass

@app.get("/searchfile")
def search_file():
    pass

