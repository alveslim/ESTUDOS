courses =  []

with open("4-Manipulando_arquivos/4-courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)
        
def get_language(course): # A função de ordenação recebe um curso e
    # retorna a linguagem do curso, que é usada como chave para ordenar os cursos
    return course["language"]
        
for course in sorted(courses, key=get_language): # A função sorted() ordena os cursos usando a função get_language como chave de ordenação
    print(f"{course['language']} - {course['category']}")

#lambda   
"""
for course in sorted(courses, key=lambda course: course["language"]):

# A função lambda é uma função anônima que recebe um curso e retorna a
# linguagem do curso, usada como chave para ordenar os cursos

    print(f"{course['language']} - {course['category']}")
"""   
