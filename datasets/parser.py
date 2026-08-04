import json

from shapely import wkt


def read_json(json_path):

    with open(json_path, "r") as file:

        data = json.load(file)

    return data


def get_metadata(data):

    return data["metadata"]


def get_image_name(data):

    return data["metadata"]["img_name"]

def get_buildings(data):

    return data["features"]["xy"]




def parse_buildings(data):

    buildings = []

    for building in data["features"]["xy"]:

        properties = building["properties"]

        polygon = wkt.loads(building["wkt"])

        xmin, ymin, xmax, ymax = polygon.bounds

        buildings.append({

            "uid": properties["uid"],

            "damage": properties.get("subtype", None),

            "polygon": polygon,

            "bounds": (xmin, ymin, xmax, ymax),

            "area": polygon.area

        })

    return buildings