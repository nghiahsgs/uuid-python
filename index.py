import uuid

#print(uuid.uuid1()) should not use because of it contain your network
print(uuid.uuid4())
print(uuid.uuid4().hex)