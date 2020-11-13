import wx
import calc
import input_data
import DXF_output



class WordButton(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_data_button)
    
    def on_data_button(self, event):
        data_input_dlg = GUI_data.DataInputDlg(self, title = 'Ввод данных для расчета')
        res = data_input_dlg.ShowModal()
        data_input_dlg.Destroy
        # print(res)


class DXF_Button(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_calc_button)
    
    def on_calc_button(self, event):
        DXF_output.draw()
        DXF_output.output()
        
        



class ResultDlg(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSize(1000,500)
        
        RESULT = calc.main_calc()
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#696969')

        main_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        number_of_points = len(RESULT) + 1

        gs = wx.GridSizer(number_of_points, 7, 5, 5)

        

        gs.Add(wx.StaticText(panel, label = "Номер точки"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Исх высота"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Исх полуразмах"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Стр высота"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Стр полуразмах"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Проектная высота"),0,wx.EXPAND)
        gs.Add(wx.StaticText(panel, label = "Проектный полуразмах"),0,wx.EXPAND)

        for i in range(len(RESULT)):
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].number}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].v_c}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].h_c}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].v_b_c}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].h_b_c}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].v_p_c}'),0,wx.EXPAND)
                gs.Add(wx.StaticText(panel, label =  f' {RESULT[i].h_p_c}'),0,wx.EXPAND)

        main_vertical_sizer.Add(gs, 1, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        

        footer_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)


        self.btn_calc = DXF_Button(panel, label='Экспортировать очертание в DXF файл', size=(300,30))
        footer_horizontal_sizer.Add(self.btn_calc, 0, flag = wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        

        self.btn_data = WordButton(panel, label='Экспортировать таблицу в Word файл', size = (300,30))
        footer_horizontal_sizer.Add(self.btn_data, 0, flag = wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)

        main_vertical_sizer.Add(footer_horizontal_sizer, 0, flag = wx.EXPAND|wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        panel.SetSizer(main_vertical_sizer)


        
        



    




