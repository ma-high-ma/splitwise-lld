from services.split.equal import SplitEqualService
from services.split.exact import SplitExactService
from services.split.percent import SplitPercentService


class SplitByTypeResolver:
    split_service_by_type_mapping = {
        "equal": SplitEqualService,
        "exact": SplitExactService,
        "percent": SplitPercentService
    }
    @classmethod
    def get_obj(cls, split_type):
        try:
            split_type_class = cls.split_service_by_type_mapping[split_type]
            return split_type_class
        except KeyError:
            raise KeyError
