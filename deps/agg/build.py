#
# This file is part of Mapnik (c++ mapping toolkit)
#
# Copyright (C) 2013 Artem Pavlenko
#
# Mapnik is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# 

import os
from glob import glob

Import('env')

agg_env = env.Clone()

cxxflags = env['CUSTOM_CXXFLAGS'] + ' -O%s -fPIC -DNDEBUG' % env['OPTIMIZATION']

agg_env.StaticLibrary('agg', glob('./src/' + '*.cpp'), LIBS=[], CXXFLAGS=cxxflags, LINKFLAGS=env['CUSTOM_LDFLAGS'])