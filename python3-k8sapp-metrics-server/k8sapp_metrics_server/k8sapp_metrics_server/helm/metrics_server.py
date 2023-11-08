#
# Copyright (c) 2023 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

from sysinv.common import exception
from sysinv.helm import base

from k8sapp_metrics_server.common import constants as app_constants


class MetricsServerHelm(base.FluxCDBaseHelm):
    """Class to encapsulate helm operations for the app chart"""

    SUPPORTED_NAMESPACES = base.BaseHelm.SUPPORTED_NAMESPACES + \
        [app_constants.HELM_NS_METRICS_SERVER]
    SUPPORTED_APP_NAMESPACES = {
        app_constants.HELM_APP_METRICS_SERVER: SUPPORTED_NAMESPACES
    }

    CHART = app_constants.HELM_CHART_METRICS_SERVER
    HELM_RELEASE = app_constants.FLUXCD_HELMRELEASE_METRICS_SERVER

    def get_namespaces(self):
        return self.SUPPORTED_NAMESPACES

    def get_overrides(self, namespace=None):

        overrides = {
            app_constants.HELM_NS_METRICS_SERVER: {}
        }

        if namespace in self.SUPPORTED_NAMESPACES:
            return overrides[namespace]
        elif namespace:
            raise exception.InvalidHelmNamespace(chart=self.CHART,
                                                 namespace=namespace)
        else:
            return overrides
