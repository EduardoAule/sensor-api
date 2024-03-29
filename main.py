import uvicorn
from fastapi import FastAPI, Response
from models import ModelName
from controller import controller as con

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Sensor API Ready!"}

# Recibe un int
@app.get("/sensors/{ds_id}")
async def read_sensors(ds_id: str):
	if ds_id == "ds_1":
		temp = con.Controller.read_DS18B20()
		return {"temperature": temp[0], "tempF": temp[1]}
	return {"sensor": "404 - not sensor found!"}


# Para Prometheus se requiere del endpoint /metrics
@app.get("/metrics")
async def read_sensors():
	temp = con.Controller.read_DS18B20()
	# Response - When you return a Response directly its data is not validated,
	# converted (serialized), nor documented automatically.
	if temp is not None:
		return Response('# HELP local_temp local temperature\n# TYPE local_temp gauge\nlocal_temp {}\n# HELP local_tempfahrenheit local fahrenheit\n# TYPE local_fahrenheit gauge\nlocal_tempfahrenheit {}\n'.format(float(temp[0]), float(temp[1])), 200, {'Content-Type': 'text/plain; charset=utf-8'} )
	else:
		return 'Could not read from DS.', 200, {'Content-Type': 'text/plain; charset=utf-8'}
	#return {"temperature": temp}

#  http://127.0.0.1:8000/sensor/foo
# item_id es str
#@app.get("/sensor/{item_id}")
#async def read_temp(item_id):
#    return {"item_id": item_id}

# Recibe un int
@app.get("/sensors/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName.ModelName):
	if model_name == ModelName.ModelName.alexnet:
		return {"model_name": model_name, "message": "Deep Learning FTW!"}

	if model_name.value == "lenet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}

# Query Parameters
# http://127.0.0.1:8000/items/?skip=0&limit=10
# above as the same http://127.0.0.1:8000/items/
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Required query parameters
# When you declare a default value for non-path parameters then it is not required.
# If you don't want to add a specific value but just make it optional, set the default as None
@app.get("/users/{item_id}")
async def read_user_item(item_id: str, needy: str):
	item = {"item_id": item_id, "needy": needy}
	return item