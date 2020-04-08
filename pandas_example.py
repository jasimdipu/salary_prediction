__parsed_rows = []


def parsed_csv():
    import csv
    __file_path = 'Desktop/data_science/baltimore-city-employee-salaries-fy2019-1.csv'
    __index = {
        'NAME': 0,
        'JOBTITLE': 1,
        'DEPTID': 2,
        'DESCR': 3,
        'HIRE_DT': 4,
        'ANNUAL_RT': 5,
        'Gross': 6,
    }

    global __parsed_rows
    with open(__file_path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            __parsed_rows.append({
                'NAME': row[__index['NAME']],
                'JOBTITLE': row[__index['JOBTITLE']],
                'DEPTID': row[__index['DEPTID']],
                'DESCR': row[__index['DESCR']],
                'HIRE_DT': row[__index['HIRE_DT']],
                'ANNUAL_RT': row[__index['ANNUAL_RT']],
                'Gross': row[__index['Gross']],
            })


def getNameMaxSalary():
    max_salary_emp = 0.0

    for row in __parsed_rows:
        if int(row['Gross']) > max_salary_emp:
            max_salary_emp = int(row['Gross'])
    return max_salary_emp


print(getNameMaxSalary())
