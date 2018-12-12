import json
import argparse
from pathlib import Path
import yaml

class ConfigBuilder:
    def __init__(self, config, options):
        self.config = config
        self.options = options

    def set_option(self, option_name, category=None):
        if self.options.get(option_name, None) is not None:
            if category:
                if self.config.get(category, None) is None:
                    self.config[category] = dict()
                self.config[category][option_name] = self.options[
                    option_name]
            else:
                    self.config[option_name] = self.options[option_name]

    def dump(self, config_path):
        with open(config_path, 'w') as f:
            json.dump(self.config, f)

def main(options_path):

    config = dict()
    config_path = 'configuration.json'
    if Path(config_path).is_file():  # check if config file exists
        print("[Info] Freebox Assistant Plugin Configuration file found...")
        print("[Info] Values will be updated from add-on configuration")
        with open(config_path) as f:
            config = json.load(f)

    with open(options_path) as f:
        print("[Info] Reading add-on configuration datas...")
        options = json.load(f)

    cfg = ConfigBuilder(config, options)

    cfg.set_option('main')
    cfg.set_option('plugins')

    config_path = 'configuration.json'
    cfg.dump(config_path)

    print('[Info] Configuration written to {}'.format(config_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Construct an appropriate json configuration file for freebox assistant plugin')
    parser.add_argument('options_path', type=str)
    args = parser.parse_args()
    main(args.options_path)
