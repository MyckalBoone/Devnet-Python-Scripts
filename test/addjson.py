import json
import json_sample

json_dict["interface"]["description"] = "Backup Link"

with open("config.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)
