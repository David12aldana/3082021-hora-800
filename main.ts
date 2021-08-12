let SEGUNDOS = 0
let MINUTOS = 0
let HORAS_pm = 0
basic.forever(function () {
    SEGUNDOS = SEGUNDOS + 1
    if (SEGUNDOS == 10) {
        MINUTOS = MINUTOS + 1
        SEGUNDOS = 1
    }
    if (MINUTOS == 10) {
        HORAS_pm = HORAS_pm + 1
        MINUTOS = 0
    }
})
basic.forever(function () {
	
})
