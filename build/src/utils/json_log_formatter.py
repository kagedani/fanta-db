import json
import logging
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def format(self, record):
        extra = getattr(record, "__dict__", {})
        json_record = {
            "datetime": str(datetime.now()),
            "level": getattr(record, "levelname", None),
            "source": getattr(record, "filename", None),
            "line": getattr(record, "lineno", None),
            "msg": getattr(record, "msg", None),
            "additional_detail": extra.get("additional_detail"),
        }
        return json.dumps(json_record)
