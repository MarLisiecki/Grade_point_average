import pandas as pd  ##Use pandas against csv library



class Operation():
    # Open file with pandas
    @staticmethod
    def open_file(name_of_file):
        data_frame = pd.read_csv(name_of_file, encoding='ISO8859-2', sep="delimiter", engine='python')
        content = data_frame.values.tolist()
        return content


    # Loops for extract data from csv to tables #
    @staticmethod
    def extract_data(content, choice, sum_of_grades, sum_of_points, semester, grades, points, index):
        for i in range(0, len(content)):
            semester.append(content[i][0].split(';')[0])
        for i in range(0, len(content)):
            grades.append(content[i][0].split(';')[7])
        for i in range(0, len(content)):
            points.append(content[i][0].split(';')[9])
        for i in range(0, len(content)):
            if (content[i][0].split(';')[0] == choice[0] or content[i][0].split(';')[0] == choice[1]):
                index.append(i)
        for i in range(0, len(grades)):
            if (grades[i].find('(E)')):
                grades[i] = grades[i].replace(' (E)', (''))
            if (grades[i].find(',')):
                grades[i] = grades[i].replace(',', ('.'))
        for i in index:
            sum_of_grades += float(grades[i]) * int(points[i])
            sum_of_points += int(points[i]) * 1
        return sum_of_grades, sum_of_points


    # Average calc
    @staticmethod
    def calculate_average(tuple_with_grades_and_points):
        average = tuple_with_grades_and_points[0] / tuple_with_grades_and_points[1]
        return round(average, 3)
