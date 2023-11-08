#
# Copyright (c) 2023 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

""" System inventory App lifecycle operator."""

from sysinv.helm import lifecycle_base as base


class MetricsServerAppLifecycleOperator(base.AppLifecycleOperator):
    """Class to encapsulate lifecycle operations for the Metrics Server"""

    def app_lifecycle_actions(self,
                              context,
                              conductor_obj,
                              app_op, app,
                              hook_info):
        """Perform lifecycle actions for an operation

        :param context: request context
        :param conductor_obj: conductor object
        :param app_op: AppOperator object
        :param app: AppOperator.Application object
        :param hook_info: LifecycleHookInfo object
        """
