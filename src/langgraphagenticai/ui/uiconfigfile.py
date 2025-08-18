from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self._config = ConfigParser()
        self._config.read(config_file)

    def get_llm_options(self):
        return self._config.get("DEFAULT", "LLM_OPTIONS").split(", ")

    def get_usecase_options(self):
        return self._config.get("DEFAULT", "USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self._config.get("DEFAULT", "GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self._config.get("DEFAULT", "PAGE_TITLE")