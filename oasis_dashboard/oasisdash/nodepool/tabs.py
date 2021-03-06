# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs
from horizon.utils import functions as utils

from oasis_dashboard.oasisdash.nodepool.nodepool import tables as nodepool_tables
from oasis_dashboard.oasisdash.nodepool.policy import tables as policy_tables

from oasis_dashboard.api import oasis

import logging
LOG = logging.getLogger(__name__)


class PolicyTab(tabs.TableTab):
    table_classes = (policy_tables.NodePoolPolicyTable,)
    name = _("NodePool Policy")
    slug = "nodepoolpolicytab"
    template_name = "horizon/common/_detail_table.html"

    def get_policy_data(self):

        request = self.tab_group.request
        policies = oasis.node_pool_policy_list(request)
        return policies


class NodePoolTab(tabs.TableTab):
    table_classes = (nodepool_tables.NodePoolTable,)
    name = _("NodePool")
    slug = "nodepooltab"
    template_name = "horizon/common/_detail_table.html"

    def get_nodepool_data(self):

        request = self.tab_group.request
        nodepools = oasis.node_pool_list(request)
        LOG.debug('**************************************')
        LOG.debug(nodepools)
        return nodepools


class NodePoolTabs(tabs.TabGroup):
    slug = "nodepooltabs"
    tabs = (PolicyTab, NodePoolTab,)
    sticky = True
