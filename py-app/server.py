from fastapi import FastAPI


app = FastAPI()


@app.get("/python/")
def read_index():
    return {'fastapi': 'world'}
