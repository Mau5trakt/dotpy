from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://biblodb:5SdBM3SOGlK01NnK@cluster0.8oeno.mongodb.net/ex01?retryWrites=true&w=majority')

db = client['ex01']
col = db['corprueb']
n = 82333234
doc = col.find_one({
    '# telefónico': n
})
if doc is not None:
    print("No es nulo")
else:
    print("ayeye")
