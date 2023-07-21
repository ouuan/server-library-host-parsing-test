<?php

function handleRequest($request)
{
    header("Content-Type: text/plain");
    $host = $request['HTTP_HOST'] ?? 'undefined';
    echo "[$host]";
}

handleRequest($_SERVER);
