import refrom yaml import load, FullLoaderfrom collections.abc import Mappingclass Content(Mapping):    __delimeter = "^(?:-|\+){3}\s*$"    __regex = re.compile(__delimeter, re.MULTILINE)        @classmethod    def load(self, cls, string):        _, fm, content = self.__regex.split(string, 2)        load(fm, Loader=FullLoader)        return cls(metadata, content)        def __init__(self, metadata, content):        self.data = metadata        self.data["content"] = content            @property     def body(self):        return self.data["content"]            @property    def type(self):        if "type" in self.data:            return self.data["type"]        else:            return None            def set_type(self, new_type):        self.data["type"] = new_type            def __getitem__(self, k):        return self.data[k]            def __iter__(self):        self.data["__iter"]            def __len__(self):        len(self.data)            def __repr__(self):        data = dict()        return str(data)    