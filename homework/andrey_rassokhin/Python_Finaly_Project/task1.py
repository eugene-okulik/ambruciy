import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='analyzer')
    parser.add_argument('path_to_logs', type=str, help='Path to logs')
    parser.add_argument('--text', type=str, help='What text to find')
    return parser.parse_args()


def search_in_file(path_to_logs, text):
    result = []
    logs_files = [
        os.path.join(path_to_logs, file) for file in os.listdir(path_to_logs) if file.endswith(".log")
    ]
    for file_path in logs_files:
        number_line = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                number_line += 1
                words = line.split()

                if text in words:
                    index = words.index(text)
                    part_of_text = ' '.join(words[max(index - 5, 0):index + 6])
                    result.append((os.path.basename(file_path), number_line, part_of_text))
    return result


args = parse_arguments()
search_result = search_in_file(args.path_to_logs, args.text)

if search_result:
    for file_path, number_line, part_of_text in search_result:
        print(f'Название файла: {file_path}\n'
              f'Cтрока в которой был найден текст: {number_line}\n'
              f'Фрагмент найденного текста: {part_of_text}')
else:
    print('Ничего не найдено')
