import logging
import os
import shutil
import sys
from rucio.client.replicaclient import ReplicaClient
import rucio.common.utils as utils

logging.basicConfig(level=logging.DEBUG)


def replica(rse, scope, data_file, sidecar_file, pfn=None):
    stats = os.stat(data_file)
    bytes = stats.st_size
    adler32 = utils.adler32(data_file)

    with open(sidecar_file, 'r') as f:
        rubin_sidecar = f.readline()

    meta = {'rubin_butler': 1, 'rubin_sidecar': rubin_sidecar}

    rpc = ReplicaClient()
    name = f'srp/data/{data_file}'
    x = rpc.add_replica(rse=rse, scope=scope, name=name, bytes_=bytes, adler32=adler32, meta=meta, pfn=pfn)
    return f"{scope}:{name}"

if __name__ == "__main__":

    filename = sys.argv[1]

    name = filename.split('.')[0]
    data_file = f"{name}.fits"
    sidecar_file = f"{name}.json"

    rse = "XRD1"
    scope = "test"

    x = replica(rse=rse, scope=scope, data_file=data_file, sidecar_file=sidecar_file, pfn=f"root://xrd1:1094//rucio/test/srp/data/{data_file}")
    print(x)
