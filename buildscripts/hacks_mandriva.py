
import os

def insert( env , options ):
    if os.path.exists( "/usr/include/js-1.70/" ):
        env.Append( CPPDEFINES=[ "LIBJS" ] )
        print('Append LIBJS')

