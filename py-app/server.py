from fastapi import FastAPI


app = FastAPI()


@app.get("/python/")
def read_index():
    return {'fastapi': 'world'}


@app.get("/python/extended/")
def read_index():
    return {'fastapi': 'extended'}
