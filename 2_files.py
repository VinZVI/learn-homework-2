"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file_input:
        sum_words = 0
        with open('referat2.txt', 'w', encoding='utf-8') as file_output:
            for line in file_input:
                line_list = line.split()
                sum_words += len(line_list)
                file_output.write(line.replace(".", '!'))
        print(sum_words)
if __name__ == "__main__":
    main()
