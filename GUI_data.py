import wx
import input_data as D
import GUI_result


class DataInputDlg(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.SetSize(1300,1000)

        position = wx.Point(50,50)        
        self.SetPosition(position)

        panel = wx.Panel(self)
        panel.SetBackgroundColour('#696969')
        


        ###############################
        # Главный вертикальный сайзер #
        ###############################
        
        main_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        # tc = wx.TextCtrl(panel)
        # main_vertical_sizer.Add(tc, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

      
        self.main_label = wx.StaticText(panel, label = "Данные для расчета", style = wx.ALIGN_CENTER)
        main_vertical_sizer.Add(self.main_label, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=5)


        ############################№№№#####
        # Главный горизонтальный субсайзер #
        ####################################

        horizontal_sub_sizer = wx.BoxSizer(wx.HORIZONTAL)

        


        ##########################
        # Левая колонка значений #
        ##########################
        left_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        
        self.L1_panel = InputDataPanel(parent=panel,
                                panel_name="Направляющая база подвижного состава",
                                unit= "м",
                                value_name = 'l',
                                value = D.l)
        left_vertical_sizer.Add(self.L1_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)


        self.L2_panel = InputDataPanel(parent=panel,
                                panel_name="База тележки",
                                unit= "м",
                                value_name = 'p',
                                value = D.p)
        left_vertical_sizer.Add(self.L2_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L3_panel = InputDataPanel(parent=panel,
                                panel_name="Сила тяжести подвижного состава брутто",
                                unit= "кН",
                                value_name = 'Q',
                                value = D.Q)
        left_vertical_sizer.Add(self.L3_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L4_panel = InputDataPanel(parent=panel,
                                panel_name="Сила тяжести тары",
                                unit= "кН",
                                value_name = 'T',
                                value = D.T)
        left_vertical_sizer.Add(self.L4_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)
        
        self.L5_panel = InputDataPanel(parent=panel,
                                panel_name="Сила тяжести тележки",
                                unit= "кН",
                                value_name = 'Qt',
                                value = D.Q_t)
        left_vertical_sizer.Add(self.L5_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L6_panel = InputDataPanel(parent=panel,
                                panel_name="Расчетная нагрузка на одну тележку",
                                unit= "кН",
                                value_name = 'Pp',
                                value=D.P_p)
        left_vertical_sizer.Add(self.L6_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L7_panel = InputDataPanel(parent=panel,
                                panel_name="Гибкость надбуксовых рессор тележки",
                                unit= "мм/кН",
                                value_name = 'λ1',
                                value=D.lambda_1)
        left_vertical_sizer.Add(self.L7_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L8_panel = InputDataPanel(parent=panel,
                                panel_name="Гибкость центральных рессор тележки",
                                unit= "мм/кН",
                                value_name = 'λ2',
                                value=D.lambda_2)
        left_vertical_sizer.Add(self.L8_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L9_panel = InputDataPanel(parent=panel,
                                panel_name="Максимальный диаметр новых колес",
                                unit= "мм",
                                value_name = 'Dmax',
                                value=D.D_max)
        left_vertical_sizer.Add(self.L9_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.L10_panel = InputDataPanel(parent=panel,
                                panel_name="Минимальный диаметр предельно изношенных колес",
                                unit= "мм",
                                value_name = 'Dmin',
                                value=D.D_min)
        left_vertical_sizer.Add(self.L10_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

 

        
        ############################
        # Средняя колонка значений #
        ############################

        central_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        

        self.C1_panel = InputDataPanel(parent=panel,
                                panel_name='Максимально допустимый прокат \
бандажей (включая местную выбоину в размере 1 мм) \
за период между обточками колес',
                                unit= "мм",
                                value_name = 'hᵖ₀',
                                value=D.h_0_p)
        central_vertical_sizer.Add(self.C1_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C2_panel = InputDataPanel(parent=panel,
                                panel_name='Понижение буксы (или другой части) \
относительно оси колесной пары вследствие износов \
подшипника и осевой шейки по радиусу',
                                unit= "мм",
                                value_name = 'Δh₁',
                                value=D.delta_h_1)
        central_vertical_sizer.Add(self.C2_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C3_panel = InputDataPanel(parent=panel,
                                panel_name='''Понижение буксы (или другой части) \
относительно оси колесной пары за период между обточками колес''',
                                unit= "мм",
                                value_name = 'Δhᵖ₁',
                                value=D.delta_h_1_p)
        central_vertical_sizer.Add(self.C3_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C4_panel = InputDataPanel(parent=panel,
                                panel_name='''Понижение рамы тележки относительно \
буксы вследствие вертикальных износов опорных поверхностей''',
                                unit= "мм",
                                value_name = 'Δh₂',
                                value=D.delta_h_2)
        central_vertical_sizer.Add(self.C4_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C5_panel = InputDataPanel(parent=panel,
                                panel_name='''Понижение рамы тележки относительно \
буксы за период между обточками колес''',
                                unit= "мм",
                                value_name = 'Δhᵖ₂',
                                value=D.delta_h_2_p)
        central_vertical_sizer.Add(self.C5_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C6_panel = InputDataPanel(parent=panel,
                                panel_name='''Понижение надрессорной балки относительно \
рамы тележек из-за износов и зазоров в элементах ее подвески''',
                                unit= "мм",
                                value_name = 'Δh₃',
                                value=D.delta_h_3)
        central_vertical_sizer.Add(self.C6_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C7_panel = InputDataPanel(parent=panel,
                                panel_name='''Понижение надрессорной балки относительно \
рамы тележек за период между обточками колес''',
                                unit= "мм",
                                value_name = 'Δhᵖ₃',
                                value=D.delta_h_3_p)
        central_vertical_sizer.Add(self.C7_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C8_panel = InputDataPanel(parent=panel,
                                panel_name='''Допускаемый вертикальный износ \
пятника и подпятника (или скользунов)''',
                                unit= "мм",
                                value_name = 'Δh₄',
                                value=D.delta_h_4)
        central_vertical_sizer.Add(self.C8_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.C9_panel = InputDataPanel(parent=panel,
                                panel_name='''Вертикальный износ пятника и подпятника \
(или скользунов) за период между обточками колес''',
                                unit= "мм",
                                value_name = 'Δhᵖ₄',
                                value=D.delta_h_4_p)
        central_vertical_sizer.Add(self.C9_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)






    
        ###########################
        # Правая колонка значений #
        #########################№#

        right_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        
        self.R1_panel = InputDataPanel(parent=panel,
                                panel_name='''Минимально допускаемая толщина \
гребня бандажа на уровне верха головки рельса''',
                                unit= "мм",
                                value_name = 't',
                                value = D.t)
        right_vertical_sizer.Add(self.R1_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R2_panel = InputDataPanel(parent=panel,
                                panel_name='''Вертикальное расстояние от центра \
тяжести груженого кузова до нижней поверхности подпятника''',
                                unit= "мм",
                                value_name = 'hцт',
                                value = D.h_zt)
        right_vertical_sizer.Add(self.R2_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R3_panel = InputDataPanel(parent=panel,
                                panel_name='''Возможное поперечное смещение \
буксы относительно колесной пары''',
                                unit= "мм",
                                value_name = "q'",
                                value = D.q_apostrophe)
        right_vertical_sizer.Add(self.R3_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R4_panel = InputDataPanel(parent=panel,
                                panel_name='''Возможное поперечное смещение \
рамы тележки относительно буксы''',
                                unit= "мм",
                                value_name = "q''",
                                value = D.q_double_apostrophe)
        right_vertical_sizer.Add(self.R4_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R5_panel = InputDataPanel(parent=panel,
                                panel_name='''Наибольшее возможное поперечное \
перемещение в направляющем сечении в одну сторону из центрального положения \
кузова относительно рамы тележки вследствие наличия зазоров при максимальных \
износах и деформациях упругих элементов в узле сочленения кузова и рамы тележки''',
                                unit= "мм",
                                value_name = "w'",
                                value = D.w_apostrophe)
        right_vertical_sizer.Add(self.R5_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R6_panel = InputDataPanel(parent=panel,
                                panel_name='''Возможное поперечное смещение пятника \
относительно подпятника (или скользунов относительно друг друга при опоре на скользуны)''',
                                unit= "мм",
                                value_name = "w''",
                                value = D.w_double_apostrophe)
        right_vertical_sizer.Add(self.R6_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R7_panel = InputDataPanel(parent=panel,
                                panel_name='''Остаточная осадка надбуксовых рессор''',
                                unit= "мм",
                                value_name = "f01",
                                value = D.f_01)
        right_vertical_sizer.Add(self.R7_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R8_panel = InputDataPanel(parent=panel,
                                panel_name='''Остаточная осадка центральных рессор''',
                                unit= "мм",
                                value_name = "f02",
                                value = D.f_02)
        right_vertical_sizer.Add(self.R8_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.R9_panel = InputDataPanel(parent=panel,
                                panel_name='''Собственный прогиб под нагрузкой среднего \
сечения конструкции рамы подвижного состава (хребтовая балка)''',
                                unit= "мм",
                                value_name = "z",
                                value = D.z)
        right_vertical_sizer.Add(self.R9_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)




        horizontal_sub_sizer.Add(left_vertical_sizer, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        horizontal_sub_sizer.Add(central_vertical_sizer, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        horizontal_sub_sizer.Add(right_vertical_sizer, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)


        main_vertical_sizer.Add(horizontal_sub_sizer, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        # Сайзер с кнопками

        footer_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)


        self.btn_confirm = wx.Button(panel, wx.ID_OK, label='Вернуться', size=(300,30))
        footer_horizontal_sizer.Add(self.btn_confirm, 0, flag = wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)

        self.btn_calc = CalculationButton(panel, label='Рассчитать', size=(140,30))
        footer_horizontal_sizer.Add(self.btn_calc, 0, flag = wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        

        main_vertical_sizer.Add(footer_horizontal_sizer, 0, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)




        panel.SetSizer(main_vertical_sizer)

        # filter_panels()


    def filter_panels(self):
        if D.adjustable == False:
            
            self.C3_panel.Show(False) # delta_hp1
            self.C5_panel.Show(False) # delta_hp2
            self.C7_panel.Show(False) # delta_hp3
            self.C9_panel.Show(False) # delta_hp4

            
        
        if D.equipment_arrangement == 'wheel':
            self.L6_panel.Show(False) # Pp
            self.L7_panel.Show(False) # lambda_1
            self.L8_panel.Show(False) # lambda_2
            self.R7_panel.Show(False) # f_01
            self.R8_panel.Show(False) # f_02
            self.R9_panel.Show(False) # z
            




       


    
        



class InputDataPanel(wx.Panel):
    def __init__(self, parent, panel_name, unit, value_name, value):
        
        self.panel_name = panel_name
        self.value_name = value_name
        self.value = value
        self.unit = unit

        _size = wx.Size(40, 50)
        _font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        super().__init__(parent, size = _size)

        self.SetBackgroundColour('#D3D3D3')
 
        self.vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label = self.panel_name, style = wx.ALIGN_CENTER)
        self.vboxsizer.Add(self.label, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        ########################################################

        self.hboxsizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.label3 = wx.StaticText(self, label = f"{value_name} = ", style = wx.ALIGN_CENTER)
        self.label.SetFont(_font)
        self.label3.Bind(wx.EVT_TEXT,self.OnKeyTyped)
        self.hboxsizer1.Add(self.label3, 0, wx.LEFT)
               
        self.value_ = wx.TextCtrl(self, value = str(value))
        self.value_.Bind(wx.EVT_TEXT,self.OnKeyTyped)
        self.hboxsizer1.Add(self.value_, proportion=1)

        self.label2 = wx.StaticText(self, label = f'      {self.unit} ' , style = wx.ALIGN_CENTER)
        self.hboxsizer1.Add(self.label2, 0 ,wx.EXPAND)

        self.vboxsizer.Add(self.hboxsizer1, 0, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        self.SetSizer(self.vboxsizer)

    def OnKeyTyped(self, event):
        self.value = float(event.GetString())
        print (self.value)


        
class CalculationButton(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_calc_button)
    
    def on_calc_button(self, event):
        # print(input_data.e_x)
        result_dlg = GUI_result.ResultDlg(self, title = 'Результат расчета')
        res = result_dlg.ShowModal()
        result_dlg.Destroy
        # print(res)


# data_input_dlg = DataInputDlg(None, title = 'Ввод данных для расчета')
        