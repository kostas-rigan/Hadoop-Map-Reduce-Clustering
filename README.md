<h1>MapReduce Clustering</h1>

# Contents
* [Description](#Description)
    * [Overview](#Overview)
    * [Files](#Files)
    * [Usage](#Usage)
* [Guidelines](#Guidelines)
* [Authors](#Authors)

# Description <a class="anchor" id="Description"></a>
## Overview <a class="anchor" id="Overview"></a>
This project implements a map-reduce clustering algorithm using Python scripts (`mapper.py` and `reducer.py`) controlled by a PowerShell script (`run.ps1`). Additionally, a convergence checker script (`checker.py`) is provided to verify convergence of the clustering algorithm.

## Files <a class="anchor" id="Files"></a>

### 1. `mapper.py`
- **Purpose:** Performs the mapping step in the map-reduce clustering algorithm.
- **Functionality:** 
  - Loads cluster centers from `temp/centers.txt`.
  - Calculates distances between points in `data.txt` and cluster centers.
  - Assigns each point to its closest cluster center.
  - Writes the results to `temp/temp_points_cluster.txt`.

### 2. `reducer.py`
- **Purpose:** Performs the reducing step in the map-reduce clustering algorithm.
- **Functionality:** 
  - Reads data from standard input.
  - Calculates new cluster centers based on the mean of points assigned to each cluster.
  - Prints the new cluster centers to standard output.

### 3. `run.ps1`
- **Purpose:** Controls the execution of the map-reduce clustering algorithm.
- **Functionality:** 
  - Creates a temporary directory `temp`.
  - Runs the map-reduce job for a specified number of iterations.
  - Checks for convergence using `checker.py` after each iteration.
  - Stops the execution if convergence is detected.
  - Deletes the temporary directory after completion.

### 4. `checker.py`
- **Purpose:** Checks for convergence between old and new cluster centers.
- **Functionality:** 
  - Compares old and new cluster center coordinates.
  - Determines convergence based on a specified tolerance level.
  - Prints "Converged" or "Not Converged" accordingly.

## Usage <a class="anchor" id="Usage"></a>
1. Place `mapper.py`, `reducer.py`, `checker.py`, `map_reduce_control.ps1`, `centers.txt`, and `data.txt` in the same directory.
2. Run `map_reduce_control.ps1` using PowerShell.
3. Monitor the output for convergence status.


# Guidelines<a class="anchor" id="Guidelines"></a>
- Execute the command `run.ps1` on a PowerShell

# Authors<a class="anchor" id="Authors"></a>
> Konstantinos Riganas, Student<br />
> Department of Management Science and Technology <br />
> Athens University of Economics and Business <br />
> t8200120@aueb.gr

> Nikolaos Nikolaidis, Student<br />
> Department of Management Science and Technology <br />
> Athens University of Economics and Business <br />
> t8200120@aueb.gr
