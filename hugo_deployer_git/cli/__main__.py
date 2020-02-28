import toml
from ..deployer import Deployer
from ..check_env import check_env

def main():
  check_env()

  with open('config.toml', "r") as cfg_toml:
    config = toml.loads(cfg_toml.read())
  # print(config)
  dp = Deployer( config['deploy'], src_dir=".")
  dp.deploy()

if __name__ == "__main__":
  main()