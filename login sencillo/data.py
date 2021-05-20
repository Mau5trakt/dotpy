from pymongo import MongoClient

client = MongoClient('localhost')
db = client['prueba']

col = db['personas']

col.insert_one({
    'edad': 21,
    'nombre': 'Mickey',
    'apeliido': 'Thompson',
    'intereses': 'Ser basado'
})

print(db.list_collection_names()) #Mostrar todos los datos de la colección

for documento in col.find({}):
    print(documento)