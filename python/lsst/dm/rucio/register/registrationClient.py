import logging
import os
import shutil
import sys
from rucio.client.replicaclient import ReplicaClient
import rucio.common.utils as utils

logging.basicConfig(level=logging.DEBUG)


class RegistrationClient(ReplicaClient):
    def register_file(self, rse, scope, name, data_file, sidecar_file, pfn=None):
        with open(sidecar_file, 'r') as f:
            sidecar = f.readlines()

        sidecar_json = ''.join(sidecar)
    
        return self.replica_json(rse, scope, data_file, sidecar_json, pfn=None):
        

    def register_json(self, rse, scope, name, data_file, sidecar, pfn=None):
        stats = os.stat(data_file)
        size = stats.st_size
        adler32 = utils.adler32(data_file)
    
        meta = {'rubin_butler': 1, 'rubin_sidecar': sidecar}
    
        rpc = ReplicaClient()
        self.add_replica(rse=rse, scope=scope, name=name, bytes_=size, adler32=adler32, meta=meta, pn=pfn)
        return True

if __name__ == "__main__":
    rpc = RegistrationClient()

    filename = sys.argv[1]

    name = filename.split('.')[0]
    data_file = f"{name}.fits"
    sidecar_file = f"{name}.json"

    rse = "XRD1"
    scope = "test"
    named_file = f"srp/data/{data_file}"

    x = rpc.register_file(rse=rse, scope=scope, name=named_file, data_file=data_file, sidecar_file=sidecar_file, pfn=f"root://xrd1:1094//rucio/test/{named_file}")
    print(x)

