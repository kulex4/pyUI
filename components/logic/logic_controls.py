"""
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2010 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
"""

import suit.core.render.engine as render_engine
import suit.core.render.mygui as mygui
import suit.core.kernel as core
import sc_core.pm as sc
from components.logic.logic2sc import TranslatorLogic2Sc
from suit.core.objects import ObjectOverlay
import logic_viewer

class EditPanel(ObjectOverlay):
    
    def __init__(self):
        ObjectOverlay.__init__(self)
        
        self.width = 550
        self.height = 100
        self.viewer = logic_viewer.TextViewer()

        self._widget = render_engine.Gui.createWidgetT("Window", "Panel",
                            mygui.IntCoord( (render_engine.Window.width) / 2 - (self.width) / 2,
                                             render_engine.Window.height - self.height,
                                             self.width, self.height),
                            mygui.Align())
        self.setVisible(False)

        self.infoText = self._widget.createWidgetT("Edit", "Edit",
                            mygui.IntCoord(15, 15, self.width - 30, self.height - 30),
                            mygui.Align())
        self.infoText.setCaption("Logic Edit Panel")
        self.setVisible(True)
        self.setEnabled(True)


        self.button = self._widget.createWidgetT("Button", "Button",
                            mygui.IntCoord(self.width-100, self.height-45, 80, 25),
                            mygui.Align())
        self.button.subscribeEventMouseButtonClick(self, 'textAccept')
        self.button.setCaption("Enter")
        self.button.setVisible(True)
        self.button.setEnabled(True)
        
        # flag to update information
        self.needInfoUpdate = False
    
    def __del__(self):
        ObjectOverlay.__del__(self)
    
    def delete(self):
        ObjectOverlay.delete(self)
        self.viewer.delete()

    def textAccept(self, _widget):
        translator = TranslatorLogic2Sc()
        kernel = core.Kernel.getSingleton()
        session = kernel.session()
        segment = kernel.segment()

        def_node = session.create_el_idtf(segment, sc.SC_CONST, "root_logic_node")

        #FIXME input parameters to translator
        #translator.translate_impl(self.getText(), def_node[1])


    def getText(self):
        return self.infoText.getCaption()
        
    def update(self):
        self.needInfoUpdate = True
    
    def _updateView(self):
        ObjectOverlay._updateView(self)
        #TODO update