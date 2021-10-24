import os 
import getpass
import hashlib
  
if __name__=="__main__":
    #Get number of CPUs
    cpus_available = int(os.environ['SLURM_CPUS_PER_TASK'])

    #Get username
    username = getpass.getuser()

    #Create Hash Code
    hash_object = hashlib.md5(username.encode())

    #Result for webcampus is 
    print('Your result for the webCampus Quiz is:', username+'_'+str(cpus_available)+'_'+hash_object.hexdigest())

