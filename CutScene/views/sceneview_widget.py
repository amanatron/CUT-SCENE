#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
A simple graphviz graphs viewer that enables creating graphs visually, 
manipulate them and save them
"""
from PySide2.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel, QSizePolicy
import sys
import os
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot


from PySide2.QtGui import QFontMetrics, QFont, QImage


class SceneViewWidget(QWidget):
    def __init__(self, main_controller, model):
        # Create QGraphViz widget
        super().__init__()
        self._main_controller = main_controller
        self._model = model
        self._main_controller.activeSceneChanged.connect(self.loadScene)
        self._model.sceneModified.connect(self.loadScene) # todo maybe dont re-render the entire scene when its modified

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setLayout(QVBoxLayout())
        self.setSizePolicy(sizePolicy)

        show_subgraphs=True
        self.qgv = QGraphViz(
            parent=self,
            show_subgraphs=show_subgraphs,
            auto_freeze= True, # show autofreeze capability
            new_edge_beingAdded_callback=self.new_edge_being_added,
            node_selected_callback=self.node_selected,
            edge_selected_callback=self.edge_selected,
            node_invoked_callback=self.node_invoked,
            edge_invoked_callback=self.edge_invoked,
            node_removed_callback=self.node_removed,
            edge_removed_callback=self.edge_removed,

            hilight_Nodes=True,
            hilight_Edges=True
            )
        self.qgv.setStyleSheet("background-color:rgb(255, 255, 255);")
        # Create A new Graph using Dot layout engine
        self.qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs, font = QFont("Arial", 12),margins=[20,20]))
        # Define sone graph
        n1 = self.qgv.addNode(self.qgv.engine.graph, "Node1", label="N1", fillcolor="red")
        n2 = self.qgv.addNode(self.qgv.engine.graph, "Node2", label="N2", fillcolor="blue:white:red")
        n3 = self.qgv.addNode(self.qgv.engine.graph, "Node3", label="N3", shape = "diamond",fillcolor="orange")
        n4 = self.qgv.addNode(self.qgv.engine.graph, "Node4", label="N4", shape="diamond",fillcolor="white")
        n5 = self.qgv.addNode(self.qgv.engine.graph, "Node5", label="N5", shape="polygon", fillcolor="red", color="white")
        n6 = self.qgv.addNode(self.qgv.engine.graph, "Node6", label="N6", shape="triangle", fillcolor="blue:white:red")

        sub = self.qgv.addSubgraph(self.qgv.engine.graph, "sub graph", self.qgv.engine.graph.graph_type, label="Subgraph", fillcolor="blue:white:red")
        n7 = self.qgv.addNode(sub, "Node7", label="N7")
        n8 = self.qgv.addNode(sub, "Node8", label="N8")

        sub2 = self.qgv.addSubgraph(self.qgv.engine.graph, "sub graph 2", self.qgv.engine.graph.graph_type, label="Subgraph 2", fillcolor="blue:white:red")
        n9 = self.qgv.addNode(sub, "Node9", label="N9")
        n10 = self.qgv.addNode(sub, "Node10", label="N10")

        # Adding nodes with an image as its shape
        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\icon\dbicon.png,100,100"
        n9 = self.qgv.addNode(self.qgv.engine.graph, "Node9", label="N9", shape=icon_path)

        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\icon\cam.png"
        n10 = self.qgv.addNode(self.qgv.engine.graph, "Node10", label="\n\n\nN10\nTest multilines", shape=icon_path, color="white")

        self.qgv.addEdge(n1, n2, {})
        self.qgv.addEdge(n3, n2, {})
        self.qgv.addEdge(n2, n4, {"width":2})
        self.qgv.addEdge(n4, n5, {"width":4})
        self.qgv.addEdge(n4, n6, {"width":5,"color":"red"})
        self.qgv.addEdge(n3, n6, {"width":2})
        self.qgv.addEdge(n6, n9, {"width":5,"color":"red"})
        self.qgv.addEdge(n9, n10, {"width":5,"color":"red"})
        self.qgv.addEdge(sub, sub2, {"width":4})


        # Build the graph (the layout engine organizes where the nodes and connections are)
        self.qgv.build()
        self.layout().addWidget(self.qgv)
        # Save it to a file to be loaded by Graphviz if needed

        # Add buttons                
        btnNew = QPushButton("New")    
        btnNew.clicked.connect(self.new)

        btnOpen = QPushButton("Open")    
        btnOpen.clicked.connect(self.load)

        btnSave = QPushButton("Save")    
        btnSave.clicked.connect(self.save)

        # hpanel.addWidget(btnNew)    
        # hpanel.addWidget(btnOpen)
        # hpanel.addWidget(btnSave)

        self.buttons_list=[]
        btnManip = QPushButton("Manipulate")    
        btnManip.setCheckable(True)
        btnManip.setChecked(True)
        btnManip.clicked.connect(self.manipulate)
        # hpanel.addWidget(btnManip)
        self.buttons_list.append(btnManip)

        btnAddNode = QPushButton("Add Node")    
        btnAddNode.clicked.connect(self.add_node)
        # hpanel.addWidget(btnAddNode)
        self.buttons_list.append(btnManip)

        btnRemNode = QPushButton("Rem Node")    
        btnRemNode.setCheckable(True)
        btnRemNode.clicked.connect(self.rem_node)
        # hpanel.addWidget(btnRemNode)
        self.buttons_list.append(btnRemNode)

        btnAddEdge = QPushButton("Add Edge")    
        btnAddEdge.setCheckable(True)
        btnAddEdge.clicked.connect(self.add_edge)
        # hpanel.addWidget(btnAddEdge)
        self.buttons_list.append(btnAddEdge)

        btnRemEdge = QPushButton("Rem Edge")    
        btnRemEdge.setCheckable(True)
        btnRemEdge.clicked.connect(self.rem_edge)
        # hpanel.addWidget(btnRemEdge)
        self.buttons_list.append(btnRemEdge)

        btnAddSubGraph = QPushButton("Add Subgraph")    
        btnAddSubGraph.clicked.connect(self.add_subgraph)
        # hpanel.addWidget(btnAddSubGraph)

        btnRemSubGraph = QPushButton("Rem Subgraph")    
        btnRemSubGraph.setCheckable(True)
        btnRemSubGraph.clicked.connect(self.rem_subgraph)
        # hpanel.addWidget(btnRemSubGraph)
        self.buttons_list.append(btnRemSubGraph)

    def loadScene(self):
        self.qgv.clear()
        scene = self._main_controller.activeScene
        if scene:
            for scene_element in scene.elements:
                self.qgv.addWidget(self.qgv.engine.graph, scene_element, delete_callback=self.delete_element)
            events_list = scene.getEvents()
            for event in events_list:
                event_id, fr_id, to_id = event
                fr_node = self.qgv.getNodeFromID(fr_id)
                to_node = self.qgv.getNodeFromID(to_id)
                self.qgv.addEdge(fr_node, to_node, {"width":2, "event_id": event_id})
        self.qgv.build()

    def new_edge_being_added(self, source, dest):
        source_id = source.widget.scene_element.itemID
        dest_id = dest.widget.scene_element.itemID
        if self._main_controller.testNewEventForCycle(source_id, dest_id):
            self._main_controller.newSceneEvent(source_id, dest_id)
        else:
            print(f"Cannot create edge from {source} to {dest} as this creates a cycle which are not properly handled yet.")
        return False, {}

    def new_scene_item_added(self, item_id):
        self.qgv.addWidget(self.qgv.engine.graph, scene_element)

    # Events
    def node_selected(self, node):
        if(self.qgv.manipulation_mode==QGraphVizManipulationMode.Node_remove_Mode):
            node_id = node.widget.scene_element.itemID
            self._main_controller.delSceneItem(node_id)
        else:
            print("Node selected {}".format(node))

    def edge_selected(self, edge):
        if(self.qgv.manipulation_mode==QGraphVizManipulationMode.Edge_remove_Mode):
            event_id = edge.kwargs["event_id"]
            self._main_controller.delSceneEvent(event_id)
        else:
            print("Edge selected {}".format(edge))

    def delete_element(self, item_id):
        self._main_controller.delSceneItem(item_id)

    def node_invoked(self, node):
        print("Node double clicked")
    def edge_invoked(self, node):
        print("Edge double clicked")
    def node_removed(self, node):
        print("Node removed")
        pass
    def edge_removed(self, edge):
        pass
        
    def manipulate(self):
        self.qgv.manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode

    def save(self):
        fname = QFileDialog.getSaveFileName(self.qgv, "Save", "", "*.json")
        if(fname[0]!=""):
            self.qgv.saveAsJson(fname[0])

        #fname = QFileDialog.getSaveFileName(self.qgv, "Save", "", "*.gv")
        #if(fname[0]!=""):
        #    self.qgv.save(fname[0])
        
    def new(self):
        self.qgv.engine.graph = Graph("MainGraph")
        self.qgv.build()
        self.qgv.repaint()

    def load(self):
        fname = QFileDialog.getOpenFileName(self.qgv, "Open", "", "*.json")
        if(fname[0]!=""):
            self.qgv.loadAJson(fname[0])

        #fname = QFileDialog.getOpenFileName(self.qgv, "Open", "", "*.gv")
        #if(fname[0]!=""):
        #    self.qgv.load_file(fname[0])

    def add_widget(self, scene_element):
        self.qgv.addWidget(self.qgv.engine.graph, scene_element)
        self.qgv.build()

    def add_node(self):
        dlg = QDialog()
        dlg.ok=False
        dlg.node_name=""
        dlg.node_label=""
        dlg.node_type="None"
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leNodeName = QLineEdit()
        leNodeLabel = QLineEdit()
        cbxNodeType = QComboBox()
        leImagePath = QLineEdit()

        pbOK = QPushButton()
        pbCancel = QPushButton()

        cbxNodeType.addItems(["None","circle","box"])
        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
        l.setWidget(0, QFormLayout.FieldRole, leNodeName)
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
        l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
        l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
        l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
        l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
        l.setWidget(3, QFormLayout.FieldRole, leImagePath)

        def ok():
            dlg.OK=True
            dlg.node_name = leNodeName.text()
            dlg.node_label = leNodeLabel.text()
            if(leImagePath.text()): 
                dlg.node_type = leImagePath.text()
            else: 
                dlg.node_type = cbxNodeType.currentText()
            dlg.close()

        def cancel():
            dlg.OK=False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        #node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
        if dlg.OK and dlg.node_name != '':
                self.qgv.addNode(self.qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
                self.qgv.build()

    def rem_node(self):
        self.qgv.manipulation_mode=QGraphVizManipulationMode.Node_remove_Mode

    def rem_edge(self):
        self.qgv.manipulation_mode=QGraphVizManipulationMode.Edge_remove_Mode

    def add_edge(self):
        self.qgv.manipulation_mode=QGraphVizManipulationMode.Edges_Connect_Mode

    def add_subgraph(self):
        dlg = QDialog()
        dlg.ok=False
        dlg.subgraph_name=""
        dlg.subgraph_label=""
        dlg.subgraph_type="None"
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leSubgraphName = QLineEdit()
        leSubgraphLabel = QLineEdit()

        pbOK = QPushButton()
        pbCancel = QPushButton()

        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Subgraph Name"))
        l.setWidget(0, QFormLayout.FieldRole, leSubgraphName)
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Subgraph Label"))
        l.setWidget(1, QFormLayout.FieldRole, leSubgraphLabel)

        def ok():
            dlg.OK=True
            dlg.subgraph_name = leSubgraphName.text()
            dlg.subgraph_label = leSubgraphLabel.text()
            dlg.close()

        def cancel():
            dlg.OK=False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        if dlg.OK and dlg.subgraph_name != '':
                self.qgv.addSubgraph(self.qgv.engine.graph, dlg.subgraph_name, subgraph_type= GraphType.SimpleGraph, label=dlg.subgraph_label)
                self.qgv.build()

    def rem_subgraph(self):
        self.qgv.manipulation_mode=QGraphVizManipulationMode.Subgraph_remove_Mode
        for btn in self.buttons_list:
            btn.setChecked(False)
        btnRemSubGraph.setChecked(True)
