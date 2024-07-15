# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-DB管理系统(BlueKing-BK-DBM) available.
Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging

from django.utils.translation import ugettext as _
from rest_framework.response import Response

from backend.flow.engine.controller.cloud import CloudServiceController
from backend.flow.views.base import FlowTestView
from backend.utils.basic import generate_root_id

logger = logging.getLogger("root")


class CloudRedisDTSServerApplySceneApiView(FlowTestView):
    def post(self, request):
        """
        {
            "created_by": "admin",
            "bk_biz_id": 2005000194,
            "ticket_type": "CLOUD_REDIS_DTS_SERVER_APPLY",
            "bk_cloud_id": 0,
            "redis_dts":{
                "host_infos": [
                    {
                        "ip": "xxx",
                        "bk_cloud_id": 0,
                        "bk_host_id":0,
                        "bk_city_name":"xxx"
                    }
                ]
            }
        }
        """
        logger.info(_("开始部署redis dts服务场景"))

        root_id = generate_root_id()
        logger.info("define root_id: {}".format(root_id))
        CloudServiceController(root_id=root_id, ticket_data=request.data).redis_dts_server_apply_scene()
        return Response({"root_id": root_id})


class CloudRedisDTSServerReduceSceneApiView(FlowTestView):
    def post(self, request):
        """
        {
            "created_by": "admin",
            "bk_biz_id": 2005000194,
            "ticket_type": "CLOUD_REDIS_DTS_SERVER_REDUCE",
            "bk_cloud_id": 0,
            "redis_dts":{
                "host_infos": [
                    {
                        "id": 15,
                        "bk_host_id":111,
                    }
                ]
            }
        }
        """
        logger.info(_("删除redis dts服务场景"))

        root_id = generate_root_id()
        logger.info("define root_id: {}".format(root_id))
        CloudServiceController(root_id=root_id, ticket_data=request.data).redis_dts_server_reduce_scene()
        return Response({"root_id": root_id})