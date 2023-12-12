import logging
import os
import shutil
import sys
from rucio.client.replicaclient import ReplicaClient
import rucio.common.utils as utils

logging.basicConfig(level=logging.DEBUG)


class Replica:
    def replica_file(rse, scope, name, data_file, sidecar_file, pfn=None):
        with open(sidecar_file, 'r') as f:
            sidecar = f.readline()
    
        self.replica(rse, scope, data_file, sidecar, pfn=None):

    def replica(rse, scope, name, data_file, sidecar, pfn=None):
        stats = os.stat(data_file)
        size = stats.st_size
        adler32 = utils.adler32(data_file)
    
        meta = {'rubin_butler': 1, 'rubin_sidecar': sidecar}
    
        rpc = ReplicaClient()
        x = rpc.add_replica(rse=rse, scope=scope, name=name, bytes_=size, adler32=adler32, meta=meta, pfn=pfn)
        return f"{scope}:{name}"
