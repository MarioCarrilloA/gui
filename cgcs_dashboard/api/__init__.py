#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cgcs_dashboard.api import ceilometer
from cgcs_dashboard.api import ceph
from cgcs_dashboard.api import dc_manager
from cgcs_dashboard.api import iservice
from cgcs_dashboard.api import patch
from cgcs_dashboard.api import sysinv
from cgcs_dashboard.api import vim


__all__ = [
    "ceilometer",
    "ceph",
    "dc_manager",
    "iservice",
    "patch",
    "sysinv",
    "vim",
]