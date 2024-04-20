# checker.py

__authors__ = 'Nikolaos Nikolaidis and Konstantinos Riganas'

def check_convergence(old_centers_file, new_centers_file, tolerance=0.0001):
    with open(old_centers_file, 'r') as f_old, open(new_centers_file, 'r') as f_new:
        old_centers = [line.strip().split(',') for line in f_old if line.strip()]
        new_centers = [line.strip().split(',') for line in f_new if line.strip()]

    converged = all(
        all(abs(float(old_c[i]) - float(new_c[i])) < tolerance for i in range(len(old_c)))
        for old_c, new_c in zip(old_centers, new_centers)
    )
    
    if converged:
        print("Converged")
    else:
        print("Not Converged")

if __name__ == "__main__":
    old_centers_file = "temp/old_centers.txt"
    new_centers_file = "temp/centers.txt"
    check_convergence(old_centers_file, new_centers_file)
