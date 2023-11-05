from functools import partial

from PySide2.QtCharts import QtCharts

from PySide2 import QtGui
from collections import namedtuple


# Data = namedtuple('Data', ['name', 'value', 'primary_color', 'secondary_color'])
#
# node = Data('Node', 333, QtGui.QColor("#82d3e5"), QtGui.QColor("#cfeef5"))
# connection = Data('Connection', 105, QtGui.QColor("#fd635c"), QtGui.QColor("#fdc4c1"))
# other = Data('Other', 20, QtGui.QColor("#feb543"), QtGui.QColor("#ffe3b8"))
#
# datas = [node, connection,other]


class PieChart(QtCharts.QChart):
    def __init__(self, data=None, parent=None):
        super(PieChart, self).__init__(parent)
        self.datas = data
        # self.set_data()

        self.legend().hide()
        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.outer = QtCharts.QPieSeries()
        self.inner = QtCharts.QPieSeries()
        self.outer.setHoleSize(0.35)
        self.inner.setPieSize(0.35)
        self.inner.setHoleSize(0.3)

        self.set_outer_series()
        self.set_inner_series()

        self.addSeries(self.outer)
        self.addSeries(self.inner)

    def set_outer_series(self):
        slices = list()
        for data in self.datas:
            slice_ = QtCharts.QPieSlice(data.name, data.value)
            slice_.setLabelVisible()
            slice_.setColor(data.primary_color)
            slice_.setLabelBrush(data.primary_color)

            slices.append(slice_)
            self.outer.append(slice_)

        for slice_ in slices:
            color = 'black'
            if slice_.percentage() > 0.1:
                slice_.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
                color = 'white'

            else:


                print(slice_.label(), slice_.percentage())

            label = "<p align='center' style='color:{}'>{}<br>{}%</p>".format(
                color,
                slice_.label(),
                round(slice_.percentage()*100, 2)
            )
            slice_.setLabel(label)
            # slice_.setLabel(str(slice_.percentage()))

            slice_.hovered.connect(partial(self.explode, slice_))

    def explode(self, slice_, is_hovered):
        if is_hovered:
            start = slice_.startAngle()
            end = slice_.startAngle() + slice_.angleSpan()
            self.inner.setPieStartAngle(end)
            self.inner.setPieEndAngle(start + 360)
        else:
            self.inner.setPieStartAngle(0)
            self.inner.setPieEndAngle(360)

        slice_.setExplodeDistanceFactor(0.1)
        slice_.setExploded(is_hovered)

    def set_inner_series(self):
        for data in self.datas:
            slice_ = self.inner.append(data.name, data.value)
            slice_.setColor(data.secondary_color)
            slice_.setBorderColor(data.secondary_color)

    def set_data(self):
        Data = namedtuple('Data', ['name', 'value', 'primary_color', 'secondary_color'])

        node = Data('Node', 333, QtGui.QColor("#82d3e5"), QtGui.QColor("#cfeef5"))
        connection = Data('Connection', 105, QtGui.QColor("#fd635c"), QtGui.QColor("#fdc4c1"))
        other = Data('Other', 20, QtGui.QColor("#feb543"), QtGui.QColor("#ffe3b8"))

        self.datas = [node, connection, other]
