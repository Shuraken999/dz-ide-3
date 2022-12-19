with open('1.txt', encoding='utf-8') as f1, open('2.txt', encoding='utf-8') as f2, open('3.txt', encoding='utf-8') as f3:
    file1 = f1.readlines()
    file2 = f2.readlines()
    file3 = f3.readlines()
    if len(file1) < len(file2) < len(file3):
        with open('4.txt', 'wt', encoding='utf-8') as w:
            w.writelines([''.join(file1), ''.join(file2), f'\n{"".join(file3)}'])
    elif len(file1) < len(file3) < len(file2):
        with open('4.txt', 'wt', encoding='utf-8') as w:
            w.writelines([''.join(file1), f'\n{"".join(file3)}', ''.join(file2)])
    elif len(file2) < len(file1) < len(file3):
        with open('4.txt', 'wt', encoding='utf-8') as w:
            w.writelines([''.join(file2), ''.join(file1), f'\n{"".join(file3)}'])
    elif len(file3) < len(file2) < len(file1):
        with open('4.txt', 'wt', encoding='utf-8') as w:
            w.writelines([f'\n{"".join(file3)}', ''.join(file2), ''.join(file1)])
f1.close()
f2.close()
f3.close()