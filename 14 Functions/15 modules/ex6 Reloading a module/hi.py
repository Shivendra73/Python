#Reloading a module: If we want to reload a module, we have reload() function
#                    present within imp module

import hello
import imp

print("hi")
imp.reload(hello)
imp.reload(hello)
imp.reload(hello)
