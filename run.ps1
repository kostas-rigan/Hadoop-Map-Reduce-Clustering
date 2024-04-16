$currentPath = (Get-Item .).FullName
New-Item "temp" -ItemType Directory > $null
For($i=0;$i -le 10; $i++) {
    Write-Host "Hello world"
}
python mapper.py | python reducer.py
Remove-Item -path $currentPath\temp -Recurse