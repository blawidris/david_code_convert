<?php
// scan current working directory for files ending in .webloc, look inside it for first url,
// then try to run yt-dlp on that url.


function getUrl($file)
{
    $contents = file_get_contents($file);
    if (preg_match('#(https://[^<]+)#', $contents, $match))
        return $match[0] ? $match[0] : null;

    return false;
}

$files = scandir('.');
foreach ($files as $file)
    if (preg_match('#.+\.webloc$#i', $file) && $url = getUrl($file))
        echo system("/opt/homebrew/bin/yt-dlp" . escapeshellarg($url));
