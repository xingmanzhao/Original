<?php

function inverse($x)
{
    if (!$x) {
        throw new Exception("Division by zero.", 501);
    }

    return 1 / $x ;
}

try {
    echo inverse(5) . "\n";
    echo inverse(0) . "\n";
} catch (Exception $x) {
    echo "catch error", $x->getMessage(), $x->getCode(), "\n";
} finally {
    echo "First finally.\n";
}

echo "Hello World \n";
