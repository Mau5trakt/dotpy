use ex01
db.libros.insertMany(
    [    
        {
        "título":"Química",
        "Autor":"Raymond Chang",
        "Edicion":"12va",
        "Categoría":"Química",
        "registro": 2,
        "cantidad": 5,
        "en prestamo": 0,
        "disponibles": 5    
        },
        {
        "título":"Química",
        "Autor":"Raymond Chang",
        "Edicion":"11va",
        "Categoría":"Química",
        "registro": 3,
        "cantidad": 3,
        "en prestamo": 0,
        "disponibles": 3   
        },
        {
            "título":"Introducción a La Termodinámica en Ingeniería Química",
        "Autor":"H. C. Van Ness",
        "Edicion":"7ma",
        "Categoría":"Termodinámica",
        "registro": 4,
        "cantidad": 4,
        "en prestamo": 0,
        "disponibles": 4   
        },
        {
            "título":"Termodinámica",
        "Autor":"Yunus A. Cengel",
        "Edicion":"8va",
        "Categoría":"Termodinámica",
        "registro": 5,
        "cantidad": 4,
        "en prestamo": 0,
        "disponibles": 4   
        },
        {
            "título":"Transferencia de Calor y Masa",
        "Autor":"Yunus A. Cengel",
        "Edicion":"4ta",
        "Categoría":"Termodinámica",
        "registro": 6,
        "cantidad": 3,
        "en prestamo": 0,
        "disponibles": 3   
        },
        {
            "título":"Fenómenos de Transporte",
        "Autor":"R. Bird",
        "Edicion":"2da",
        "Categoría":"Transferencia de Calor y Masa",
        "registro": 7,
        "cantidad": 4,
        "en prestamo": 0,
        "disponibles": 4   
        },
        {
            "título":"Fundamentos de Física",
        "Autor":"Raymond A. Serway",
        "Edicion":"10ma",
        "Categoría":"Física",
        "registro": 8,
        "cantidad": 7,
        "en prestamo": 0,
        "disponibles": 7   
        },
        {
            "título":"Cálculo, Trascendentes Tempranas",
        "Autor":"Dennis G. Zill",
        "Edicion":"4ta",
        "Categoría":"Cálculo Diferencial",
        "registro": 9,
        "cantidad": 10,
        "en prestamo": 0,
        "disponibles": 10   
        }
           ]
)
db.libros.find({})