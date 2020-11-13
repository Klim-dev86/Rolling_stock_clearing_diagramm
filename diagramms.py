import input_data as data


class Point:

    def __init__(self, type_of_diagram, number, height, width, upper_or_lower, main_or_additional):
        self.type = type_of_diagram
        self.number = number
        self.height = height
        self.width = width
        self.upper_or_lower = upper_or_lower
        self.main_or_additional = main_or_additional

    def __str__(self):
        return f"Тип диаграммы: {self.type}, Номер точки: {self.number}, Высота: {self.height} мм," \
               f" Ширина {self.width} мм, {self.upper_or_lower}, {self.main_or_additional}"


def construct_array_of_points():
    array_of_point_objects = []
    _diagram = choose_diagram(data.diagram_type,
                              data.diagram_sub_type,
                              data.equipment_arrangement,
                              data.track_gauge)

    for point in _diagram:
        array_of_point_objects.append(Point(type_of_diagram=point[0],
                                            number=point[1],
                                            height=point[2],
                                            width=point[3],
                                            upper_or_lower=point[4],
                                            main_or_additional=point[5]))

    return array_of_point_objects


def choose_diagram(diagram_type, diagram_sub_type, equipment_arrangement, track_gauge):

    spring_type = ''
    _diagram = ()

    if equipment_arrangement == 'carriage_body':
        spring_type = 'spring'
    elif equipment_arrangement in ('bogie_frame', 'bolster'):
        spring_type = 'bogie_spring'
    elif equipment_arrangement in ('wheel', 'axel_box'):
        spring_type = 'no_spring'

    if data.diagram_type in ('T', 'Tz', 'Tpr', '1-T'):
        _diagram = diagrams[diagram_type][diagram_sub_type][spring_type]

    elif data.diagram_type in ('0-VM', '1-VM', '02-VM', '03-VM'):
        _diagram = diagrams[diagram_type][diagram_sub_type][spring_type][track_gauge]

    return _diagram


diagrams = {
    'T': {
        'clear': {
            'spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  340,  1875, 'lower', 'main'),
                ('T', 11,  340,  1440, 'lower', 'main'),
                ('T', 12,  270,  1380, 'lower', 'main'),
                ('T', 13,  100,  1380, 'lower', 'main'),
                ('T', 14,  100, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,  100, 718.5, 'lower', 'main'),
                ('T', 18,  100,     0, 'lower', 'main'),
            ),
            'bogie_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  310,  1875, 'lower', 'main'),
                ('T', 11,  310,  1440, 'lower', 'main'),
                ('T', 12,  250,  1380, 'lower', 'main'),
                ('T', 13,   80,  1380, 'lower', 'main'),
                ('T', 14,   80, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,   80, 718.5, 'lower', 'main'),
                ('T', 18,   80,     0, 'lower', 'main'),
            ),
            'no_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  295,  1875, 'lower', 'main'),
                ('T', 11,  295,  1440, 'lower', 'main'),
                ('T', 12,  235,  1380, 'lower', 'main'),
                ('T', 13,   65,  1380, 'lower', 'main'),
                ('T', 14,   65, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,   65, 718.5, 'lower', 'main'),
                ('T', 18,   65,     0, 'lower', 'main'),
            )

        },
        'turned_off_retarder': {
            'spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  340,  1875, 'lower', 'main'),
                ('T', 11,  340,  1440, 'lower', 'main'),
                ('T', 12,  270,  1380, 'lower', 'main'),
                ('T', 13,  100,  1380, 'lower', 'main'),
                ('T', 14,  100,   985, 'lower', 'main'),
                ('T', 15,  125,   939, 'lower', 'main'),
                ('T', 16,  125, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  125, 718.5, 'lower', 'main'),
                ('T', 20,  125,   625, 'lower', 'main'),
                ('T', 21,  100,   605, 'lower', 'main'),
                ('T', 22,   90,   115, 'lower', 'additional'),
                ('T', 23,   90,   115, 'lower', 'additional'),
                ('T', 24,  100,     0, 'lower', 'main')
            ),
            'bogie_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  310,  1875, 'lower', 'main'),
                ('T', 11,  310,  1440, 'lower', 'main'),
                ('T', 12,  250,  1380, 'lower', 'main'),
                ('T', 13,   80,  1380, 'lower', 'main'),
                ('T', 14,   80,   985, 'lower', 'main'),
                ('T', 15,  115,   939, 'lower', 'main'),
                ('T', 16,  115, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  115, 718.5, 'lower', 'main'),
                ('T', 20,  115,   625, 'lower', 'main'),
                ('T', 21,   80,   605, 'lower', 'main'),
                ('T', 22,   85,   115, 'lower', 'additional'),
                ('T', 23,   85,   115, 'lower', 'additional'),
                ('T', 24,   80,    0, 'lower', 'main')
            ),
            'no_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  295,  1875, 'lower', 'main'),
                ('T', 11,  295,  1440, 'lower', 'main'),
                ('T', 12,  235,  1380, 'lower', 'main'),
                ('T', 13,   65,  1380, 'lower', 'main'),
                ('T', 14,   65,   985, 'lower', 'main'),
                ('T', 15,  110,   939, 'lower', 'main'),
                ('T', 16,  110, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  105, 718.5, 'lower', 'main'),
                ('T', 20,  105,   625, 'lower', 'main'),
                ('T', 21,   65,   605, 'lower', 'main'),
                ('T', 22,   80,   115, 'lower', 'additional'),
                ('T', 23,   80,   115, 'lower', 'additional'),
                ('T', 24,   65,     0, 'lower', 'main')
            )

        },
        'turned_on_retarder': {
            'spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  340,  1875, 'lower', 'main'),
                ('T', 11,  340,  1440, 'lower', 'main'),
                ('T', 12,  270,  1380, 'lower', 'main'),
                ('T', 13,  105,  1380, 'lower', 'main'),
                ('T', 14,  105,   960, 'lower', 'main'),
                ('T', 15,  110,   960, 'lower', 'main'),
                ('T', 16,  110,   910, 'lower', 'main'),
                ('T', 17,  130,   910, 'lower', 'main'),
                ('T', 18,  130, 871.5, 'lower', 'main'),
                ('T', 19,    0, 871.5, 'lower', 'main'),
                ('T', 20,    0, 718.5, 'lower', 'main'),
                ('T', 21,  140, 718.5, 'lower', 'main'),
                ('T', 22,  140,   540, 'lower', 'main'),
                ('T', 23,  115,   540, 'lower', 'main'),
                ('T', 24,  115,   115, 'lower', 'main'),
                ('T', 25,  100,   115, 'lower', 'main'),
                ('T', 26,  100,     0, 'lower', 'main')
            ),
            'bogie_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  310,  1875, 'lower', 'main'),
                ('T', 11,  310,  1440, 'lower', 'main'),
                ('T', 12,  250,  1380, 'lower', 'main'),
                ('T', 13,   95,  1380, 'lower', 'main'),
                ('T', 14,   95,   960, 'lower', 'main'),
                ('T', 15,  100,   960, 'lower', 'main'),
                ('T', 16,  100,   910, 'lower', 'main'),
                ('T', 17,  120,   910, 'lower', 'main'),
                ('T', 18,  120, 871.5, 'lower', 'main'),
                ('T', 19,    0, 871.5, 'lower', 'main'),
                ('T', 20,    0, 718.5, 'lower', 'main'),
                ('T', 21,  130, 718.5, 'lower', 'main'),
                ('T', 22,  130,   540, 'lower', 'main'),
                ('T', 23,  105,   540, 'lower', 'main'),
                ('T', 24,  105,   115, 'lower', 'main'),
                ('T', 25,   90,   115, 'lower', 'main'),
                ('T', 26,   90,     0, 'lower', 'main')
            ),
            'no_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  295,  1875, 'lower', 'main'),
                ('T', 11,  295,  1440, 'lower', 'main'),
                ('T', 12,  235,  1380, 'lower', 'main'),
                ('T', 13,   90,  1380, 'lower', 'main'),
                ('T', 14,   90,   960, 'lower', 'main'),
                ('T', 15,  110,   960, 'lower', 'main'),
                ('T', 16,  110,   910, 'lower', 'main'),
                ('T', 17,  115,   910, 'lower', 'main'),
                ('T', 18,  115, 871.5, 'lower', 'main'),
                ('T', 19,    0, 871.5, 'lower', 'main'),
                ('T', 20,    0, 718.5, 'lower', 'main'),
                ('T', 21,  125, 718.5, 'lower', 'main'),
                ('T', 22,  125,   540, 'lower', 'main'),
                ('T', 23,  100,   540, 'lower', 'main'),
                ('T', 24,  100,   115, 'lower', 'main'),
                ('T', 25,   85,   115, 'lower', 'main'),
                ('T', 26,   85,     0, 'lower', 'main')
            )
        },
        'gravity_yard': {
            'spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  340,  1875, 'lower', 'main'),
                ('T', 11,  340,  1440, 'lower', 'main'),
                ('T', 12,  270,  1380, 'lower', 'main'),
                ('T', 13,  115,  1380, 'lower', 'main'),
                ('T', 14,  115,   960, 'lower', 'main'),
                ('T', 15,  130,   960, 'lower', 'main'),
                ('T', 16,  130, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  140, 718.5, 'lower', 'main'),
                ('T', 20,  140,   540, 'lower', 'main'),
                ('T', 21,  115,   540, 'lower', 'main'),
                ('T', 22,  115,   115, 'lower', 'main'),
                ('T', 23,  100,   115, 'lower', 'main'),
                ('T', 24,  100,     0, 'lower', 'main'),
            ),
            'bogie_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  310,  1875, 'lower', 'main'),
                ('T', 11,  310,  1440, 'lower', 'main'),
                ('T', 12,  250,  1380, 'lower', 'main'),
                ('T', 13,  105,  1380, 'lower', 'main'),
                ('T', 14,  105,   960, 'lower', 'main'),
                ('T', 15,  120,   960, 'lower', 'main'),
                ('T', 16,  120, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  130, 718.5, 'lower', 'main'),
                ('T', 20,  130,   540, 'lower', 'main'),
                ('T', 21,  105,   540, 'lower', 'main'),
                ('T', 22,  105,   115, 'lower', 'main'),
                ('T', 23,   90,   115, 'lower', 'main'),
                ('T', 24,   90,     0, 'lower', 'main'),
            ),
            'no_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,   700, 'upper', 'main'),
                ('T',  2, 4500,  1400, 'upper', 'main'),
                ('T',  3, 4250,  1600, 'upper', 'main'),
                ('T',  4, 3850,  1875, 'upper', 'main'),
                ('T',  5, 3850,  1925, 'upper', 'additional'),
                ('T',  6, 2600,  1875, 'upper', 'main'),
                ('T',  7, 2600,  1925, 'upper', 'additional'),
                ('T',  8, 1370,  1875, 'upper', 'main'),
                ('T',  9, 1370,  1975, 'upper', 'additional'),
                ('T', 10,  295,  1875, 'lower', 'main'),
                ('T', 11,  295,  1440, 'lower', 'main'),
                ('T', 12,  235,  1380, 'lower', 'main'),
                ('T', 13,  100,  1380, 'lower', 'main'),
                ('T', 14,  100,   960, 'lower', 'main'),
                ('T', 15,  115,   960, 'lower', 'main'),
                ('T', 16,  115, 871.5, 'lower', 'main'),
                ('T', 17,    0, 871.5, 'lower', 'main'),
                ('T', 18,    0, 718.5, 'lower', 'main'),
                ('T', 19,  125, 718.5, 'lower', 'main'),
                ('T', 20,  125,   540, 'lower', 'main'),
                ('T', 21,  100,   540, 'lower', 'main'),
                ('T', 22,  100,   115, 'lower', 'main'),
                ('T', 23,   85,   115, 'lower', 'main'),
                ('T', 24,   85,     0, 'lower', 'main'),
            )
        }
    },  # Done
    'Tz': {
        'clear': {
            'spring': (
                ('Tz', 0, 5200,     0, 'upper', 'main'),
                ('Tz', 1, 5200,  1010, 'upper', 'main'),
                ('Tz', 2, 5000,  1235, 'upper', 'main'),
                ('Tz', 3, 4750,  1425, 'upper', 'main'),
                ('Tz', 4, 4320,  1690, 'upper', 'main'),
                ('Tz', 5, 4050,  1825, 'upper', 'main'),
                ('Tz', 6, 3000,  1875, 'upper', 'main'),
                ('Tz', 7, 2900,  1875, 'upper', 'main'),
                ('Tz', 8, 2000,  1725, 'upper', 'main'),
                ('Tz', 9, 1270,  1700, 'upper', 'main'),
                ('Tz', 10, 340,  1700, 'lower', 'main'),
                ('Tz', 11, 340,  1440, 'lower', 'main'),
                ('Tz', 12, 270,  1380, 'lower', 'main'),
                ('Tz', 13, 100,  1380, 'lower', 'main'),
                ('Tz', 14, 100, 871.5, 'lower', 'main'),
                ('Tz', 15,   0, 871.5, 'lower', 'main'),
                ('Tz', 16,   0, 718.5, 'lower', 'main'),
                ('Tz', 17, 100, 718.5, 'lower', 'main'),
                ('Tz', 18, 100,     0, 'lower', 'main'),
            ),
            'bogie_spring': (
                ('Tz', 0, 5200,     0, 'upper', 'main'),
                ('Tz', 1, 5200,  1010, 'upper', 'main'),
                ('Tz', 2, 5000,  1235, 'upper', 'main'),
                ('Tz', 3, 4750,  1425, 'upper', 'main'),
                ('Tz', 4, 4320,  1690, 'upper', 'main'),
                ('Tz', 5, 4050,  1825, 'upper', 'main'),
                ('Tz', 6, 3000,  1875, 'upper', 'main'),
                ('Tz', 7, 2900,  1875, 'upper', 'main'),
                ('Tz', 8, 2000,  1725, 'upper', 'main'),
                ('Tz', 9, 1270,  1700, 'upper', 'main'),
                ('Tz', 10, 310,  1700, 'lower', 'main'),
                ('Tz', 11, 310,  1440, 'lower', 'main'),
                ('Tz', 12, 250,  1380, 'lower', 'main'),
                ('Tz', 13,  80,  1380, 'lower', 'main'),
                ('Tz', 14,  80, 871.5, 'lower', 'main'),
                ('Tz', 15,   0, 871.5, 'lower', 'main'),
                ('Tz', 16,   0, 718.5, 'lower', 'main'),
                ('Tz', 17,  80, 718.5, 'lower', 'main'),
                ('Tz', 18,  80,     0, 'lower', 'main'),
            ),
            'no_spring': (
                ('Tz', 0, 5200,     0, 'upper', 'main'),
                ('Tz', 1, 5200,  1010, 'upper', 'main'),
                ('Tz', 2, 5000,  1235, 'upper', 'main'),
                ('Tz', 3, 4750,  1425, 'upper', 'main'),
                ('Tz', 4, 4320,  1690, 'upper', 'main'),
                ('Tz', 5, 4050,  1825, 'upper', 'main'),
                ('Tz', 6, 3000,  1875, 'upper', 'main'),
                ('Tz', 7, 2900,  1875, 'upper', 'main'),
                ('Tz', 8, 2000,  1725, 'upper', 'main'),
                ('Tz', 9, 1270,  1700, 'upper', 'main'),
                ('Tz', 10, 295,  1700, 'lower', 'main'),
                ('Tz', 11, 295,  1440, 'lower', 'main'),
                ('Tz', 12, 235,  1380, 'lower', 'main'),
                ('Tz', 13,  65,  1380, 'lower', 'main'),
                ('Tz', 14,  65, 871.5, 'lower', 'main'),
                ('Tz', 15,   0, 871.5, 'lower', 'main'),
                ('Tz', 16,   0, 718.5, 'lower', 'main'),
                ('Tz', 17,  65, 718.5, 'lower', 'main'),
                ('Tz', 18,  65,     0, 'lower', 'main'),
            )
        },
        'turned_off_retarder': {
            'spring': (
                ('Tz',  0, 5200,     0, 'upper', 'main'),
                ('Tz',  1, 5200,  1010, 'upper', 'main'),
                ('Tz',  2, 5000,  1235, 'upper', 'main'),
                ('Tz',  3, 4750,  1425, 'upper', 'main'),
                ('Tz',  4, 4320,  1690, 'upper', 'main'),
                ('Tz',  5, 4050,  1825, 'upper', 'main'),
                ('Tz',  6, 3000,  1875, 'upper', 'main'),
                ('Tz',  7, 2900,  1875, 'upper', 'main'),
                ('Tz',  8, 2000,  1725, 'upper', 'main'),
                ('Tz',  9, 1270,  1700, 'upper', 'main'),
                ('Tz', 10,  340,  1700, 'lower', 'main'),
                ('Tz', 11,  340,  1440, 'lower', 'main'),
                ('Tz', 12,  270,  1380, 'lower', 'main'),
                ('Tz', 13,  100,  1380, 'lower', 'main'),
                ('Tz', 14,  100,   985, 'lower', 'main'),
                ('Tz', 15,  125,   939, 'lower', 'main'),
                ('Tz', 16,  125, 871.5, 'lower', 'main'),
                ('Tz', 17,    0, 871.5, 'lower', 'main'),
                ('Tz', 18,    0, 718.5, 'lower', 'main'),
                ('Tz', 19,  125, 718.5, 'lower', 'main'),
                ('Tz', 20,  125,   625, 'lower', 'main'),
                ('Tz', 21,  100,   605, 'lower', 'main'),
                ('Tz', 22,   90,   115, 'lower', 'additional'),
                ('Tz', 23,   90,   115, 'lower', 'additional'),
                ('Tz', 24,  100,     0, 'lower', 'main')
            ),
            'bogie_spring': (
                ('Tz',  0, 5200,     0, 'upper', 'main'),
                ('Tz',  1, 5200,  1010, 'upper', 'main'),
                ('Tz',  2, 5000,  1235, 'upper', 'main'),
                ('Tz',  3, 4750,  1425, 'upper', 'main'),
                ('Tz',  4, 4320,  1690, 'upper', 'main'),
                ('Tz',  5, 4050,  1825, 'upper', 'main'),
                ('Tz',  6, 3000,  1875, 'upper', 'main'),
                ('Tz',  7, 2900,  1875, 'upper', 'main'),
                ('Tz',  8, 2000,  1725, 'upper', 'main'),
                ('Tz',  9, 1270,  1700, 'upper', 'main'),
                ('Tz', 10,  310,  1700, 'lower', 'main'),
                ('Tz', 11,  310,  1440, 'lower', 'main'),
                ('Tz', 12,  250,  1380, 'lower', 'main'),
                ('Tz', 13,   80,  1380, 'lower', 'main'),
                ('Tz', 14,   80,   985, 'lower', 'main'),
                ('Tz', 15,  115,   939, 'lower', 'main'),
                ('Tz', 16,  115, 871.5, 'lower', 'main'),
                ('Tz', 17,    0, 871.5, 'lower', 'main'),
                ('Tz', 18,    0, 718.5, 'lower', 'main'),
                ('Tz', 19,  115, 718.5, 'lower', 'main'),
                ('Tz', 20,  115,   625, 'lower', 'main'),
                ('Tz', 21,   80,   605, 'lower', 'main'),
                ('Tz', 22,   85,   115, 'lower', 'additional'),
                ('Tz', 23,   85,   115, 'lower', 'additional'),
                ('Tz', 24,   80,     0, 'lower', 'main')
            ),
            'no_spring': "TODO"  # TODO
        },
        'turned_on_retarder': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'gravity_yard': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        }
    },
    'Tpr': {
        'clear': {
            'spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,  1200, 'upper', 'main'),
                ('T',  2, 4500,  1775, 'upper', 'main'),
                ('T',  3, 4350,  1775, 'upper', 'main'),
                ('T',  4, 4000,  1775, 'upper', 'main'),
                ('T',  5, 1270,  1775, 'upper', 'main'),
                ('T',  6, 1270,  1700, 'upper', 'main'),
                ('T', 10,  340,  1700, 'lower', 'main'),
                ('T', 11,  340,  1440, 'lower', 'main'),
                ('T', 12,  270,  1380, 'lower', 'main'),
                ('T', 13,  100,  1380, 'lower', 'main'),
                ('T', 14,  100, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,  100, 718.5, 'lower', 'main'),
                ('T', 18,  100,     0, 'lower', 'main'),
            ),
            'bogie_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,  1200, 'upper', 'main'),
                ('T',  2, 4500,  1775, 'upper', 'main'),
                ('T',  3, 4350,  1775, 'upper', 'main'),
                ('T',  4, 4000,  1775, 'upper', 'main'),
                ('T',  5, 1270,  1775, 'upper', 'main'),
                ('T',  6, 1270,  1700, 'upper', 'main'),
                ('T', 10,  310,  1700, 'lower', 'main'),
                ('T', 11,  310,  1440, 'lower', 'main'),
                ('T', 12,  250,  1380, 'lower', 'main'),
                ('T', 13,   80,  1380, 'lower', 'main'),
                ('T', 14,   80, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,   80, 718.5, 'lower', 'main'),
                ('T', 18,   80,     0, 'lower', 'main'),
            ),
            'no_spring': (
                ('T',  0, 5300,     0, 'upper', 'main'),
                ('T',  1, 5300,  1200, 'upper', 'main'),
                ('T',  2, 4500,  1775, 'upper', 'main'),
                ('T',  3, 4350,  1775, 'upper', 'main'),
                ('T',  4, 4000,  1775, 'upper', 'main'),
                ('T',  5, 1270,  1775, 'upper', 'main'),
                ('T',  6, 1270,  1700, 'upper', 'main'),
                ('T', 10,  295,  1700, 'lower', 'main'),
                ('T', 11,  295,  1440, 'lower', 'main'),
                ('T', 12,  235,  1380, 'lower', 'main'),
                ('T', 13,   65,  1380, 'lower', 'main'),
                ('T', 14,   65, 871.5, 'lower', 'main'),
                ('T', 15,    0, 871.5, 'lower', 'main'),
                ('T', 16,    0, 718.5, 'lower', 'main'),
                ('T', 17,   65, 718.5, 'lower', 'main'),
                ('T', 18,   65,     0, 'lower', 'main'),
            )
        },
        'turned_off_retarder': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'turned_on_retarder': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'gravity_yard': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        }
    },
    '1-T': {
        'clear': {
            'spring': (
                ('1-T', 0, 5300, 0, 'upper', 'main'),
                ('1-T', 1, 5300, 700, 'upper', 'main'),
                ('1-T', 2, 4500, 1400, 'upper', 'main'),
                ('1-T', 3, 4250, 1600, 'upper', 'main'),
                ('1-T', 4, 4000, 1700, 'upper', 'main'),
                ('1-T', 5, 4000, 1750, 'upper', 'additional'),
                ('1-T', 6, 2600, 1700, 'upper', 'main'),
                ('1-T', 7, 2600, 1750, 'upper', 'additional'),
                ('1-T', 8, 1270, 1700, 'upper', 'main'),
                ('1-T', 9, 1270, 1800, 'upper', 'additional'),
                ('1-T', 10, 340, 1700, 'lower', 'main'),
                ('1-T', 11, 340, 1440, 'lower', 'main'),
                ('1-T', 12, 270, 1380, 'lower', 'main'),
                ('1-T', 13, 100, 1380, 'lower', 'main'),
                ('1-T', 14, 100, 871.5, 'lower', 'main'),
                ('1-T', 15, 0, 871.5, 'lower', 'main'),
                ('1-T', 16, 0, 718.5, 'lower', 'main'),
                ('1-T', 17, 100, 718.5, 'lower', 'main'),
                ('1-T', 18, 100, 0, 'lower', 'main'),
            ),
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'turned_off_retarder': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'turned_on_retarder': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        },
        'gravity_yard': {
            'spring': "TODO",  # TODO
            'bogie_spring': "TODO",  # TODO
            'no_spring': "TODO"  # TODO
        }
    },
    '0-VM': {
        'clear': {
            'spring': {
                1520: (
                    ('T', 0, 4650,     0, 'upper', 'main'),
                    ('T', 1, 4650,   720, 'upper', 'main'),
                    ('T', 2, 4200,  1130, 'upper', 'main'),
                    ('T', 3, 3800,  1460, 'upper', 'main'),
                    ('T', 4, 3500,  1625, 'upper', 'main'),
                    ('T', 5, 3100,  1625, 'upper', 'main'),
                    ('T', 6, 3100,  1675, 'upper', 'additional'),
                    ('T', 7, 2600,  1675, 'upper', 'additional'),
                    ('T', 8, 2600,  1625, 'upper', 'main'),
                    ('T', 9, 1160,  1650, 'upper', 'additional'),
                    ('T', 10, 1160, 1625, 'upper', 'main'),
                    ('T', 11, 430,  1625, 'lower', 'main'),
                    ('T', 12, 430,  1520, 'lower', 'main'),
                    ('T', 13, 100,  1190, 'lower', 'main'),
                    ('T', 14, 100, 871.5, 'lower', 'main'),
                    ('T', 15,   0, 871.5, 'lower', 'main'),
                    ('T', 16,   0, 718.5, 'lower', 'main'),
                    ('T', 17, 100, 718.5, 'lower', 'main'),
                    ('T', 18, 100,     0, 'lower', 'main')
                    ),
                1435: (
                    ('T', 0, 4650,     0, 'upper', 'main'),
                    ('T', 1, 4650,   720, 'upper', 'main'),
                    ('T', 2, 4200,  1130, 'upper', 'main'),
                    ('T', 3, 3800,  1460, 'upper', 'main'),
                    ('T', 4, 3500,  1625, 'upper', 'main'),
                    ('T', 5, 3100,  1625, 'upper', 'main'),
                    ('T', 6, 3100,  1675, 'upper', 'additional'),
                    ('T', 7, 2600,  1675, 'upper', 'additional'),
                    ('T', 8, 2600,  1625, 'upper', 'main'),
                    ('T', 9, 1160,  1650, 'upper', 'additional'),
                    ('T', 10, 1160, 1625, 'upper', 'main'),
                    ('T', 11, 430,  1625, 'lower', 'main'),
                    ('T', 12, 430,  1520, 'lower', 'main'),
                    ('T', 13, 100,  1190, 'lower', 'main'),
                    ('T', 14, 100, 831.5, 'lower', 'main'),
                    ('T', 15,   0, 821.5, 'lower', 'main'),
                    ('T', 16,   0, 678.5, 'lower', 'main'),
                    ('T', 17, 100, 678.5, 'lower', 'main'),
                    ('T', 18, 100,     0, 'lower', 'main')
                    )
            },
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_off_retarder': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder_osjt': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'gravity_yard': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        }
    },
    '1-VM': {
        'clear': {
            'spring': {
                1520: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 350, 1675, 'lower', 'main'),
                    ('T', 12, 350, 1520, 'lower', 'main'),
                    ('T', 13, 100, 1190, 'lower', 'main'),
                    ('T', 14, 100, 871, 5, 'lower', 'main'),
                    ('T', 15, 0, 871.5, 'lower', 'main'),
                    ('T', 16, 0, 718.5, 'lower', 'main'),
                    ('T', 17, 100, 718.5, 'lower', 'main'),
                    ('T', 18, 100, 0, 'lower', 'main')
                    ),
                1435: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 430, 1675, 'lower', 'main'),
                    ('T', 12, 430, 1520, 'lower', 'main'),
                    ('T', 13, 100, 1190, 'lower', 'main'),
                    ('T', 14, 100, 831, 5, 'lower', 'main'),
                    ('T', 15, 0, 831.5, 'lower', 'main'),
                    ('T', 16, 0, 678.5, 'lower', 'main'),
                    ('T', 17, 100, 678.5, 'lower', 'main'),
                    ('T', 18, 100, 0, 'lower', 'main')
                    )
            },
            'bogie_spring': {
                1520: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 330, 1675, 'lower', 'main'),
                    ('T', 12, 330, 1520, 'lower', 'main'),
                    ('T', 13, 80, 1190, 'lower', 'main'),
                    ('T', 14, 80, 871, 5, 'lower', 'main'),
                    ('T', 15, 0, 871.5, 'lower', 'main'),
                    ('T', 16, 0, 718.5, 'lower', 'main'),
                    ('T', 17, 80, 718.5, 'lower', 'main'),
                    ('T', 18, 80, 0, 'lower', 'main')
                    ),
                1435: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 410, 1675, 'lower', 'main'),
                    ('T', 12, 410, 1520, 'lower', 'main'),
                    ('T', 13, 80, 1190, 'lower', 'main'),
                    ('T', 14, 80, 831, 5, 'lower', 'main'),
                    ('T', 15, 0, 831.5, 'lower', 'main'),
                    ('T', 16, 0, 678.5, 'lower', 'main'),
                    ('T', 17, 80, 678.5, 'lower', 'main'),
                    ('T', 18, 80, 0, 'lower', 'main')
                    )
            },
            'no_spring': {
                1520: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 315, 1675, 'lower', 'main'),
                    ('T', 12, 315, 1520, 'lower', 'main'),
                    ('T', 13, 65, 1190, 'lower', 'main'),
                    ('T', 14, 65, 871, 5, 'lower', 'main'),
                    ('T', 15, 0, 871.5, 'lower', 'main'),
                    ('T', 16, 0, 718.5, 'lower', 'main'),
                    ('T', 17, 65, 718.5, 'lower', 'main'),
                    ('T', 18, 65, 0, 'lower', 'main')
                    ),
                1435: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 395, 1675, 'lower', 'main'),
                    ('T', 12, 395, 1520, 'lower', 'main'),
                    ('T', 13, 65, 1190, 'lower', 'main'),
                    ('T', 14, 65, 831, 5, 'lower', 'main'),
                    ('T', 15, 0, 831.5, 'lower', 'main'),
                    ('T', 16, 0, 678.5, 'lower', 'main'),
                    ('T', 17, 65, 678.5, 'lower', 'main'),
                    ('T', 18, 65, 0, 'lower', 'main')
                    )
            },
        },
        'turned_off_retarder': {
            'spring': {
                1520: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 430, 1675, 'lower', 'main'),
                    ('T', 12, 430, 1520, 'lower', 'main'),
                    ('T', 13, 100, 1190, 'lower', 'main'),
                    ('T', 14, 100, 985, 'lower', 'main'),
                    ('T', 15, 100, 985, 'lower', 'additional'),
                    ('T', 16, 115, 871.5, 'lower', 'main'),
                    ('T', 17, 0, 871.5, 'lower', 'main'),
                    ('T', 18, 0, 718.5, 'lower', 'main'),
                    ('T', 19, 75, 718.5, 'lower', 'main'),
                    ('T', 20, 100, 718.5, 'lower', 'main'),
                    ('T', 21, 70, 625, 'lower', 'additional'),
                    ('T', 22, 65, 625, 'lower', 'additional'),
                    ('T', 23, 65, 115, 'lower', 'additional'),
                    ('T', 24, 90, 115, 'lower', 'additional'),
                    ('T', 25, 100, 0, 'lower', 'main')
                    ),
                1435: (
                    ('T', 0, 4700, 0, 'upper', 'main'),
                    ('T', 1, 4700, 1160, 'upper', 'main'),
                    ('T', 2, 4500, 1400, 'upper', 'main'),
                    ('T', 3, 4250, 1600, 'upper', 'main'),
                    ('T', 4, 3850, 1700, 'upper', 'main'),
                    ('T', 5, 3100, 1700, 'upper', 'additional'),
                    ('T', 6, 3100, 1750, 'upper', 'main'),
                    ('T', 7, 2600, 1750, 'upper', 'additional'),
                    ('T', 8, 2600, 1700, 'upper', 'main'),
                    ('T', 9, 1160, 1700, 'upper', 'additional'),
                    ('T', 10, 1160, 1675, 'lower', 'main'),
                    ('T', 11, 430, 1675, 'lower', 'main'),
                    ('T', 12, 430, 1520, 'lower', 'main'),
                    ('T', 13, 100, 1190, 'lower', 'main'),
                    ('T', 14, 100, 985, 'lower', 'main'),
                    ('T', 15, 100, 985, 'lower', 'additional'),
                    ('T', 16, 115, 831.5, 'lower', 'main'),
                    ('T', 17, 0, 831.5, 'lower', 'main'),
                    ('T', 18, 0, 678.5, 'lower', 'main'),
                    ('T', 19, 75, 678.5, 'lower', 'main'),
                    ('T', 20, 100, 678.5, 'lower', 'main'),
                    ('T', 21, 70, 625, 'lower', 'additional'),
                    ('T', 22, 65, 625, 'lower', 'additional'),
                    ('T', 23, 65, 115, 'lower', 'additional'),
                    ('T', 24, 90, 115, 'lower', 'additional'),
                    ('T', 25, 100, 0, 'lower', 'main')
                    )
            },
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder_osjt': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'gravity_yard': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        }
    },
    '02-VM': {
        'clear': {
            'spring': {
                1520: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  430,  1575, 'upper', 'main'),
                    ('02-VM', 12,  430,  1520, 'lower', 'main'),
                    ('02-VM', 13,  100,  1190, 'lower', 'main'),
                    ('02-VM', 14,  100, 871.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 871.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 718.5, 'lower', 'main'),
                    ('02-VM', 17,  100, 718.5, 'lower', 'main'),
                    ('02-VM', 18,  100,     0, 'lower', 'main')
                    ),
                1435: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  430,  1575, 'upper', 'main'),
                    ('02-VM', 12,  430,  1520, 'lower', 'main'),
                    ('02-VM', 13,  100,  1190, 'lower', 'main'),
                    ('02-VM', 14,  100, 831.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 831.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 678.5, 'lower', 'main'),
                    ('02-VM', 17,  100, 678.5, 'lower', 'main'),
                    ('02-VM', 18,  100,     0, 'lower', 'main')
                    )
            },
            'bogie_spring': {
                1520: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  410,  1575, 'upper', 'main'),
                    ('02-VM', 12,  410,  1520, 'lower', 'main'),
                    ('02-VM', 13,   80,  1190, 'lower', 'main'),
                    ('02-VM', 14,   80, 871.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 871.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 718.5, 'lower', 'main'),
                    ('02-VM', 17,   80, 718.5, 'lower', 'main'),
                    ('02-VM', 18,   80,     0, 'lower', 'main')
                    ),
                1435: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  410,  1575, 'upper', 'main'),
                    ('02-VM', 12,  410,  1520, 'lower', 'main'),
                    ('02-VM', 13,   80,  1190, 'lower', 'main'),
                    ('02-VM', 14,   80, 831.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 831.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 678.5, 'lower', 'main'),
                    ('02-VM', 17,   80, 678.5, 'lower', 'main'),
                    ('02-VM', 18,   80,     0, 'lower', 'main')
                    )
            },
            'no_spring': {
                1520: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  395,  1575, 'upper', 'main'),
                    ('02-VM', 12,  395,  1520, 'lower', 'main'),
                    ('02-VM', 13,   65,  1190, 'lower', 'main'),
                    ('02-VM', 14,   65, 871.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 871.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 718.5, 'lower', 'main'),
                    ('02-VM', 17,   65, 718.5, 'lower', 'main'),
                    ('02-VM', 18,   65,     0, 'lower', 'main')
                    ),
                1435: (
                    ('02-VM',  0, 4650,     0, 'upper', 'main'),
                    ('02-VM',  1, 4650,   690, 'upper', 'main'),
                    ('02-VM',  2, 3805,  1395, 'upper', 'main'),
                    ('02-VM',  3, 3500,  1575, 'upper', 'main'),
                    ('02-VM',  4, 3100,  1575, 'upper', 'main'),
                    ('02-VM',  5, 3100,  1625, 'upper', 'additional'),
                    ('02-VM',  6, 2600,  1672, 'upper', 'additional'),
                    ('02-VM',  7, 2600,  1575, 'upper', 'main'),
                    ('02-VM',  8,  395,  1575, 'upper', 'main'),
                    ('02-VM', 12,  395,  1520, 'lower', 'main'),
                    ('02-VM', 13,   65,  1190, 'lower', 'main'),
                    ('02-VM', 14,   65, 831.5, 'lower', 'main'),
                    ('02-VM', 15,    0, 831.5, 'lower', 'main'),
                    ('02-VM', 16,    0, 678.5, 'lower', 'main'),
                    ('02-VM', 17,   65, 678.5, 'lower', 'main'),
                    ('02-VM', 18,   65,     0, 'lower', 'main')
                    )
            },
        },
        'turned_off_retarder': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'turned_on_retarder_osjt': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        },
        'gravity_yard': {
            'spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'bogie_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
            'no_spring': {
                1520: "TODO",  # TODO
                1435: "TODO"  # TODO
            },  # TODO,
        }
    },
    '03-VM': {
        'clear': {
            'spring': {
                1520: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 430, 1575, 'lower', 'main'),
                    ('03-VM', 6, 430, 1520, 'lower', 'main'),
                    ('03-VM', 7, 335, 1440, 'lower', 'main'),
                    ('03-VM', 8, 335, 1430, 'lower', 'main'),
                    ('03-VM', 9, 145, 1250, 'lower', 'main'),
                    ('03-VM', 10, 115, 1175, 'lower', 'main'),
                    ('03-VM', 11, 100, 1050, 'lower', 'main'),
                    ('03-VM', 12, 100, 871.5, 'lower', 'main'),
                    ('03-VM', 13, 0, 871.5, 'lower', 'main'),
                    ('03-VM', 14, 0, 718.5, 'lower', 'main'),
                    ('03-VM', 15, 100, 718.5, 'lower', 'main'),
                    ('03-VM', 16, 100, 0, 'lower', 'main')
                    ),
                1435: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 430, 1575, 'lower', 'main'),
                    ('03-VM', 6, 430, 1520, 'lower', 'main'),
                    ('03-VM', 7, 335, 1440, 'lower', 'main'),
                    ('03-VM', 8, 335, 1430, 'lower', 'main'),
                    ('03-VM', 9, 145, 1250, 'lower', 'main'),
                    ('03-VM', 10, 115, 1175, 'lower', 'main'),
                    ('03-VM', 11, 100, 1050, 'lower', 'main'),
                    ('03-VM', 12, 100, 831.5, 'lower', 'main'),
                    ('03-VM', 13, 0, 831.5, 'lower', 'main'),
                    ('03-VM', 14, 0, 678.5, 'lower', 'main'),
                    ('03-VM', 15, 100, 678.5, 'lower', 'main'),
                    ('03-VM', 16, 100, 0, 'lower', 'main')
                    )

            },  # TODO,
            'bogie_spring': {
                1520: (
                ('03-VM', 0, 4280, 0, 'upper', 'main'),
                ('03-VM', 1, 4280, 440, 'upper', 'main'),
                ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                ('03-VM', 5, 410, 1575, 'lower', 'main'),
                ('03-VM', 6, 410, 1520, 'lower', 'main'),
                ('03-VM', 7, 315, 1440, 'lower', 'main'),
                ('03-VM', 8, 315, 1430, 'lower', 'main'),
                ('03-VM', 9, 125, 1250, 'lower', 'main'),
                ('03-VM', 10, 95, 1175, 'lower', 'main'),
                ('03-VM', 11, 80, 1050, 'lower', 'main'),
                ('03-VM', 12, 80, 871.5, 'lower', 'main'),
                ('03-VM', 13, 0, 871.5, 'lower', 'main'),
                ('03-VM', 14, 0, 718.5, 'lower', 'main'),
                ('03-VM', 15, 80, 718.5, 'lower', 'main'),
                ('03-VM', 16, 80, 0, 'lower', 'main')
                ),
                1435: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 410, 1575, 'lower', 'main'),
                    ('03-VM', 6, 410, 1520, 'lower', 'main'),
                    ('03-VM', 7, 315, 1440, 'lower', 'main'),
                    ('03-VM', 8, 315, 1430, 'lower', 'main'),
                    ('03-VM', 9, 125, 1250, 'lower', 'main'),
                    ('03-VM', 10, 95, 1175, 'lower', 'main'),
                    ('03-VM', 11, 80, 1050, 'lower', 'main'),
                    ('03-VM', 12, 80, 831.5, 'lower', 'main'),
                    ('03-VM', 13, 0, 831.5, 'lower', 'main'),
                    ('03-VM', 14, 0, 678.5, 'lower', 'main'),
                    ('03-VM', 15, 80, 678.5, 'lower', 'main'),
                    ('03-VM', 16, 80, 0, 'lower', 'main')
                    )

            },
            'no_spring': {
                1520: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 395, 1575, 'lower', 'main'),
                    ('03-VM', 6, 395, 1520, 'lower', 'main'),
                    ('03-VM', 7, 300, 1440, 'lower', 'main'),
                    ('03-VM', 8, 300, 1430, 'lower', 'main'),
                    ('03-VM', 9, 110, 1250, 'lower', 'main'),
                    ('03-VM', 10, 80, 1175, 'lower', 'main'),
                    ('03-VM', 11, 65, 1050, 'lower', 'main'),
                    ('03-VM', 12, 65, 871.5, 'lower', 'main'),
                    ('03-VM', 13, 0, 871.5, 'lower', 'main'),
                    ('03-VM', 14, 0, 718.5, 'lower', 'main'),
                    ('03-VM', 15, 65, 718.5, 'lower', 'main'),
                    ('03-VM', 16, 65, 0, 'lower', 'main')
                    ),
                1435: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 395, 1575, 'lower', 'main'),
                    ('03-VM', 6, 395, 1520, 'lower', 'main'),
                    ('03-VM', 7, 300, 1440, 'lower', 'main'),
                    ('03-VM', 8, 300, 1430, 'lower', 'main'),
                    ('03-VM', 9, 110, 1250, 'lower', 'main'),
                    ('03-VM', 10, 80, 1175, 'lower', 'main'),
                    ('03-VM', 11, 65, 1050, 'lower', 'main'),
                    ('03-VM', 12, 65, 831.5, 'lower', 'main'),
                    ('03-VM', 13, 0, 831.5, 'lower', 'main'),
                    ('03-VM', 14, 0, 678.5, 'lower', 'main'),
                    ('03-VM', 15, 65, 678.5, 'lower', 'main'),
                    ('03-VM', 16, 65, 0, 'lower', 'main')
                    )

            },
        },

        'gravity_yard': {
            'spring': {
                1520: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 430, 1575, 'lower', 'main'),
                    ('03-VM', 6, 430, 1520, 'lower', 'main'),
                    ('03-VM', 7, 335, 1440, 'lower', 'main'),
                    ('03-VM', 8, 335, 1430, 'lower', 'main'),
                    ('03-VM', 9, 145, 1250, 'lower', 'main'),
                    ('03-VM', 10, 130, 1212, 'lower', 'main'),
                    ('03-VM', 11, 130, 871.5, 'lower', 'main'),
                    ('03-VM', 12, 0, 871.5, 'lower', 'main'),
                    ('03-VM', 16, 0, 718.5, 'lower', 'main'),
                    ('03-VM', 15, 140, 718.5, 'lower', 'main'),
                    ('03-VM', 17, 140, 0, 'lower', 'main')
                    ),
                1435: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 430, 1575, 'lower', 'main'),
                    ('03-VM', 6, 430, 1520, 'lower', 'main'),
                    ('03-VM', 7, 335, 1440, 'lower', 'main'),
                    ('03-VM', 8, 335, 1430, 'lower', 'main'),
                    ('03-VM', 9, 145, 1250, 'lower', 'main'),
                    ('03-VM', 10, 130, 1212, 'lower', 'main'),
                    ('03-VM', 11, 130, 831.5, 'lower', 'main'),
                    ('03-VM', 12, 0, 831.5, 'lower', 'main'),
                    ('03-VM', 16, 0, 678.5, 'lower', 'main'),
                    ('03-VM', 15, 140, 678.5, 'lower', 'main'),
                    ('03-VM', 17, 140, 0, 'lower', 'main')
                    )

            },
            'no_spring': {
                1520: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 415, 1575, 'lower', 'main'),
                    ('03-VM', 6, 415, 1520, 'lower', 'main'),
                    ('03-VM', 7, 320, 1440, 'lower', 'main'),
                    ('03-VM', 8, 320, 1430, 'lower', 'main'),
                    ('03-VM', 9, 130, 1250, 'lower', 'main'),
                    ('03-VM', 10, 115, 1212, 'lower', 'main'),
                    ('03-VM', 11, 115, 871.5, 'lower', 'main'),
                    ('03-VM', 12, 0, 871.5, 'lower', 'main'),
                    ('03-VM', 16, 0, 718.5, 'lower', 'main'),
                    ('03-VM', 15, 125, 718.5, 'lower', 'main'),
                    ('03-VM', 17, 125, 0, 'lower', 'main')
                    ),
                1435: (
                    ('03-VM', 0, 4280, 0, 'upper', 'main'),
                    ('03-VM', 1, 4280, 440, 'upper', 'main'),
                    ('03-VM', 2, 3980, 1040, 'upper', 'main'),
                    ('03-VM', 3, 3670, 1350, 'upper', 'main'),
                    ('03-VM', 4, 3220, 1575, 'upper', 'main'),
                    ('03-VM', 5, 415, 1575, 'lower', 'main'),
                    ('03-VM', 6, 415, 1520, 'lower', 'main'),
                    ('03-VM', 7, 320, 1440, 'lower', 'main'),
                    ('03-VM', 8, 320, 1430, 'lower', 'main'),
                    ('03-VM', 9, 130, 1250, 'lower', 'main'),
                    ('03-VM', 10, 115, 1212, 'lower', 'main'),
                    ('03-VM', 11, 115, 831.5, 'lower', 'main'),
                    ('03-VM', 12, 0, 831.5, 'lower', 'main'),
                    ('03-VM', 16, 0, 678.5, 'lower', 'main'),
                    ('03-VM', 15, 125, 678.5, 'lower', 'main'),
                    ('03-VM', 17, 125, 0, 'lower', 'main')
                    )
            }
        }
    }  # Done
}

diagram = construct_array_of_points()


if __name__ == "__main__":
    for point in diagram:
        print(str(point))
