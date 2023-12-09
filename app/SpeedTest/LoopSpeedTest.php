<?php

function Test_01($aArr, $aFind) {
    $Res = 0;
    $i = 0;
    while ($i < count($aArr)) {
        if ($aArr[$i] == $aFind) {
            $Res += 1;
        }
        $i += 1;
    }
    return $Res;
}

function Test_02($aArr, $aFind) {
    $Arr = array_filter($aArr, function ($a) use ($aFind) {
        return $a == $aFind;
    });
    return count($Arr);
}

function Test_03($aArr, $aFind) {
    $Res = 0;
    foreach ($aArr as $a) {
        if ($a == $aFind) {
            $Res += 1;
        }
    }
    return $Res;
}

function Test_04($aArr, $aFind) {
    $Res = array_count_values($aArr)[$aFind] ?? 0;
    return $Res;
}

function SpeedFunc($aFunc, $aArr, $aFind, $aCount) {
    $Start = microtime(true);
    for ($a = 0; $a < $aCount; $a++) {
        $Res = $aFunc($aArr, $aFind);
    }
    printf("Method: %s, Time: %0.2f, Found: %d\n", $aFunc, microtime(true) - $Start, $Res);
}

function SpeedAll($aArr, $aFind, $aCount) {
    echo PHP_EOL;
    echo "php ver " . phpversion() . PHP_EOL;

    $Start = microtime(true);
    $Methods = ['Test_01', 'Test_02', 'Test_03', 'Test_04'];
    foreach ($Methods as $Method) {
        SpeedFunc($Method, $aArr, $aFind, $aCount);
    }
    printf("Total: %0.2f\n", microtime(true) - $Start);
}

function DTimer($aFunc) {
    return function ($aArr, $aFind) use ($aFunc) {
        $Start = microtime(true);
        $Count = 1 * 1000000;
        for ($a = 0; $a < $Count; $a++) {
            $Res = $aFunc($aArr, $aFind);
        }
        printf("Method: %s, Time: %0.2f, Found: %s\n", $aFunc, microtime(true) - $Start, $Res);
    };
}

$Arr1 = array_map(function () {
    return rand(1, 10);
}, range(1, 100));

SpeedAll($Arr1, 3, 1 * 1000000);
// Test_04_Decor($Arr1, 3);
?>
