SEGUNDOS = 0
MINUTOS = 0
horas_am = 0
HORAS_pm = 0

def on_forever():
    global SEGUNDOS, horas_am, MINUTOS, HORAS_pm
    SEGUNDOS = SEGUNDOS + 1
    if MINUTOS == 59 and SEGUNDOS == 59:
        horas_am = horas_am + 1
        MINUTOS = 0
        if horas_am == 12 and SEGUNDOS > 59:
            HORAS_pm = 1
            horas_am = 0
    if SEGUNDOS == 59:
        SEGUNDOS = 0
        MINUTOS = MINUTOS + 1
basic.forever(on_forever)
