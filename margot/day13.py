import numpy as np

name = "input"

summary = 0
summary_with_smudges = 0
with open("inputs/day13/{}.txt".format(name)) as file:
    check = True
    while check:
        valleydat = []
        line = next(file).rstrip()
        while any(line):
            valleydat.append(list(line))
            try:
               line = next(file).rstrip()
            except StopIteration:
               check = False
               break
        valleydat = np.array(valleydat)

        for i in range(1, valleydat.shape[0]//2+1):
            overlap_top = (valleydat[:i] == valleydat[2*i-1:i-1:-1])
            if np.all(overlap_top):
                summary += 100*i
                break

            overlap_bot = (np.flip(valleydat, axis=0)[:i] == np.flip(valleydat, axis=0)[2*i-1:i-1:-1])
            if np.all(overlap_bot):
                summary += 100*(valleydat.shape[0]-i)
                break

        for j in range(1, valleydat.shape[1]//2+1):
            overlap_top = (valleydat[:, :j] == valleydat[:, 2*j-1:j-1:-1])
            if np.all(overlap_top):
                summary += j
                break

            overlap_bot = (np.flip(valleydat, axis=1)[:, :j] == np.flip(valleydat, axis=1)[:, 2*j-1:j-1:-1])
            if np.all(overlap_bot):
                summary += valleydat.shape[1]-j
                break
                
        for i in range(1, valleydat.shape[0]//2+1):
            overlap_top = (valleydat[:i] == valleydat[2*i-1:i-1:-1])
            if np.sum(np.invert(overlap_top)) == 1:
                summary_with_smudges += 100*i
                break

            overlap_bot = (np.flip(valleydat, axis=0)[:i] == np.flip(valleydat, axis=0)[2*i-1:i-1:-1])
            if np.sum(np.invert(overlap_bot)) == 1:
                summary_with_smudges += 100*(valleydat.shape[0]-i)
                break

        for j in range(1, valleydat.shape[1]//2+1):
            overlap_top = (valleydat[:, :j] == valleydat[:, 2*j-1:j-1:-1])
            if np.sum(np.invert(overlap_top)) == 1:
                summary_with_smudges += j
                break

            overlap_bot = (np.flip(valleydat, axis=1)[:, :j] == np.flip(valleydat, axis=1)[:, 2*j-1:j-1:-1])
            if np.sum(np.invert(overlap_bot)) == 1:
                summary_with_smudges += valleydat.shape[1]-j
                break

print("Summary w/ regular mirrors (task 1):", summary)
print("Summary w/ smudged mirrors (task 2):", summary_with_smudges)