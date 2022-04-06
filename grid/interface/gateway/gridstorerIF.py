from base.interface.gateway.basestorerIF import DataStorerIF


class InterpStorerIF(DataStorerIF):
    @classmethod
    def from_dir(cls, dir: str, name: str="interp"):
        super().from_dir(cls, dir, name, ".pickle")
