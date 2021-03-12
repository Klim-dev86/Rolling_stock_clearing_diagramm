import input_data as data
import diagrams


#####################################
# Расчет горизонтальных ограничений #
#####################################

# Ссылки на ГОСТ 9238-2013, если не указано иное

def get_d_coeff():
    """Определение минимального расстояния между наружными гранями гребней предельно изношенных колесных пар, d, мм"""
    # Ж.25.3 а)
    d = None

    if data.track_gauge == 1520:
        d_apostrophe = 1437
        d = d_apostrophe + 2 * data.t
    elif data.track_gauge == 1435:
        d_apostrophe = 1358
        d = d_apostrophe + 2 * data.t
    return d


def get_k_k1_k2_k3_coeff(upper_or_lower_point):
    """Определение коэффициентов к, к1, к2, к3"""
    # Ж.25.3 а) Таблица Ж.1
    k = k1 = k2 = k3 = None

    if data.diagram_type in ['T', 'Tz', 'Tpr', '1-T']:
        k = 0
        k1 = 0.625 * data.p ** 2
        k2 = 2.5
        k3 = 180

    elif data.diagram_type == '1-VM':
        k1 = 0.625 * data.p
        k2 = 2.5
        k3 = 180
        if upper_or_lower_point == 'upper':
            k = 0
        elif upper_or_lower_point == 'lower':
            k = 25

    elif data.diagram_type == '0-VM':
        k1 = 0.625 * data.p ** 2
        k2 = 2.5
        k3 = 180
        if upper_or_lower_point == 'upper':
            k = 75
        elif upper_or_lower_point == 'lower':
            k = 25

    elif data.diagram_type in ['02-VM', '03-VM']:
        k1 = 0.5 * data.p ** 2
        k2 = 2
        k3 = 0
        if upper_or_lower_point == 'upper':
            k = 75
        elif upper_or_lower_point == 'lower':
            k = 25

    return k, k1, k2, k3


def get_S(upper_or_lower_point):
    """Определение ширины колеи S, мм"""
    # Ж.25.3 а)
    S = None

    if data.diagram_type in ['T', 'Tz', 'Tpr', '1-T']:
        S = 1530
    elif data.diagram_type == '1-VM' and upper_or_lower_point == 'upper':
        S = 1530
    elif data.diagram_type == '1-VM' and upper_or_lower_point == 'lower':
        S = 1465
    elif data.diagram_type in ['0-VM', '02-VM', '03-VM']:
        S = 1465

    return S


def get_alfa_betta_coeff(point_number, upper_or_lower_point):
    """Определение дополнительных ограничений подвижного состава с длиной более 24 м
     и базой более 17 м - альфа и бетта"""
    alfa = betta = None

    if data.R == 150:

        if data.diagram_type in ['T', 'Tc', 'Tpr', '1-T']:

            alfa = betta = 0.833 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 72)

        elif data.diagram_type == '1-VM' and upper_or_lower_point == 'upper':

            alfa = betta = 0.833 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 72)

        else:

            alfa = 1.333 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 100)
            betta = 1.333 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 120)

    elif data.R == 80:

        alfa = betta = 3.75 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 72)

    elif data.R == 40:

        alfa = betta = 10 * (data.l * data.n - data.n ** 2 + 0.25 * data.p ** 2 - 72)

    if alfa <= 0:
        alfa = 0

    if betta <= 0:
        betta = 0

    return alfa, betta


def get_horizontal_restrictions_1(upper_or_lower_point, point_number):
    """Определение ограничений E, мм, для:
    - верхних очертаний любого габарита;
    - нижних очертаний по рисункам 5, 15 и 20;
    - нижних очертаний по рисункам 17, 18, 19 до точки 13 включительно;
    - нижних очертаний по рисункам 20 и 21 до точки 10 включительно."""

    k, k1, k2, k3 = get_k_k1_k2_k3_coeff(upper_or_lower_point)
    S = get_S(upper_or_lower_point)
    d = get_d_coeff()
    q = data.q_apostrophe + data.q_double_apostrophe
    w = data.w_apostrophe + data.w_double_apostrophe

    if data.equipment_arrangement == 'wheel':
        E = 0.5 * (S - d) + data.delta_q - k

    elif data.equipment_arrangement == 'axel_box':
        E = 0.5 * (S - d) + data.q_apostrophe + data.delta_q - k

    elif data.equipment_arrangement == 'bogie_frame':

        if data.n_position == 'zero':

            delta_k_apostrophe = k1 - k3

            if delta_k_apostrophe <= 0:
                delta_k_apostrophe = 0

            E = 0.5 * (S - d) + q + data.delta_q + delta_k_apostrophe - k

        if data.n_position == 'inner':

            delta_k_apostrophe = k2 * (data.p - data.n) * data.n - k3
            if delta_k_apostrophe <= 0:
                delta_k_apostrophe = 0

            E = 0.5 * (S - d + 2) + q + data.delta_q + delta_k_apostrophe - k

        elif data.n_position == 'outer':

            delta_k_apostrophe = k2 * (data.p + data.n) * data.n - k3
            if delta_k_apostrophe <= 0:
                delta_k_apostrophe = 0

            fi_apostrophe = (2 * data.n + data.p) / data.n

            E = (0.5 * (S - d) + q) * fi_apostrophe + data.delta_q + delta_k_apostrophe - k

    elif data.equipment_arrangement == 'bolster':

        delta_k_apostrophe = k2 * (data.p - data.n) * data.n - k3

        E = 0.5 * (S - d) + q + data.w_apostrophe + data.delta_q + delta_k_apostrophe - k

    elif data.equipment_arrangement == 'carriage_body':

        alfa, betta = get_alfa_betta_coeff(point_number, upper_or_lower_point)

        if data.n_position == 'zero':

            delta_k = k1 - k3
            if delta_k <= -8:
                delta_k = 0

            E = 0.5 * (S - d) + q + w + data.delta_q + delta_k - k

        elif data.n_position == 'inner':

            delta_k = k2 * (data.l - data.n) * data.n + k1 - k3
            if delta_k <= -8:
                delta_k = 0

            E = 0.5 * (S - d) + q + w + data.delta_q + delta_k - k + alfa

        elif data.n_position == 'outer':

            delta_k = k2 * (data.p + data.n) * data.n - k3

            fi = (2 * data.n + data.l) / data.n

            if delta_k <= 8 * fi:
                delta_k = 0

            E = (0.5 * (S - d) + q + w) * fi + data.delta_q + delta_k - k + betta

    if E <= 0:  # Значения принимаются в расчет только при их положительном значении
        E = 0

    return E


def get_horizontal_restrictions_2():
    """Определение ограничений E, мм, для нижних очертаний по рисункам:
     - 6 (11 "б" по ЦВ-4422-86) Т, Тпр, 1-Т, Тц нерабочие (отторможенные) замедлители,
     - 16 (15 "б" по ЦВ-4422-86) 1-ВМ, 0-ВМ, 02-ВМ нерабочие (отторможенные) замедлители
     для точек с номером 14 и более"""
    # Ж.25.4

    E = None

    if data.n_position == 'zero' or 'inner':
        E = 10 + data.q_apostrophe + data.q_double_apostrophe + 0.5 * (
                data.w_apostrophe + data.w_double_apostrophe) + data.delta_q

    if data.n_position == 'outer':
        fi = (2 * data.n + data.l) / data.n

        E = (10 + data.q_apostrophe + data.q_double_apostrophe + 0.5 * (
                data.w_apostrophe + data.w_double_apostrophe)) * fi + data.delta_q

    return E


def get_horizontal_restrictions_3():
    """Определение ограничений E, мм, для нижних очертаний по рисункам:
        - 7 (11 "в" по ЦВ-4422-86) Т, Тпр, 1-Т, Тц замедлители в любом положении для точек 14 и более,
        - 8 (11 "г" по ЦВ-4422-86) Т, Тпр, 1-Т, Тц с устройствами надвига вагонов для точек 14 и более,
        - 17 (15 "в" по ЦВ-4422-86) 1-ВМ, 0-ВМ, 02-ВМ замедлители в любом положении для точек 14 и более,
        - 19 (15 "д" по ЦВ-4422-86) 1-ВМ, 0-ВМ, 02-ВМ с устройствами надвига вагонов для точек 14 и более,
        - 18 (15 "г" по ЦВ-4422-86) 1-ВМ, 0-ВМ, 02-ВМ замедлители ОСЖТ в любом положении для точек 13а, 13б, 14 и более;
        - 21 (17 "б" по ЦВ-4422-86) 03-ВМ замедлители в любом положении для точек 11 и более"""
    # Ж.25.5

    E = None

    if data.n_position == 'zero' or 'inner':
        E = data.q_apostrophe + data.q_double_apostrophe + 0.5 * (
                data.w_apostrophe + data.w_double_apostrophe) + data.delta_q

    if data.n_position == 'outer':
        fi = (2 * data.n + data.l) / data.n

        E = (data.q_apostrophe + data.q_double_apostrophe + 0.5 * (
                data.w_apostrophe + data.w_double_apostrophe)) * fi + data.delta_q

    return E


def add_or_substract_E(point_width, upper_or_lower_point, point_number, E):
    """Добавление или вычитание вычисленного значения Е к полуширине габарита в зависимости от
    номера рассчитываемой точки по ЦВ-4422-86"""
    # paragraph 2.3.1 ЦВ-4422-86

    if upper_or_lower_point == 'upper':
        B = point_width - E

    if data.diagram_type in ['T', '1-T', 'Tpr', 'Tz', '1-VM', '0-VM', '02-VM'] and point_number in range(1, 14):
        B = point_width - E

    if data.diagram_type == '03-VM' and data.diagram_sub_type == 'clear' and point_number in range(1, 12):
        B = point_width - E

    if data.diagram_type == '03-VM' and data.diagram_sub_type == 'gravity_yard' and point_number in range(1, 11):
        B = point_width - E

    # paragraph 2.3.2
    if data.diagram_type in ['T', '1-T', 'Tpr',
                             'Tz'] and data.diagram_sub_type == 'turned_off_retarder' and point_number == 14:
        B = point_width + E

    # TODO

    # paragraph 2.3.3
    if data.diagram_type in ['T', '1-T', 'Tpr',
                             'Tz'] and data.diagram_sub_type == 'turned_on_retarder' and point_number in range(14,
                                                                                                               22):
        B = point_width + E

    if data.diagram_type in ['T', '1-T', 'Tpr',
                             'Tz'] and data.diagram_sub_type == 'turned_on_retarder' and point_number in range(22,
                                                                                                               26):
        B = point_width - E

    # paragraph 2.3.4
    if data.diagram_type in ['T', '1-T', 'Tpr',
                             'Tz'] and data.diagram_sub_type == 'gravity_yard' and point_number in range(14, 20):
        B = point_width + E

    if data.diagram_type in ['T', '1-T', 'Tpr',
                             'Tz'] and data.diagram_sub_type == 'gravity_yard' and point_number in range(20, 24):
        B = point_width - E

    # paragraph 2.3.5
    if data.diagram_type in ['1-VM', '0-VM',
                             '02-VM'] and data.diagram_sub_type == 'turned_off_retarder' and point_number in range(14,
                                                                                                                   20):
        B = point_width + E

    # TODO

    # paragraph 2.3.6
    if data.diagram_type in ['1-VM', '0-VM',
                             '02-VM'] and data.diagram_sub_type == 'turned_on_retarder' and point_number in range(14,
                                                                                                                  22):
        B = point_width + E

    if data.diagram_type in ['1-VM', '0-VM',
                             '02-VM'] and data.diagram_sub_type == 'turned_on_retarder' and point_number in range(22,
                                                                                                                  26):
        B = point_width - E

    # paragraph 2.3.7

    # TODO

    # paragraph 2.3.8

    if data.diagram_type in ['1-VM', '0-VM',
                             '02-VM'] and data.diagram_sub_type == 'gravity_yard' and point_number in range(14, 18):
        B = point_width + E

    if data.diagram_type in ['1-VM', '0-VM',
                             '02-VM'] and data.diagram_sub_type == 'gravity_yard' and point_number in range(18, 20):
        B = point_width - E

    pass
    return B


def get_horizontal_build_position(point_width, upper_or_lower_point, point_number):
    """Определение горизонтальной координаты B, мм, строительного очертания"""

    if upper_or_lower_point == 'upper':
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    if data.diagram_type in ['T', '1-T', 'Tpr', 'Tz', '1-VM', '0-VM', '02-VM', '03-VM'] \
            and data.diagram_sub_type == 'clear' \
            and upper_or_lower_point == 'lower':
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    if data.diagram_type in ['1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'turned_on_retarder' \
            and point_number in range(1, 14):
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    if data.diagram_type in ['1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'turned_on_retarder_osjt' \
            and point_number in range(1, 14):
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    if data.diagram_type in ['1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'gravity_yard' \
            and point_number in range(1, 14):
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    if data.diagram_type == '03-VM' \
            and data.diagram_sub_type == 'clear' \
            and point_number in range(1, 11):
        E = get_horizontal_restrictions_1(upper_or_lower_point, point_number)

    #########

    if data.diagram_type in ['T', '1-T', "Tpr", 'Tz', '1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'turned_off_retarder' \
            and point_number >= 14:
        E = get_horizontal_restrictions_2()

    #########

    if data.diagram_type in ['T', '1-T', "Tpr", 'Tz', '1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'turned_on_retarder' \
            and point_number >= 14:
        E = get_horizontal_restrictions_3()

    if data.diagram_type in ['T', '1-T', "Tpr", 'Tz', '1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'gravity_yard' \
            and point_number >= 14:
        E = get_horizontal_restrictions_3()

    if data.diagram_type in ['1-VM', '0-VM', '02-VM'] \
            and data.diagram_sub_type == 'turned_on_retarder_osjt' \
            and point_number > 13:
        E = get_horizontal_restrictions_3()

    if data.diagram_type == '03-VM' and data.diagram_sub_type == 'gravity_yard' \
            and point_number >= 11:
        E = get_horizontal_restrictions_3()

    # TODO add_or_substract_E(point_width, upper_or_lower_point, point_number, E)

    B = point_width - E

    if B < 0:
        B = 0

    return B


def get_horizontal_project_position(point_width, upper_or_lower_point, point_number):
    """Определение горизонтальной координаты проектного очертания"""

    B = get_horizontal_build_position(point_width, upper_or_lower_point, point_number)

    B_proj = B - data.e_x

    if B_proj < 0:
        B_proj = 0

    return B_proj


###################################
# Расчет вертикальных ограничений #
###################################

# Расчет понижений частей подвижного состава

def get_vert_wheel_restr():
    """ Определение понижения подвижного состава для колесных пар, h0, мм"""
    # Ж.26.1 а)
    h_0 = 0.5 * (data.D_max - data.D_min)
    return h_0


def get_vert_axel_box_restr():
    """ Определение понижения подвижного состава для букс, h1, мм"""
    # Ж.26.1 б)
    h_1 = get_vert_wheel_restr() + data.delta_h_1
    return h_1


def get_vert_bogie_frame_restr():
    """ Определение понижения подвижного состава для рамы тележки, h2, мм"""
    # Ж.26.1 в)
    f1 = data.P_p * data.lambda_1
    h_2 = get_vert_axel_box_restr() + data.delta_h_2 + data.f_01 + f1
    return h_2


def get_vert_bolster_restr():
    """ Определение понижения подвижного состава для надрессорной балки, h3, мм"""
    # Ж.26.1 г)
    f2 = data.P_p * data.lambda_2
    h_3 = get_vert_bogie_frame_restr() + data.delta_h_3 + data.f_02 + f2
    return h_3


def get_vert_carriage_body_restr():
    """ Определение понижения подвижного состава для кузова, h4, мм"""
    # Ж.26.1 д)
    h_4 = get_vert_bolster_restr() + data.delta_h_4 + (2 * data.z * data.n) / data.l
    return h_4


# Расчет вертикальных ограничений нижних частей подвижного состава, регулируемых в процессе эксплуатации
# Ж.26.1

def get_vert_bogie_frame_adjustable_parts_restr():
    """Определение понижения регулируемого оборудования, укрепленного на раме тележки, h2р, мм"""
    # Ж.26.1 е)

    f1 = data.P_p * data.lambda_1
    h_2_p = data.h_0_p + data.delta_h_1_p + data.delta_h_2_p + f1

    return h_2_p


def get_vert_carriage_body_adjustable_parts_restr():
    """Определение понижения регулируемого оборудования, укрепленного на кузове, h4р, мм"""
    # Ж.26.1 е)

    f2 = data.P_p * data.lambda_2
    h_2_p = get_vert_bogie_frame_adjustable_parts_restr()
    h_4_p = h_2_p + data.delta_h_3_p + data.delta_h_4_p + f2

    return h_4_p


# Определение понижений кузова и укрепленных на нем частей обусловленных вертикальной кривой горба сортировочных горок
# Ж.26.2

def get_vert_gravity_yard_restr():
    """Определение понижения кузова и укрепленного на неи оборудования, обусловленного вертикальной
    кривой горба сортировочных горок, hRb, мм
    """
    # Ж.26.2

    h_R_b = None

    if data.diagram_type in ['T', 'Tc', 'Tpr', '1-T']:

        if data.l <= 14:
            h_R_b = 2 * data.n * (data.l - data.n) + 0.5 * data.p ** 2
        else:
            h_R_b = 13.75 * data.l - 0.5 * (data.l - 2 * data.n) ** 2 - 94.5

    if data.diagram_type in ['0-VM', '1-VM', '02-VM', '03-VM']:

        if data.l <= 21.25:
            h_R_b = 2 * data.n * (data.l - data.n) + 0.5 * data.p ** 2
        else:
            if data.n > 0.5 * (data.l - 21.25):
                h_R_b = 21.25 * data.l - 0.5 * (data.l - 2 * data.n) ** 2
            else:
                h_R_b = 42.5 * data.n

    return h_R_b


# Определение понижений кузова и укрепленных на нем частей,
# обусловленных вертикальной кривой путей надвига и спускной части горок Ж.26.3

def get_vert_hump_track_restr():
    """Определение понижения кузова и укрепленного на неи оборудования, обусловленного вертикальной
    кривой путей надвига и спускной части горок, hRn, мм
    """

    h_R_n = None

    if data.diagram_type in ['T', 'Tc', 'Tpr', '1-T']:
        h_R_n = 30 * data.n

    elif data.diagram_type in ['0-VM', '1-VM', '02-VM', '03-VM']:
        if data.diagram_sub_type == 'gravity_yard_empty':
            h_R_n = 2 * (data.l + data.n) * data.n + 0.075 * (data.T * data.h_zt * data.lambda_3) / data.l - (
                    data.l + 2 * data.n) / data.l
        else:
            h_R_n = 2 * (data.l + data.n) * data.n + 0.075 * (data.Q * data.h_zt * data.lambda_3) / data.l - (
                    data.l + 2 * data.n) / data.l

    return h_R_n


# Определение высоты точек строительного очертания

def get_vertical_build_position(point_height, upper_or_lower_point):
    """ Определение наименьшей высоты точек строительного очертания, H, мм """
    H = None

    if upper_or_lower_point == 'upper':
        H = point_height

    elif upper_or_lower_point == 'lower':

        if data.equipment_arrangement == 'wheel':
            h_0 = get_vert_wheel_restr()
            H = point_height + h_0

        elif data.equipment_arrangement == 'axel_box':
            h_1 = get_vert_axel_box_restr()
            H = point_height + h_1

        elif data.equipment_arrangement == 'bogie_frame' and not data.adjustable:
            h_2 = get_vert_bogie_frame_restr()
            H = point_height + h_2

        elif data.equipment_arrangement == 'bogie_frame' and data.adjustable:
            h_2_p = get_vert_bogie_frame_adjustable_parts_restr()
            H = point_height + h_2_p

        elif data.equipment_arrangement == 'bolster':
            h_3 = get_vert_bolster_restr()
            H = point_height + h_3

        elif data.equipment_arrangement == 'carriage_body' and not data.adjustable:
            h_4 = get_vert_carriage_body_restr()
            H = point_height + h_4

            if data.diagram_sub_type == 'gravity_yard':
                if data.n_position == 'inner':
                    h_R_b = get_vert_gravity_yard_restr()
                    H_R_b = h_4 + h_R_b

                    H = min(H, H_R_b)

                elif data.n_position == 'outer':
                    h_R_n = get_vert_hump_track_restr()
                    H_R_n = h_4 + h_R_n

                    H = min(H, H_R_n)

        elif data.equipment_arrangement == 'carriage_body' and data.adjustable:
            h_4_p = get_vert_carriage_body_adjustable_parts_restr()
            H = point_height + h_4_p

            if data.n_position == 'outer':
                h_R_n = get_vert_hump_track_restr()
                H_P_R_n = h_4_p + h_R_n

                H = min(H, H_P_R_n)

    return H


# Определение высоты точек проектного очертания

def get_vertical_project_position(point_number, point_height, upper_or_lower_point):
    """ Определение наименьшей высоты точек проектного очертания, H, мм """
    H_proj = None

    # Ж.27.2 расчет по формуле 2.99 из ЦВ-4422-86
    if data.diagram_type in ['T', '1-T'] and point_number in [8, 9, 10]:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    elif data.diagram_type == 'Tz' and point_number in [7, 8, 9, 10]:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    elif data.diagram_type == 'Tpr' and point_number in [5, 6, 7]:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    elif data.diagram_type in ['0-VM', '1-VM'] and point_number in [9, 10, 11, 12]:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    elif data.diagram_type == '02-VM' and point_number == 8:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    elif data.diagram_type == '03-VM' and point_number == 5:
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    # Ж.27.1
    elif upper_or_lower_point == 'upper':
        H_i_w = point_height
        H_proj = H_i_w - data.e_y

    # Ж.27.2 расчет по формуле 2.99 из ЦВ-4422-86
    elif upper_or_lower_point == 'lower':
        H_i = get_vertical_build_position(point_height, upper_or_lower_point)
        H_proj = H_i + data.e_y

    return H_proj


class Result:
    def __init__(self,
                 number,
                 initial_vertical_coord,
                 initial_horizontal_coord,
                 build_vertical_coord,
                 project_vertical_coord,
                 build_horizontal_coord,
                 project_horizontal_coord,
                 main_or_additional
                 ):
        self.number = number
        # Изначальные координаты точки
        self.v_c = initial_vertical_coord
        self.h_c = initial_horizontal_coord
        # Строительные координаты точки
        self.v_b_c = build_vertical_coord
        self.h_b_c = build_horizontal_coord
        # Проектные координаты точки
        self.v_p_c = project_vertical_coord
        self.h_p_c = project_horizontal_coord
        # Основная или дополнительная точка
        self.main_or_additional = main_or_additional


#######################################
# Окончательные  вычисления #
#######################################


def main_calc():
    result_array = []
    diagram = diagrams.diagram

    for point in diagram:
        vert_build_coord = get_vertical_build_position(point.height, point.upper_or_lower)
        horizontal_build_coord = get_horizontal_build_position(point.width, point.upper_or_lower, point.number)
        vert_project_coord = get_vertical_project_position(point.number, point.height, point.upper_or_lower)
        horizontal_project_coord = get_horizontal_project_position(point.width, point.upper_or_lower, point.number)
        result_array.append(Result(number=point.number,
                                   initial_vertical_coord=point.height,
                                   initial_horizontal_coord=point.width,
                                   build_vertical_coord=vert_build_coord,
                                   project_vertical_coord=vert_project_coord,
                                   build_horizontal_coord=horizontal_build_coord,
                                   project_horizontal_coord=horizontal_project_coord,
                                   main_or_additional=point.main_or_additional,
                                   )
                            )
    return result_array


if __name__ == "__main__":

    RESULT = main_calc()
    for i in range(len(RESULT)):
        print('Номер', RESULT[i].number,
              'Верт коорд', RESULT[i].v_c,
              'Горизонт коорд', RESULT[i].h_c,
              'Верт стр коорд', RESULT[i].v_b_c,
              'Горизонт стр коорд', RESULT[i].h_b_c,
              'Верт проект коорд', RESULT[i].v_p_c,
              'Горизонт проект коорд', RESULT[i].h_p_c)
