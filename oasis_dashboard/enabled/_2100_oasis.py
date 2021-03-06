#  Copyright 2015 Cisco Systems.
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
from django.utils.translation import ugettext_lazy as _


DASHBOARD = 'oasisdash'
ADD_INSTALLED_APPS = [
    'oasis_dashboard',
    'oasis_dashboard.oasisdash'
]

DEFAULT = True
AUTO_DISCOVER_STATIC_FILES = True


ADD_JS_FILES = [
    'horizon/lib/angular/angular-route.js',
    'oasisdash/js/ui-ace.js',
    'oasisdash/js/ace.js',
    'oasisdash/js/mode-python.js',
    'oasisdash/js/theme-eclipse.js',
]

ADD_ANGULAR_MODULES = ['horizon.dashboard.oasisdash', 'ui.ace']

# ADD_EXCEPTIONS = {
#    'recoverable': exceptions.RECOVERABLE,
#    'not_found': exceptions.NOT_FOUND,
#    'unauthorized': exceptions.UNAUTHORIZED,
#}

