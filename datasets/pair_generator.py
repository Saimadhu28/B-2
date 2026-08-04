from datasets.parser import parse_buildings


def create_pairs(pre_json, post_json):

    pre_buildings = parse_buildings(pre_json)
    post_buildings = parse_buildings(post_json)

    pre_dict = {}

    for b in pre_buildings:
        pre_dict[b["uid"]] = b

    pairs = []

    for post in post_buildings:

        uid = post["uid"]

        if uid in pre_dict:

            pair = {
                "uid": uid,
                "pre": pre_dict[uid],
                "post": post,
                "label": post["damage"]
            }

            pairs.append(pair)

    return pairs