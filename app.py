from fastapi import FastAPI,HTTPException
from products import Product
app=FastAPI()
test = {
    1: ["post", "context", "updated post"],
    2: ["delete the post", "past was deleted"],
    3: ["create user", "user registered successfully"],
    4: ["update user", "user details updated"],
    5: ["get user", "user details fetched"],
    6: ["login", "user logged in"],
    7: ["logout", "user logged out"],
    8: ["upload file", "file uploaded successfully"],
    9: ["download file", "file downloaded"],
    10: ["reset password", "password reset successful"]
}
products=[
    Product(id=1,Name="laptop",price=999,quantitiy=10)
]
@app.get('/hello')
def hello():
    return {"message":"Hello World"}
@app.get("/world")
def world():
    return {"msg":"hello how are you are you fine"}
@app.get("/input/{id}")
def input(id:int=None):
    if id not in test:
        raise HTTPException(status_code=404,detail="the poast was not found")
    return test.get(id)
@app.get("/multiple")
def multiple(list1:int=None):
    if list1 and list1>len(test):
        raise HTTPException(status_code=404,detail="file not found")
    if list1 and list1<=len(test):
        line=list(test.values())
        return line[:list1]
    return test
@app.get("/product/{id}")
def product(id:int):
    if id not in test:
        raise HTTPException(status_code=404,detail="This is an error")
    return test[id]
