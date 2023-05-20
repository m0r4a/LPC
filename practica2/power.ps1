$miVariable = "Bison"

if ($miVariable -eq "Bison") {
    Write-Host "La variable es igual a 'Bison'"
} else {
    Write-Host "La variable no es igual a 'Bison'"
}

for ($i = 1; $i -le 5; $i++) {
    Write-Host "Iteración $i"
}

function Saludar($nombre) {
    Write-Host "¡Hola, $nombre!"
}

Saludar "Juan"

