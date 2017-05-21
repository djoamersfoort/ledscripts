<?php

const LIGHT_COUNT = 10;
const FADE_DURATION = 10;
const PI2 = 6.2831853071796; // Eh
const LIGHTS_ON = 3;

define('COVERED_PERCENTILE', 1 - LIGHTS_ON / (LIGHT_COUNT * .5));

function determine($node)
{
    $timePosition = microtime(true) / LIGHT_COUNT * PI2;
    $nodePosition = ($node / LIGHT_COUNT) * PI2;

    $nodeIntensity = cos($timePosition - $nodePosition) - COVERED_PERCENTILE;
    return max(0, $nodeIntensity / (1 - COVERED_PERCENTILE));
}

function color($red, $green, $blue)
{
    return decbin(sprintf('%03d%03d%03d', $red, $green, $blue));
}

$x = time() + FADE_DURATION;

$fp = fopen('php://stdout', 'wb');
if (!$fp) {
    die();
}

while ($x > time()) {
    for ($i = 0; $i < LIGHT_COUNT; $i++) {
        $mul = determine($i);

        fwrite($fp, color($mul * 24, $mul * 15, $mul * 117), 24);
        break;
    }
    break;
}
