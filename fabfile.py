#---------------------------
# Credit: Asfak Mahamud
#---------------------------
from fabric.api import *
import yaml
import os

OUR_CONFIG_FILE = 'host_config.yaml' 

our_env = None
our_user = None
our_host = None
our_host_config = yaml.load(open(OUR_CONFIG_FILE, "r"))

def prodhost():
    """Sets host config to 'remote'.
    """
    _host("prod")

def devhost():
    """Sets host config to 'dev'.
    """
    _host("dev")

def localhost():
    """Sets host config to 'local'.
    """
    _host("local")

def _host(the_host_string):
    global our_env, our_user, our_host
    our_env = the_host_string
    a_key_filename = None
    if the_host_string == 'local':
        our_user, our_host = os.environ.get('USER'), '127.0.0.1'
    else:
        our_user = our_host_config[our_env]['user']
        our_host = our_host_config[our_env]['host']
        a_key_filename = our_host_config[our_env]['key_file']
        
    env.host_string = our_host
    env.hosts = [
        our_host
    ]
    env.key_filename = a_key_filename
    env.user = our_user
    
def ls():
    global our_host, our_env
    if our_host is None or our_env not in ["prod", "dev"]:
        print "Please prefix with `fab prodhost` OR `fab devhost`"
        return
    run('ls')
    
def provision_machine():
    global our_host, our_env
    if our_host is None or our_env not in ["prod", "dev"]:
        print "Please prefix with `fab prodhost` OR `fab devhost`"
        return
    #### Code for provisioning remote host ####

def deploy():
    global our_host, our_env
    if our_host is None or our_env not in ["prod", "dev"]:
        print "Please prefix with `fab prodhost` OR `fab devhost`"
        return
    #### Code to deploy service in remote host ####
    pass