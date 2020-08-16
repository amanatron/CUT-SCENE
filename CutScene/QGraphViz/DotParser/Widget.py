#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
Dot perser implementation
"""
from PySide2.QtGui import QFontMetrics, QFont
from QGraphViz.DotParser import Node
from views.visualmodeelement_view import VisualModeElement


class Widget(Node):
    """
    The dot graphviz engine
    """
    def __init__(self, parent_widget, scene_element, parent_graph, edit_callback = None, delete_callback = None, new_item_callbacks={}, **kwargs):
        super().__init__(scene_element.itemID, parent_graph, **kwargs)
        self.widget = VisualModeElement(parent_widget, scene_element, 
                                        edit_callback=edit_callback,
                                        delete_callback=delete_callback,
                                        new_item_callbacks=new_item_callbacks)
        self.widget.setMouseTracking(True)
        geometry = self.widget.geometry()
        width, height = geometry.size().width(), geometry.size().height()
        self.pos = [geometry.x()+width/2, geometry.y()+height/2]
        self.size = [width, height]
        self.widget.show()
