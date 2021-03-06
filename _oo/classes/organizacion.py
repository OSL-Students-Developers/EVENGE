# -*- coding: utf-8 -*-
#Evenge - gestor de eventos (events management)
#Copyright (C) 2014 - desarrollo.evenge@gmail.com
#Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

import webapp2
from google.appengine.ext import ndb
from datetime import datetime
from invitacion import Invitacion

class Organizacion(ndb.Model):
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    idCreador = ndb.StringProperty()
    telefono = ndb.StringProperty()
    fecha = ndb.DateProperty(auto_now_add=True)
    twitter = ndb.StringProperty()
    web = ndb.StringProperty()
    usuarios = ndb.StringProperty(repeated=True)
    eventos = ndb.StringProperty(repeated=True)
    ponentes = ndb.StringProperty(repeated=True)
    invitaciones = ndb.StructuredProperty(Invitacion, repeated=True)
  
    def getKey(self):
        return str(self.key.id())
