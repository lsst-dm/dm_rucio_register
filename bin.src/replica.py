from lsst.dm.replica impore Replica
if __name__ == "__main__":

    filename = sys.argv[1]

    name = filename.split('.')[0]
    data_file = f"{name}.fits"
    sidecar_file = f"{name}.json"

    rse = "XRD1"
    scope = "test"

    x = Replica.replica(rse=rse, scope=scope, data_file=data_file, sidecar_file=sidecar_file, pfn=f"root://xrd1:1094//rucio/test/srp/data/{data_file}")
    print(x)

