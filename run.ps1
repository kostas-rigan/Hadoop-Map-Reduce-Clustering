For($i=0;$i -le 10; $i++) {
    Write-Host "Hello world"
}
python mapper.py | python reducer.py