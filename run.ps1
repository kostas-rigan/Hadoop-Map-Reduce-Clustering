$currentPath = (Get-Item .).FullName  # get current path
New-Item "temp" -ItemType Directory > $null  # create a new temporary folder silently
Copy-Item $currentPath\centers.txt -Destination $currentPath\temp\centers.txt  # create a copy of the original centers to the temporary folder

$continueLoop = $true  # Boolean variable to control the loop

while ($continueLoop) {
    Copy-Item $currentPath\temp\centers.txt -Destination $currentPath\temp\old_centers.txt  # create a copy of the current centers as old centers
    Set-Content -Path $currentPath\temp\centers.txt -Value (py mapper.py | py reducer.py)  # simulate map reduce job and change the centers file
    Get-Content $currentPath\temp\centers.txt  # print the contents of the current centers
    $convergenceResult = py checker.py  # check for convergence
    if ($convergenceResult -eq "Converged") {
        Write-Host "Converged. Exiting loop."
        $continueLoop = $false  # Set the loop control variable to false to exit the loop
    }
    # TODO: run a script that will check convergence and change the for loop into a while loop
}

Remove-Item -path $currentPath\temp -Recurse  # delete the temporary folder

