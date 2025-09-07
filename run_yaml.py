import yaml

# with open("test.yaml") as f:
#     data = yaml.safe_load(f)
#     print(data)


# import yaml

# with open("nested.yml") as f:
#     data = yaml.safe_load(f)

# for member in data['project']['team']:
#     print(f"{member['name']} - {member['role']}")
#     print("Skills:", ", ".join(member['skills']))
#     print("---")


# import yaml

# with open("multi_docs.yaml") as f:
#     for doc in yaml.safe_load_all(f):
#         print(doc)


# import yaml

# with open("aliases.yaml") as f:
#     data = yaml.safe_load(f)

# print(data)


with open("merge.yaml") as f:
    data = yaml.safe_load(f)
    print(data)
