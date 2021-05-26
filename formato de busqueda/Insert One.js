use ex01
db.libros.find({})
db.libros.insertOne({
    "título":"Química Cuántica",
        "Autor":"Ira N. Levine",
        "Edicion":"6ta",
        "Categoría":"Química",
        "registro": 1,
        "cantidad": 3,
        "en prestamo": 0,
        "disponibles": 3   
})