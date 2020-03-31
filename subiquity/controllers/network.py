# Copyright 2019 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from subiquitycore.controllers.network import NetworkController

from subiquity.controller import SubiquityController


class NetworkController(NetworkController, SubiquityController):

    autoinstall_key = "network"
    autoinstall_schema = {
        'type': 'object',
        'properties': {
            'version': {
                'type': 'integer',
                'minimum': 2,
                'maximum': 2,
                },
            'ethernets': {'type': 'object'},
            'wifis': {'type': 'object'},
            'bridges': {'type': 'object'},
            'bonds': {'type': 'object'},
            'tunnels': {'type': 'object'},
            'vlans': {'type': 'object'},
            },
        }

    def done(self):
        self.configured()
        super().done()

    def make_autoinstall(self):
        return self.model.render()['network']
