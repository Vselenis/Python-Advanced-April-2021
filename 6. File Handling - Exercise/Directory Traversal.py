import os


def extract_files(dir):
    return [el for el in dir if "." in el]

def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        name, extention = file.split(".")
        if extention not in report:
            report[extention] = []
        report[extention].append(name)
    return report

dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_files_extensions(files)

for extention, names in sorted(report_info.items(), key=lambda x: x[0]):
    print(f".{extention}")
    print(*[f"- - - {name}.{extention}" for name in names], sep='\n')