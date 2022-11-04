from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\Users\\banda\\PycharmProjects\\BDD_POM\\ConfigurationData\\config.ini")
    return config.get(section, Key)