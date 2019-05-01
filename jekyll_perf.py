def add_file(id, base_dir):
    file_name = base_dir + "risk." + str(id) + ".md"
    with open(file_name, "a") as f:
        f.write('---\n')
        f.write('id: risk.' + str(id) + '\n')
        f.write('title: "Risk.' + str(id) + ': License managing initialization failure"\n')
        f.write('toc: true\n---\n\n')
        f.write('# Risk.' + str(id) + ': License managing initialization failure\n\n')
        f.write(
            '## Error Cause\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n## Error Resolution\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n## Occurs in Version\n7.2.1')


def insert_in_toc(id, base_dir):
    toc_name = base_dir + 'navigation.yml'
    with open(toc_name, "a") as toc:
        toc.write('      - title: "Risk.' + str(id) + '"\n')
        toc.write('        url: /_pages/risk.' + str(id) + '/' + '\n')


def main():
    base_dir = r'D:/ioana/python_perf_test/'
    for i in range(1, 1000):
        add_file(i, base_dir)
        insert_in_toc(i, base_dir)


main()
