$dnsCache = Get-DnsClientCache

if ($dnsCache) {
    Write-Host "Contenido caché de DNS:"
    foreach ($entry in $dnsCache) {
        Write-Host "Registro DNS: $($entry.RecordName)"
        Write-Host "Tipo de registro: $($entry.Type)"
        Write-Host "Dirección IP: $($entry.IPAddress)"
        Write-Host "Tiempo de vida (TTL): $($entry.TimeToLive.TotalSeconds) segundos"
        Write-Host "-----"
    }
} else {
    Write-Host "No se encontró información caché de DNS."
}
