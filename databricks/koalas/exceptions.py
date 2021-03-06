#
# Copyright (C) 2019 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Exceptions/Errors used in Koalas.
"""


class SparkPandasIndexingError(Exception):
    pass


def code_change_hint(pandas_function, spark_target_function):
    if pandas_function is not None and spark_target_function is not None:
        return "You are trying to use pandas function {}, use spark function {}" \
               .format(pandas_function, spark_target_function)
    elif pandas_function is not None and spark_target_function is None:
        return ("You are trying to use pandas function {}, checkout the spark "
                "user guide to find a relevant function").format(pandas_function)
    elif pandas_function is None and spark_target_function is not None:
        return "Use spark function {}".format(spark_target_function)
    else:   # both none
        return "Checkout the spark user guide to find a relevant function"


class SparkPandasNotImplementedError(NotImplementedError):

    def __init__(self, pandas_function=None, spark_target_function=None, description=""):
        self.pandas_source = pandas_function
        self.spark_target = spark_target_function
        hint = code_change_hint(pandas_function, spark_target_function)
        if len(description) > 0:
            description += " " + hint
        else:
            description = hint
        super(SparkPandasNotImplementedError, self).__init__(description)


class PandasNotImplementedError(NotImplementedError):

    def __init__(self, class_name, method_name=None, arg_name=None, property_name=None):
        assert (method_name is None) != (property_name is None)
        self.class_name = class_name
        self.method_name = method_name
        self.arg_name = arg_name
        if method_name is not None:
            if arg_name is not None:
                msg = "The method `{0}.{1}()` does not support `{2}` parameter" \
                    .format(class_name, method_name, arg_name)
            else:
                msg = "The method `{0}.{1}()` is not implemented yet." \
                    .format(class_name, method_name)
        else:
            msg = "The property `{0}.{1}` is not implemented yet." \
                .format(class_name, property_name)
        super(NotImplementedError, self).__init__(msg)


class SparkPandasMergeError(Exception):
    pass
