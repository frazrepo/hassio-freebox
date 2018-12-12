import json
import argparse
from pathlib import Path

# Usage : python config_builder.py /data/options/json
class ConfigBuilder:
    def __init__(self, config, options):
        self.config = config
        self.options = options

    def set_option(self, option_name, category=None, sub_category=None):
        if self.options.get(option_name, None) is not None:
            if category:
                if self.config.get(category, None) is None:
                    self.config[category] = dict()
                    if sub_category:
                        if self.config[category].get(sub_category, None) is None:
                            self.config[category][sub_category] = dict()
                if sub_category:
                    self.config[category][sub_category][option_name] = self.options[
                    option_name]
                else:
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
    
    # Check if config file exists
    if Path(config_path).is_file():  
        print("[fbx-addon] Freebox Assistant Plugin Configuration file found...")
        print("[fbx-addon] Values will be updated from add-on configuration")
        with open(config_path) as f:
            config = json.load(f)

    with open(options_path) as f:
        print("[fbx-addon] Reading add-on configuration datas...")
        options = json.load(f)

    cfg = ConfigBuilder(config, options)

    # Freebox Assistant Plugins Options
    cfg.set_option('pushbullet_token', 'main')
    cfg.set_option('code_telecommande', 'plugins', 'freebox')
    cfg.set_option('search_path', 'plugins', 'freebox')
    cfg.set_option('use_Mon_Bouquet', 'plugins', 'freebox')
    cfg.set_option('box_to_control', 'plugins', 'freebox')

    config_path = 'configuration.json'
    cfg.dump(config_path)

    print('[fbx-addon] Configuration written to {}'.format(config_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Construct an appropriate json configuration file for freebox assistant plugin')
    parser.add_argument('options_path', type=str)
    args = parser.parse_args()
    main(args.options_path)
