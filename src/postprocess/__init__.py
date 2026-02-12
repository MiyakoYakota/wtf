import os
import pkgutil
import importlib
from utils.logs import get_logger

logger = get_logger(__name__) # will show postprocess in log

class LazyProcRegistry:
    def __init__(self, package_path, package_name):
        self.package_path = package_path
        self.package_name = package_name
        self._processors = {}
        self._discovered = False
        logger.info(f"LazyProcRegistry for {package_name}")

    def _discover(self):
        # replace file splitting .py with pkutil.iter_modules. its quicker
        if self._discovered:
            return
        for _, name, is_pkg in pkgutil.iter_modules([self.package_path]):
            if name != 'postprocessors' and not is_pkg: # skip self file
                self._processors[name] = None
        self._discovered = True
        # logger.info(f"")
        # this would be annoyingly verbose so uncomment if you want

    def items(self):
        self._discover()
        for name in list(self._processors.keys()):
            yield name, self.get(name)

    def get(self, name):
        # lazy loading
        if name not in self._processors:
            return None
        
        if self._processors[name] is None:
            try:
                module_path = f"{self.package_name}.{name}"
                module = importlib.import_module(module_path)
                # Look for the 'extract' function you defined earlier
                func = getattr(module, 'extract', None)
                if callable(func):
                    self._processors[name] = func
                else:
                    logger.warning(f"No 'extract' function in {name}")
            except Exception as e:
                logger.error(f"Failed to load postprocessor {name}: {e}")
        
        return self._processors[name]

# registry instance init
postprocessors = LazyProcRegistry(os.path.dirname(__file__), "postprocess")