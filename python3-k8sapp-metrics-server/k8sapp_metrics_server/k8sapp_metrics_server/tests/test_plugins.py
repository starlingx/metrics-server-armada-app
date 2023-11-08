#
# Copyright (c) 2023 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

from k8sapp_metrics_server.common import constants as app_constants
from sysinv.tests.db import base as dbbase


class K8SAppMetricsServerAppMixin(object):
    app_name = app_constants.HELM_APP_METRICS_SERVER
    path_name = app_name + '.tgz'

    def setUp(self):  # pylint: disable=useless-parent-delegation
        super(K8SAppMetricsServerAppMixin, self).setUp()

    def test_stub(self):
        # Replace this with a real unit test.
        pass


# Test Configuration:
# - Controller
# - IPv6
# - Ceph Storage
# - metrics-server app
class K8sAppMetricsServerControllerTestCase(K8SAppMetricsServerAppMixin,
                                            dbbase.BaseIPv6Mixin,
                                            dbbase.BaseCephStorageBackendMixin,
                                            dbbase.ControllerHostTestCase):
    pass


# Test Configuration:
# - AIO
# - IPv4
# - Ceph Storage
# - metrics-server app
class K8SAppMetricsServerAIOTestCase(K8SAppMetricsServerAppMixin,
                                     dbbase.BaseCephStorageBackendMixin,
                                     dbbase.AIOSimplexHostTestCase):
    pass
