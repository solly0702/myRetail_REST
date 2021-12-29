class Validator(object):
    def validate_type(self, element, desired_type):
        if desired_type == "integer":
            return type(element) == int
        elif desired_type == "string":
            return type(element) == str
        elif desired_type == "number":
            return type(element) == float or type(element) == int
        raise ValueError("Invalid value for desired type")

    def validateTypes(self, element, fields):
        for k in fields:
            if "type" in fields[k]:
                if not self.validate_type(element[k], fields[k]["type"]):
                    raise ValueError("Invalid type of field")
            else:
                self.validateTypes(element[k], fields[k])

        return True

    def validate(self, element, fields):
        return self.validateTypes(element, fields)
