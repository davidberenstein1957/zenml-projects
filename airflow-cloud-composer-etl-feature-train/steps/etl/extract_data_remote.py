# Apache Software License 2.0
#
# Copyright (c) ZenML GmbH 2024. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import gcsfs
import pandas as pd
from zenml import step
from zenml.logger import get_logger

logger = get_logger(__name__)


@step
def extract_data_remote(data_path: str = "gs://yourpath") -> pd.DataFrame:
    """Extract data from remote source.

    Args:
        data_path: Loads data from remote storage. Defaults to "gs://yourpath".

    Returns:
        pd.DataFrame: Dataframe containing the data.
    """
    fs = gcsfs.GCSFileSystem()

    with fs.open(data_path, "r") as f:
        return pd.read_csv(f)
