import eel

eel.init("web")

# ------------------------
# Test work code project
# @eel.expose
# def call_in_js(x):
#     print(x)

# eel.call_in_pyhton("e")

# a = '1index.html'

# ------------------------

@eel.expose
def recv_data(login, password):
    print (login, password)



eel.start('1index.html', size=(500, 500))