import wx
import GUI_data
import input_data
import wx.lib.masked.numctrl
import diagramms

BACKGROUND_COLOUR = '#696969'
PANEL_COLOUR = '#D3D3D3'


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent,
                         title=title,
                         size=(800, 900),
                         pos=(50, 50),
                         style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        panel = wx.Panel(self)
        panel.SetBackgroundColour(BACKGROUND_COLOUR)

        # Main sizer
        main_vbox = wx.BoxSizer(wx.VERTICAL)

        # Sub sizer
        main_hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Left sizer content

        left_vbox = wx.BoxSizer(wx.VERTICAL)

        dyagramm_panel = TypeOfDiagrammPanel(panel)
        left_vbox.Add(dyagramm_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.rail_width_panel = RailWidth(panel)
        left_vbox.Add(self.rail_width_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        minimal_radius_panel = MinimalRadius(panel)
        left_vbox.Add(minimal_radius_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        equipment_position_panel = EquipmentPosition(panel)
        left_vbox.Add(equipment_position_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.position_of_section = PositionOfSection(panel)
        left_vbox.Add(self.position_of_section, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        # Place left sizer

        main_hbox.Add(left_vbox, flag=wx.EXPAND | wx.ALL, border=10)

        # Right sizer content

        right_vbox = wx.BoxSizer(wx.VERTICAL)

        equipment_arrangement_panel = EquipmentArrangementPanel(panel)
        right_vbox.Add(equipment_arrangement_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        vertical_ajustment_panel = VerticalAjustment(panel)
        right_vbox.Add(vertical_ajustment_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        tolerance_panel = Tolerance(panel)
        right_vbox.Add(tolerance_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        hinge_panel = Hinge(panel)
        right_vbox.Add(hinge_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        self.gravity_yard_panel = GravityYard(panel)
        right_vbox.Add(self.gravity_yard_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)

        # Place right sizer

        main_hbox.Add(right_vbox, flag=wx.EXPAND | wx.ALL, border=10)

        # Place subsizer in the main sizer

        main_vbox.Add(main_hbox, 1, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        # Footer subsizer

        footer_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_data = DataButton(panel, label='Ввести дополнительные данные для расчета', size=(300, 30))
        footer_horizontal_sizer.Add(self.btn_data, 0, flag=wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=0)

        main_vbox.Add(footer_horizontal_sizer, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.BOTTOM, border=20)

        panel.SetSizer(main_vbox)

        # Start settings

        self.rail_width_panel.rb_1430.Enable(True)


class TypeOfDiagrammPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Тип габарита", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_T = wx.RadioButton(self, wx.ID_ANY, label="Т", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_T, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_T.SetToolTip(wx.ToolTip('''    Т- статический габарит для подвижного состава, допускаемого \
в обращение по железнодорожным путям общего и необщего пользования шириной колеи 1520 мм на \
электрифицированных железных дорогах и других участках, сооружения и устройства на которых отвечают \
требованиям габаритов приближения строений C и Cр'''))

        self.rb_Tz = wx.RadioButton(self, wx.ID_ANY, label="Тц")
        vboxsizer.Add(self.rb_Tz, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_Tz.SetToolTip(wx.ToolTip('''    Тц - статический габарит для цистерн, вагонов-самосвалов \
и другого подвижного состава, допускаемого к обращению по железнодорожным путям общего и необщего пользования, \
сооружения и устройства на которых приведены к требованиям контрольного очертания, указанного в \
приложении Г ГОСТ 9238-2013'''))

        self.rb_Tpr = wx.RadioButton(self, wx.ID_ANY, label="Тпр")
        vboxsizer.Add(self.rb_Tpr, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_Tpr.SetToolTip(wx.ToolTip('''    Тпр - статический габарит для железнодорожного подвижного \
состава, допускаемого к обращению на главных путях перегонов и станций, а также по другим железнодорожным \
путям, сооружения устройства и междупутья которых приведены в соответствие с требованиями контрольного \
очертания, указанного на рисунке Г.1 (приложение Г) ГОСТ 9238-2013, или имеют технологическую негабаритность'''))

        self.rb_1_T = wx.RadioButton(self, wx.ID_ANY, label="1-Т")
        vboxsizer.Add(self.rb_1_T, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_1_T.SetToolTip(wx.ToolTip('''    1-Т - статический габарит для железнодорожного подвижного \
состава, допускаемого в обращение по всем железнодорожным путям общего и необщего пользования, внешним и \
внутренним путям промышленных и транспортных предприятий железных дорог государств-участников Содружества \
Независимых Государств (СНГ), а также Грузии и Латвии, Литвы, Эстонии'''))

        self.rb_1_VM = wx.RadioButton(self, wx.ID_ANY, label="1-ВМ")
        vboxsizer.Add(self.rb_1_VM, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_1_VM.SetToolTip(wx.ToolTip('''    1-ВМ - статический габарит для железнодорожного подвижного\
состава, допускаемого в обращение как по железнодорожным путям шириной колеи 1520 (1524) мм, так и шириной \
колеи 1435 мм, используемых для международных сообщений в соответствии с приложением А ГОСТ 9238-2013'''))

        self.rb_0_VM = wx.RadioButton(self, wx.ID_ANY, label="0-ВМ")
        vboxsizer.Add(self.rb_0_VM, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_0_VM.SetToolTip(wx.ToolTip('''    0-ВМ - статический габарит для железнодорожного подвижного \
состава, допускаемого в обращение как по железным дорогам колеи 1520 (1524) мм, так и по линиям железных дорог \
- членов Организации сотрудничества железных дорог (ОСЖД) и Международного Союза железных дорог (МСЖД) \
колеи 1435 мм, с ограничениями только на отдельных участках согласно приложению А ГОСТ 9238-2013'''))

        self.rb_02_VM = wx.RadioButton(self, wx.ID_ANY, label="02-ВМ")
        vboxsizer.Add(self.rb_02_VM, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_02_VM.SetToolTip(wx.ToolTip('''    02-ВМ - статический габарит для железнодорожного подвижного \
состава, допускаемого в обращение как по всей сети железных дорог колеи 1520 (1524) мм, так и по железным \
дорогам - членам ОСЖД колеи 1435 мм, за исключением отдельных участков согласно приложению А ГОСТ 9238-2013'''))

        self.rb_03_VM = wx.RadioButton(self, wx.ID_ANY, label="03-ВМ")
        vboxsizer.Add(self.rb_03_VM, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        self.rb_03_VM.SetToolTip(wx.ToolTip('''    03-ВМ - статический габарит для железнодорожного подвижного \
состава, допускаемого к обращению как по всей сети железных дорог колеи 1520 (1524) мм, так и по всем железным \
дорогам колеи 1435 мм европейских и азиатских стран'''))

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_T.GetId():
            input_data.diagram_type = 'T'
            frame.rail_width_panel.rb_1520.SetValue(True)
            frame.rail_width_panel.rb_1430.Enable(False)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(False)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_Tz.GetId():
            input_data.diagram_type = 'Tz'
            frame.rail_width_panel.rb_1520.SetValue(True)
            frame.rail_width_panel.rb_1430.Enable(False)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(False)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_Tpr.GetId():
            input_data.diagram_type = 'Tpr'
            frame.rail_width_panel.rb_1520.SetValue(True)
            frame.rail_width_panel.rb_1430.Enable(False)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(False)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_1_T.GetId():
            input_data.diagram_type = '1-T'
            frame.rail_width_panel.rb_1520.SetValue(True)
            frame.rail_width_panel.rb_1430.Enable(False)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(False)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_1_VM.GetId():
            input_data.diagram_type = '1-VM'
            frame.rail_width_panel.rb_1430.Enable(True)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(True)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_0_VM.GetId():
            input_data.diagram_type = '0-VM'
            frame.rail_width_panel.rb_1430.Enable(True)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(True)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_02_VM.GetId():
            input_data.diagram_type = '02-VM'
            frame.rail_width_panel.rb_1430.Enable(True)
            frame.gravity_yard_panel.rb_1.Enable(True)
            frame.gravity_yard_panel.rb_2.Enable(True)
            frame.gravity_yard_panel.rb_3.Enable(True)
            frame.gravity_yard_panel.rb_4.Enable(True)

        if rb.GetId() == self.rb_03_VM.GetId():
            input_data.diagram_type = '03-VM'
            frame.rail_width_panel.rb_1430.Enable(True)
            frame.gravity_yard_panel.rb_1.Enable(False)
            frame.gravity_yard_panel.rb_2.Enable(False)
            frame.gravity_yard_panel.rb_3.Enable(False)
        print(input_data.diagram_type)


class RailWidth(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Ширина колеи", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_1520 = wx.RadioButton(self, label="1520 мм", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_1520, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_1430 = wx.RadioButton(self, label="1430 мм")
        vboxsizer.Add(self.rb_1430, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_1520.GetId():
            input_data.track_gauge = 1520

        if rb.GetId() == self.rb_1430.GetId():
            input_data.track_gauge = 1430

        # print (input_data.track_gauge)


class MinimalRadius(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Минимальный радиус кривой пути", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_150 = wx.RadioButton(self, label="150 м", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_150, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_80 = wx.RadioButton(self, label="80 м")
        vboxsizer.Add(self.rb_80, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_40 = wx.RadioButton(self, label="40 м")
        vboxsizer.Add(self.rb_40, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_150.GetId():
            input_data.track_gauge = 150

        if rb.GetId() == self.rb_80.GetId():
            input_data.track_gauge = 80

        if rb.GetId() == self.rb_40.GetId():
            input_data.track_gauge = 40

        # print (input_data.track_gauge)


class EquipmentPosition(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="""Положение оборудования
относительно направляющего сечения""", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_inner = wx.RadioButton(self, label="Внутреннее сечение", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_inner, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_outer = wx.RadioButton(self, label="Наружнее сечение")
        vboxsizer.Add(self.rb_outer, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_zero = wx.RadioButton(self, label="Направляющее сечение")
        vboxsizer.Add(self.rb_zero, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_inner.GetId():
            input_data.n_position = 'inner'
            frame.position_of_section.horizontal_tolerance.SetEditable(True)

        if rb.GetId() == self.rb_outer.GetId():
            input_data.n_position = 'outer'
            frame.position_of_section.horizontal_tolerance.SetEditable(True)

        if rb.GetId() == self.rb_zero.GetId():
            input_data.n_position = 'zero'
            frame.position_of_section.horizontal_tolerance.ChangeValue('0')
            frame.position_of_section.horizontal_tolerance.SetEditable(False)
            input_data.n = 0

        # print (input_data.track_gauge)


class PositionOfSection(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        self.vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="""   Расстояние от направляющего сечения
  до рассчитываемого сечения""", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        self.vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.hboxsizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.label1 = wx.StaticText(self, label="Растояние (n) :   ", style=wx.ALIGN_CENTER)
        self.hboxsizer1.Add(self.label1, 0,  flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.horizontal_tolerance = wx.TextCtrl(self, value=str(input_data.n))
        self.hboxsizer1.Add(self.horizontal_tolerance, proportion=1)
        self.horizontal_tolerance.Bind(wx.EVT_TEXT, self.on_key_typed)

        self.label2 = wx.StaticText(self, label="  м  ", style=wx.ALIGN_CENTER)
        self.hboxsizer1.Add(self.label2, 0,  flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.vboxsizer.Add(self.hboxsizer1, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.SetSizer(self.vboxsizer)

    def on_key_typed(self, event):
        value = event.GetString()
        input_data.n = float(value)
        # print (input_data.n)


class EquipmentArrangementPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Место размещения оборудования", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_weel = wx.RadioButton(self, label="Колесная пара", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_weel, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_axel_box = wx.RadioButton(self, label="Букса")
        vboxsizer.Add(self.rb_axel_box, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_bogie_frame = wx.RadioButton(self, label="Рама тележки")
        vboxsizer.Add(self.rb_bogie_frame, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_bolster = wx.RadioButton(self, label="Надрессорная балка")
        vboxsizer.Add(self.rb_bolster, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_carriage = wx.RadioButton(self, label="Кузов")
        vboxsizer.Add(self.rb_carriage, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_weel.GetId():
            input_data.equipment_arrangement = 'wheel'

        if rb.GetId() == self.rb_axel_box.GetId():
            input_data.equipment_arrangement = 'axel_box'

        if rb.GetId() == self.rb_bogie_frame.GetId():
            input_data.equipment_arrangement = 'bogie_frame'

        if rb.GetId() == self.rb_bolster.GetId():
            input_data.equipment_arrangement = 'bolster'

        if rb.GetId() == self.rb_carriage.GetId():
            input_data.equipment_arrangement = 'carriage_body'

        # print (input_data.equipment_arrangement)


class VerticalAjustment(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Регулировка оборудования по высоте", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_yes = wx.RadioButton(self, label="Регулируемое оборудование", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_yes, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_no = wx.RadioButton(self, label="Не регулируемое оборудование")
        vboxsizer.Add(self.rb_no, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiogroup)

        self.SetSizer(vboxsizer)
        # self.SetSizer(hboxsizer)

    def on_radiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_yes.GetId():
            input_data.adjustable = True

        if rb.GetId() == self.rb_no.GetId():
            input_data.adjustable = False

        # print (input_data.adjastible)


class Tolerance(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        self.vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="""Плюсовой конструктивный допуск
   на размещение оборудования""", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        self.vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        ########################################################

        self.hboxsizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.label1 = wx.StaticText(self, label="Горизонтальный допуск (ey):   ", style=wx.ALIGN_CENTER)
        self.hboxsizer1.Add(self.label1, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.horizontal_tolerance = wx.TextCtrl(self, value=str(input_data.e_x))
        self.horizontal_tolerance.Bind(wx.EVT_TEXT, self.on_key_typed_x_field)
        self.hboxsizer1.Add(self.horizontal_tolerance, proportion=1)

        self.label2 = wx.StaticText(self, label="  мм  ", style=wx.ALIGN_CENTER)
        self.hboxsizer1.Add(self.label2, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.vboxsizer.Add(self.hboxsizer1, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        ########################################################

        self.hboxsizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.label3 = wx.StaticText(self, label="Вертикальный допуск (ex):       ", style=wx.ALIGN_CENTER)
        self.hboxsizer2.Add(self.label3, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.vertical_tolerance = wx.TextCtrl(self, value=str(input_data.e_y))


        self.vertical_tolerance.Bind(wx.EVT_TEXT, self.on_key_typed_y_field)
        self.hboxsizer2.Add(self.vertical_tolerance, proportion=1)

        self.label4 = wx.StaticText(self, label="  мм  ", style=wx.ALIGN_CENTER)
        self.hboxsizer2.Add(self.label4, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.vboxsizer.Add(self.hboxsizer2, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.SetSizer(self.vboxsizer)
        # self.SetSizer(hboxsizer)

    @staticmethod
    def on_key_typed_x_field(event):
        input_data.e_x = float(event.GetString())
        # print (input_data.e_x)

    @staticmethod
    def on_key_typed_y_field(event):
        input_data.e_y = float(event.GetString())
        # print (input_data.e_y)


class Hinge(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        self.vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="""Зазор в шарнирном соединении""", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        self.vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        ########################################################

        self.hboxsizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.label3 = wx.StaticText(self, label="Зазор (Δq): ", style=wx.ALIGN_CENTER)
        self.hboxsizer2.Add(self.label3, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.clearance = wx.TextCtrl(self, value=str(input_data.delta_q))
        self.clearance.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.hboxsizer2.Add(self.clearance, proportion=1)

        self.label4 = wx.StaticText(self, label="  мм  ", style=wx.ALIGN_CENTER)
        self.hboxsizer2.Add(self.label4, 0, flag=wx.LEFT | wx.ALIGN_CENTRE)

        self.vboxsizer.Add(self.hboxsizer2, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.SetSizer(self.vboxsizer)
        # self.SetSizer(hboxsizer)

    def OnKeyTyped(self, event):
        input_data.delta_q = float(event.GetString())
        print(input_data.delta_q)


class GravityYard(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetBackgroundColour(PANEL_COLOUR)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Прохождение сортировочных горок", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        vboxsizer.Add(self.label, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_no = wx.RadioButton(self, label="Не проходит", style=wx.RB_GROUP)
        vboxsizer.Add(self.rb_no, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_1 = wx.RadioButton(self, label="Проходит с нерабочими (расторможенными) замедлителями")
        vboxsizer.Add(self.rb_1, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_2 = wx.RadioButton(self, label="Проходит с замедлителями в любом их положении")
        vboxsizer.Add(self.rb_2, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_3 = wx.RadioButton(self, label="Проходит с замедлителями ОСЖТ в любом их положении")
        vboxsizer.Add(self.rb_3, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_4 = wx.RadioButton(self, label="Проходит устройства надвига вагонов")
        vboxsizer.Add(self.rb_4, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.rb_5 = wx.RadioButton(self, label="Проходит устройства надвига вагонов в порожнем состоянии")
        vboxsizer.Add(self.rb_5, 0, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM, border=5)

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        self.SetSizer(vboxsizer)
        # self.SetSizer(hboxsizer)

    def OnRadiogroup(self, e):
        rb = e.GetEventObject()
        if rb.GetId() == self.rb_no.GetId():
            input_data.diagram_sub_type = 'clear'

        if rb.GetId() == self.rb_1.GetId():
            input_data.diagram_sub_type = 'turned_off_retarder'

        if rb.GetId() == self.rb_2.GetId():
            input_data.diagram_sub_type = 'turned_on_retarder'

        if rb.GetId() == self.rb_3.GetId():
            input_data.diagram_sub_type = 'turned_on_retarder_osjt'

        if rb.GetId() == self.rb_4.GetId():
            input_data.diagram_sub_type = 'gravity_yard'

        if rb.GetId() == self.rb_5.GetId():
            input_data.diagram_sub_type = 'gravity_yard_empty'

        # print (input_data.diagramm_sub_type)


class DataButton(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_data_button)

    def on_data_button(self, event):
        diagramms.initialize_diagram()
        data_input_dlg = GUI_data.DataInputDlg(self, title='Ввод данных для расчета')
        data_input_dlg.filter_panels()
        data_input_dlg.ShowModal()
        data_input_dlg.Destroy()



app = wx.App()

title_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)

frame = MyFrame(None, 'Расчет строительных и проектных очертаний подвижного состава')

frame.Show()
app.MainLoop()
