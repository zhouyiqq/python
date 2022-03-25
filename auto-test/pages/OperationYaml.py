import yaml


class OperationYaml:
    def set_w_yaml(self, data, yamlpath):
        """
        以覆盖的方式写入yaml
        :param data: 写入进yml的内容
        :param yamlpath: yaml的文件路径
        :return:
        """
        with open(yamlpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)

    def set_a_yaml(self, data, yamlpath):
        """
        以追加的方式写入yaml
        :param data: 写入进yml的内容
        :param yamlpath: yaml的文件路径
        :return:
        """
        with open(yamlpath, 'a', encoding='utf-8') as f:
            yaml.dump(data, f)

    def get_yaml(self, yamlpath):
        """
        读取yaml
        :param yamlpath: yaml的文件路径
        :return: 返回从yamlpath文件中读取出来的内容
        """
        f = open(yamlpath, 'r', encoding='utf-8')
        f_result = f.read()
        result = yaml.load(f_result, Loader=yaml.FullLoader)
        return result