$currentPath = (Get-Item .).FullName  # get current path
New-Item "temp" -ItemType Directory > $null  # create a new temporary folder silently
Copy-Item $currentPath\centers.txt -Destination $currentPath\temp\centers.txt  # create a copy of the original centers to the temporary folder
$hadoopStreamingPath = -join($env:HADOOP_HOME, "\share\hadoop\tools\lib\hadoop-streaming-3.4.0.jar")  # you must set up HADOOP_HOME environment variable before running this script

$continueLoop = $true  # Boolean variable to control the loop
$cnt = 0

while ($continueLoop) {
    Copy-Item $currentPath\temp\centers.txt -Destination $currentPath\temp\old_centers.txt  # create a copy of the current centers as old centers
    hadoop jar $hadoopStreamingPath -file centers.txt -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input ./data.txt -output "/MapReduce/mapreduce_output$cnt"  # run map reduce job
    hadoop fs -copyToLocal "/MapReduce/mapreduce_output$cnt/part_00000" centers.txt  # get a copy to local
    $convergenceResult = py checker.py  # check for convergence
    if ($convergenceResult -eq "Converged") {
        Write-Host "Converged. Exiting loop."
        $continueLoop = $false  # Set the loop control variable to false to exit the loop
    }
    $cnt += 1
}

Remove-Item -path $currentPath\temp -Recurse  # delete the temporary folder

