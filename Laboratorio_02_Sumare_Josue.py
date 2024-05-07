# Verificar si una es substring de otra.
def is_substring(first_string, second_string):
    # 1. Implementar un algoritmo que reciba dos cadenas e indique si una de ellas es substring de la otra.
    return (first_string in second_string) or (second_string in first_string)


# 2. Calcular el score de dos cadenas teniendo en consideración, si son iguales valor de +1 y si son diferentes -2.
def calculate_score(first_string, second_string):

    # Similitud entre cadenas
    score = 0
    size_1, size_2 = len(first_string), len(second_string)
    size = min(size_1, size_2)
    for i in range(size):
        if first_string[i] == second_string[i]:
            score += 1
        else:
            score -= 2
    score -= 2 * (size_1 - size_2) if (size_1 >= size_2) else 2 * (size_2 - size_1)
    return score


# 3. Implementar el alineamiento global. Los datos de salida deben ser guardados en un .txt, en donde se tendrá: (i)el
# score final, (ii)la matriz de scores, (iii)la cantidad de alineamiento producidos y (iv)los alineamientos generados.


def global_alignment(string1, string2,filename):
    score_matrix = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        score_matrix[i][0] = i * -2
    for j in range(len(string2) + 1):
        score_matrix[0][j] = j * -2

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            match = 1 if string1[i - 1] == string2[j - 1] else -2
            score_matrix[i][j] = max(score_matrix[i - 1][j - 1] + match,
                                     score_matrix[i - 1][j] - 2,
                                     score_matrix[i][j - 1] - 2)

    final_score = score_matrix[-1][-1]

    alignments = []
    alignment = ""
    i, j = len(string1), len(string2)

    while i > 0 or j > 0:
        if i > 0 and j > 0 and string1[i - 1] == string2[j - 1]:
            alignment = string1[i - 1] + alignment
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] - 2:
            alignment = string1[i - 1] + alignment
            i -= 1
        elif j > 0 and score_matrix[i][j] == score_matrix[i][j - 1] - 2:
            alignment = " " + alignment
            j -= 1
        else:
            break

    alignments.append(alignment)

    with open(filename, "w") as file:
        file.write(f"Score final: {final_score}\n\n")
        file.write("Matriz de scores:\n")
        for row in score_matrix:
            file.write(" ".join(map(str, row)) + "\n")
        file.write("\nCantidad de alineamientos producidos: {}\n\n".format(len(alignments)))
        file.write("Alineamientos generados:\n")
        for alignment in alignments:
            file.write(alignment + "\n")

# 1ra parte
#10 bacteria
#10 influenza
bacteria="tcaagcgtta"
influenza="atggaagcaa"

global_alignment(bacteria, influenza,"test_1.txt")

#2da parte
# 10 sarscov
# 10 influenza
sarscov="attaaaggtt"
influenza="atggaagcaa"

global_alignment(sarscov, influenza,"test_2.txt")


# 3ra parte:
# 30 sarscov
# 30 bacteria
sarscov="attaaaggtttataccttcccaggtaacaa"
bacteria="tcaagcgttagagaagtcattatgtgataa"
for i in range(len(sarscov)): 
    global_alignment(sarscov, bacteria,"test_3.txt")

# 4ta parte
# 60 bacteria
# 30 influenaza
bacteria="tcaagcgttagagaagtcattatgtgataaaaaaattcaacttggtatcaacttaactaa"
influenza="atggaagcaatatcactgatgactatacta"
global_alignment(bacteria, influenza,"test_4.txt")

# 5ta 
# 60 influenza
# 120 sarscov
influenza="atggaagcaatatcactgatgactatactactggtggtaacaacaagtaatgcagacaaa"
sarscov="attaaaggtttataccttcccaggtaacaaaccaaccaactttcgatctcttgtagatctgttctctaaacgaactttaaaatctgtgtggctgtcactcggctgcatgcttagtgcact"
global_alignment(bacteria, influenza,"test_5.txt")

# 5ta 
# 120 sarscov
# 240 influenza
sarscov="attaaaggtttataccttcccaggtaacaaaccaaccaactttcgatctcttgtagatctgttctctaaacgaactttaaaatctgtgtggctgtcactcggctgcatgcttagtgcact"
influenza="atggaagcaatatcactgatgactatactactggtggtaacaacaagtaatgcagacaaaatctgcatcggtcaccaatcaacaaattccacggaaactgtagacacgctaacagaaacaaatgttcctgtaacacaagccaaagaattgctccacacagaacacaatgggatgctatgtgcaacaaatctgggacgtcctcttatcctagacacatgcaccattgaaggactgatctat"
global_alignment(bacteria, influenza,"test_6.txt")