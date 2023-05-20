#!/usr/bin/perl

use strict;
use warnings;

my $regripperPath = "/path/to/regripper/regripper.pl";
my $outputFile = "output.txt";
my $regKey = "HKEY_CURRENT_USER";

# Ejecutando RegRipper para analizar el registro de usuario y guardar el resultado en un archivo

my $command = "$regripperPath -r $regKey > $outputFile";

# Capturando el resultado de la ejecución

my $result = system($command);

if ($result == -1) {
    print "Error: Asegúrate de haber cambiado el path a RegRipper en el código.\n";
} elsif ($result >> 8) {
    print "Error: Se produjo un error durante la ejecución del análisis.\n";
} else {
    print "Análisis completado. El resultado se ha guardado en $outputFile.\n";
}

