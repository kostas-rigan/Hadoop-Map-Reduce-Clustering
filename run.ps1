$currentPath = (Get-Item .).FullName  # get current path
New-Item "temp" -ItemType Directory > $null  # create a new temporary folder silently
Copy-Item $currentPath\centers.txt -Destination $currentPath\temp\centers.txt  # create a copy of the original centers to the temporary folder
For($i=0;$i -le 10; $i++) {
    Copy-Item $currentPath\temp\centers.txt -Destination $currentPath\temp\old_centers.txt  # create a copy of the current centers as old centers
    Set-Content -Path $currentPath\temp\centers.txt -Value (python mapper.py | python reducer.py)  # simulate map reduce job and change the centers file
    Get-Content $currentPath\temp\centers.txt  # print the contents of the current centers
    # TODO: run a script that will check convergence and change the for loop into a while loop
}
Remove-Item -path $currentPath\temp -Recurse  # delete the temporary folder