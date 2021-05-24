from pymongo import MongoClient

client = MongoClient('mongodb+srv://usuarios:RgvAZFpFu9LYm5RF@cluster0.8oeno.mongodb.net/ex01?retryWrites=true&w=majority')

db = client['ex01']
col = db['corprueb']
#print(client.list_database_names()) ver todas mis bases de datos
#print(db.list_collection_names()) ver todas las colecciones
for documento in col.find({'# telefónico':8233323}):   #Query de consulta de mi base de datos
    a = documento
    print(a)
