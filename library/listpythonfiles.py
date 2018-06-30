
import os

files = os.walk(r"e:\classroom\python\june11\demo")

for  (dn,dl,fl) in files:
    if dn.find(".git") >= 0:  # ignore folders related to git
        continue
    print("Directory : ", dn)
    print("Files %d, directories %d" % (len(fl), len(dl)))
    for f in fl:
        if f.endswith(".py"):
            print(f)

