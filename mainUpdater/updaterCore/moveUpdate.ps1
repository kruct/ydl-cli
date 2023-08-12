$filePath = ".\latestUpdate.zip"
$parentFolder = Split-Path $filePath -Parent
Move-Item $filePath "$parentFolder\"
