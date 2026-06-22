from pydantic import BaseModel


class CancerPredictIn(BaseModel):
    radius_mean: int
    texture_mean: int