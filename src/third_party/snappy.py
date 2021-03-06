
def configure( env , fileLists , options ):

    myenv = env.Clone()
    if not options["windows"]:
        myenv.Append(CPPFLAGS=" -Wno-sign-compare -Wno-unused-function ") #snappy doesn't compile cleanly

    files = ["$BUILD_DIR/third_party/snappy/snappy.cc", "$BUILD_DIR/third_party/snappy/snappy-sinksource.cc"]

    fileLists["serverOnlyFiles"] += [ myenv.Object(f) for f in files ]

def configureSystem( env , fileLists , options ):
    env.Append( LIBS=[ "snappy" ] )
