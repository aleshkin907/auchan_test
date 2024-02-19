import glob
import re

TEST_FOLDER_MASK = "TEST_Folder_*"
TEST_FILE_MASK = "TEST_AUCHAN_*"
RESULT_FOLDER_MASK = "Result"
RESULT_FILE_MASK = "TEST_AUCHAN_success_"


class NumberParser:
    @staticmethod
    def parse_ranges(input_str):
        input_str = input_str.replace('"', '').replace("'", "")
        elements = [x.strip() for x in input_str.split(',')]
        result = []

        for element in elements:
            if '-' in element:
                start, end = element.split('-')
                width = len(start) if start[0] == '0' else 0
                start_num = int(start)
                end_num = int(end)
                result.extend(str(num).zfill(width) for num in range(start_num, end_num + 1))
            else:
                result.append(element.strip())

        return result


class FileProcessor:
    @staticmethod
    def write_numbers(file_path, numbers):
        with open(file_path, 'w') as file:
            file.write('\n'.join(numbers))


def main():
    test_folders = glob.glob(TEST_FOLDER_MASK)

    for folder in test_folders:
        auchan_files = glob.glob(f'{folder}/{TEST_FILE_MASK}')

        for file_path in auchan_files:
            with open(file_path, 'r') as file:
                content = file.read().strip()
                numbers = NumberParser.parse_ranges(content)
                file_id = re.search(r'\d+', file_path.split("/")[-1]).group()

                target_file_path = f'{RESULT_FOLDER_MASK}/{RESULT_FILE_MASK}{file_id}'
                FileProcessor.write_numbers(target_file_path, numbers)


if __name__ == "__main__":
    main()
