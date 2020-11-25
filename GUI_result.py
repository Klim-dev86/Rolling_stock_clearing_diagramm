import wx
import calc
# import input_data
import DXF_output


class DocxButton(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_data_button)

    def on_data_button(self, event):
        pass


class DxfButton(wx.Button):
    def __init__(self, parent, label, size):
        super().__init__(parent, label=label, size=size)

        self.Bind(wx.EVT_BUTTON, self.on_calc_button)

    def on_calc_button(self, event):
        DXF_output.draw()
        DXF_output.output()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        RESULT = calc.main_calc()

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.list_ctrl.InsertColumn(0, "Номер точки")
        self.list_ctrl.InsertColumn(1, "Исходная высота")
        self.list_ctrl.InsertColumn(2, "Строительная высота")
        self.list_ctrl.InsertColumn(3, "Проектная высота")
        self.list_ctrl.InsertColumn(4, "Исходная ширина")
        self.list_ctrl.InsertColumn(5, "Строительная ширина")
        self.list_ctrl.InsertColumn(6, "Проектная ширина")

        for i in range(7):
            self.list_ctrl.SetColumnWidth(i, -2)

        index = 0
        for i in range(len(RESULT)):

            self.list_ctrl.InsertItem(index, str(RESULT[i].number))
            self.list_ctrl.SetItem(index, 1, str(RESULT[i].v_c))
            self.list_ctrl.SetItem(index, 2, str(RESULT[i].v_b_c))
            self.list_ctrl.SetItem(index, 3, str(RESULT[i].v_p_c))
            self.list_ctrl.SetItem(index, 4, str(RESULT[i].h_c))
            self.list_ctrl.SetItem(index, 5, str(RESULT[i].h_b_c))
            self.list_ctrl.SetItem(index, 6, str(RESULT[i].h_p_c))

            if index % 2:
                self.list_ctrl.SetItemBackgroundColour(index, "white")
            else:
                self.list_ctrl.SetItemBackgroundColour(index, "#fffacd")
            index += 1

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        self.dxf_btn = DxfButton(self, label='Экспортировать очертание в DXF файл', size=(300, 30))
        sizer.Add(self.dxf_btn, 0, wx.ALL, 5)

        self.dox_btn = DocxButton(self, label='Экспортировать таблицу в Word файл', size=(300, 30))
        sizer.Add(self.dox_btn, 0, wx.ALL, 5)

        self.SetSizer(sizer)


class ResultDlg(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSize(870, 700)

        panel = MyPanel(self)

