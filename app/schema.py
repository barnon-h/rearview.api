from pydantic import BaseModel

class prediction_request( BaseModel ):
    year : int
    miles : int
    make : str
    model : str

class prediction_response( BaseModel ):
    predicted_price : float