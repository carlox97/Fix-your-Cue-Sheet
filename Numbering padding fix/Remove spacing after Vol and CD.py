import os

cds = ["CD1", "CD2", "CD3", "CD4", "CD5", "CD6", "CD7", "CD8", "CD9", "Cd1", "Cd2", "Cd3", "Cd4", "Cd5", "Cd6", "Cd7", "Cd8", "Cd9", "CD 1", "CD 2", "CD 3", "CD 4", "CD 5", "CD 6", "CD 7", "CD 8", "CD 9", "cd 1", "cd 2", "cd 3", "cd 4", "cd 5", "cd 6", "cd 7", "cd 8", "cd 9", "cd1", "cd2", "cd3", "cd4", "cd5", "cd6", "cd7", "cd8", "cd9"]
CD = ["CD01", "CD02", "CD03", "CD04", "CD05", "CD06", "CD07", "CD08", "CD09"]

vols = ["Vol.1", "Vol.2", "Vol.3", "Vol.4", "Vol.5", "Vol.6", "Vol.7", "Vol.8", "Vol.9", "vol.1", "vol.2", "vol.3", "vol.4", "vol.5", "vol.6", "vol.7", "vol.8", "vol.9", "Vol. 1", "Vol. 2", "Vol. 3", "Vol. 4", "Vol. 5", "Vol. 6", "Vol. 7", "Vol. 8", "Vol. 9", "vol. 1", "vol. 2", "vol. 3", "vol. 4", "vol. 5", "vol. 6", "vol. 7", "vol. 8", "vol. 9", ]
VOL = ["Vol.01", "Vol.02", "Vol.03", "Vol.04", "Vol.05", "Vol.06", "Vol.07", "Vol.08", "Vol.09"]

cwd = os.getcwd()

lenght = len(cds) - 1
lenghtv = len(vols) -1


for root, dirs, files in os.walk(cwd):
    for d in dirs:
        if "CD 1 " in d or "CD 2 " in d or "CD 3 " in d or "CD 4 " in d or "CD 5 " in d or "CD 6 " in d or "CD 7 " in d or "CD 8 " in d or "CD 9 " in d:
            new = d
            new = new.replace("CD ", "CD0")
            percorso = os.path.join(root, d)
            nuovo = os.path.join(root, new)
            print(nuovo)
            os.replace(percorso, nuovo)
        if "Vol. 1 " in d or "Vol. 2 " in d or "Vol. 3 " in d or "Vol. 4 " in d or "Vol. 5 " in d or "Vol. 6 " in d or "Vol. 7 " in d or "Vol. 8 " in d or "Vol. 9 " in d:
            new = d 
            new = new.replace("Vol. ", "Vol.0")
            percorso = os.path.join(root, d)
            nuovo = os.path.join(root, new)
            print(nuovo)
            os.replace(percorso, nuovo)            

