import yaml

with open("yaml_sample.yaml") as data:
    yaml_sample = data.read()
yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)
print(yaml_dict)
