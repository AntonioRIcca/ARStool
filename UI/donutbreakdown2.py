# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the Donut Chart Breakdown example from Qt v5.x"""


import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QColor, QFont, QPainter, QBrush
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCharts import QtCharts
colors = [Qt.red, Qt.darkGreen, Qt.darkBlue, Qt.darkMagenta, Qt.darkCyan]


class MainSlice(QtCharts.QPieSlice):
    def __init__(self, breakdown_series, parent=None):
        super().__init__(parent)

        self.breakdown_series = breakdown_series
        self.name = None

        self.percentageChanged.connect(self.update_label)

    def get_breakdown_series(self):
        return self.breakdown_series

    def set_name(self, name):
        self.name = name

    def name(self):
        return self.name

    @Slot()
    def update_label(self):
        p = self.percentage() * 100
        self.setLabel(f"{self.name + '<br>'} {p:.1f}%")


class DonutBreakdownChart(QtCharts.QChart):
    def __init__(self, mcat, data, parent=None):
        super().__init__(QtCharts.QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
        self.main_series = QtCharts.QPieSeries()
        self.main_series.setPieSize(0.7)
        self.addSeries(self.main_series)

        self.setBackgroundBrush(QBrush(QColor('transparent')))
        self.legend().setLabelColor('white')
        self.setTitleBrush(QColor(255,255,255))
        self.setTitleFont(QFont("Arial", 12))

        for i in range(len(data)):
            cat = list(data.keys())[i]
            # print(cat)
            series = 'series' + str(i+1)
            self.__setattr__(series, QtCharts.QPieSeries())
            self.__getattribute__(series).setName(cat)
            for elem in data[cat]:
                self.__getattribute__(series).append(elem, data[cat][elem]['p'])
            self.add_breakdown_series(self.__getattribute__(series), colors[i])


        # self.series1 = QtCharts.QPieSeries()
        # self.series1.setName("Fossil fuels")
        # self.series1.append("Oil", 353295)
        # self.series1.append("Coal", 188500)
        # self.series1.append("Natural gas", 148680)
        # self.series1.append("Peat", 94545)
        #
        # self.series2 = QtCharts.QPieSeries()
        # self.series2.setName("Renewables")
        # self.series2.append("Wood fuels", 319663)
        # self.series2.append("Hydro power", 45875)
        # self.series2.append("Wind power", 1060)
        #
        # self.series3 = QtCharts.QPieSeries()
        # self.series3.setName("Others")
        # self.series3.append("Nuclear energy", 238789)
        # self.series3.append("Import energy", 37802)
        # self.series3.append("Other", 32441)

        # donut_breakdown = DonutBreakdownChart()
        self.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.setTitle(mcat)
        self.legend().setAlignment(Qt.AlignRight)
        # self.legend().setVisible(False)
        # self.add_breakdown_series(self.series1, Qt.red)
        # self.add_breakdown_series(self.series2, Qt.darkGreen)
        # self.add_breakdown_series(self.series3, Qt.darkBlue)

    def add_breakdown_series(self, breakdown_series, color):
        font = QFont("Arial", 8)
        QFont()

        # add breakdown series as a slice to center pie
        main_slice = MainSlice(breakdown_series)
        main_slice.set_name(breakdown_series.name())
        main_slice.setValue(breakdown_series.sum())
        self.main_series.append(main_slice)

        # customize the slice
        main_slice.setBrush(color)
        main_slice.setLabelVisible()
        main_slice.setLabelColor(Qt.white)
        main_slice.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
        main_slice.setLabelFont(font)
        main_slice.setLabelColor('white')

        # position and customize the breakdown series
        breakdown_series.setPieSize(0.8)
        breakdown_series.setHoleSize(0.7)
        breakdown_series.setLabelsVisible()

        print('slices =', len(breakdown_series.slices()))
        f_light = pow(2.2, 1 / len(breakdown_series.slices())) * 100
        print('f_light =', f_light)
        for pie_slice in breakdown_series.slices():
            # color = QColor(color).lighter(110)
            color = QColor(color).lighter(f_light)
            pie_slice.setBrush(color)
            pie_slice.setLabelFont(font)
            pie_slice.setLabelColor('white')

        # add the series to the chart
        self.addSeries(breakdown_series)

        # recalculate breakdown donut segments
        self.recalculate_angles()

        # update customize legend markers
        self.update_legend_markers()

    def recalculate_angles(self):
        angle = 0
        slices = self.main_series.slices()
        for pie_slice in slices:
            breakdown_series = pie_slice.get_breakdown_series()
            breakdown_series.setPieStartAngle(angle)
            angle += pie_slice.percentage() * 360.0  # full pie is 360.0
            breakdown_series.setPieEndAngle(angle)

    def update_legend_markers(self):
        # go through all markers
        for series in self.series():
            markers = self.legend().markers(series)
            for marker in markers:
                if series == self.main_series:
                    # hide markers from main series
                    marker.setVisible(False)
                else:
                    # modify markers from breakdown series
                    label = marker.slice().label()
                    p = marker.slice().percentage() * 100
                    # marker.setLabel(f"{label + '<br>'} {p:.1f}%")
                    marker.setLabel(f"{label} {p:.1f}%")
                    marker.setFont(QFont("Arial", 8))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Graph is based on data of:
    #    'Total consumption of energy increased by 10 per cent in 2010'
    # Statistics Finland, 13 December 2011
    # http://www.stat.fi/til/ekul/2010/ekul_2010_2011-12-13_tie_001_en.html
    # series1 = QtCharts.QPieSeries()
    # series1.setName("Fossil fuels")
    # series1.append("Oil", 353295)
    # series1.append("Coal", 188500)
    # series1.append("Natural gas", 148680)
    # series1.append("Peat", 94545)
    #
    # series2 = QtCharts.QPieSeries()
    # series2.setName("Renewables")
    # series2.append("Wood fuels", 319663)
    # series2.append("Hydro power", 45875)
    # series2.append("Wind power", 1060)
    #
    # series3 = QtCharts.QPieSeries()
    # series3.setName("Others")
    # series3.append("Nuclear energy", 238789)
    # series3.append("Import energy", 37802)
    # series3.append("Other", 32441)
    #
    donut_breakdown = DonutBreakdownChart(None)
    # donut_breakdown.setAnimationOptions(QtCharts.QChart.AllAnimations)
    # donut_breakdown.setTitle("Total consumption of energy in Finland 2010")
    # donut_breakdown.legend().setAlignment(Qt.AlignRight)
    # donut_breakdown.add_breakdown_series(series1, Qt.red)
    # donut_breakdown.add_breakdown_series(series2, Qt.darkGreen)
    # donut_breakdown.add_breakdown_series(series3, Qt.darkBlue)

    window = QMainWindow()
    chart_view = QtCharts.QChartView(donut_breakdown)
    chart_view.setRenderHint(QPainter.Antialiasing)
    window.setCentralWidget(chart_view)
    available_geometry = window.screen().availableGeometry()
    size = available_geometry.height() * 0.75
    window.resize(size, size * 0.8)
    window.show()

    sys.exit(app.exec_())
