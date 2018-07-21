# -*- coding: utf-8 -*-

from scanhosts.models import HostInfo
from ansible_task.models import AnsibleModuleLog
from rest_framework import serializers
from assets.models import *
from users.models import UserProfile, UserLog
from django.contrib.auth.models import Permission, Group


class HostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostInfo
        fields = ('id', 'internal_ip', 'public_ip', 'system_ver', 'hostname',
                  'host_type', 'sn', 'manufacturer', 'server_model', 'mac', 'total_mem', 'cpu_counts',
                  'cpu_model', 'total_disk', 'scan_datetime')


class ModuleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnsibleModuleLog
        fields = ('id', 'ans_user', 'ans_remote_ip', 'ans_module', 'ans_args',
                  'ans_server', 'ans_result', 'ans_datetime')


class AssetsSerializer(serializers.ModelSerializer):
    asset_management_ip = serializers.IPAddressField(allow_blank=True, allow_null=True)

    class Meta:
        model = Assets
        fields = '__all__'


class ServerAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = ServerAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        server = ServerAssets.objects.create(**data)
        return server


class NetworkAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = NetworkAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        network = NetworkAssets.objects.create(**data)
        return network


class OfficeAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = OfficeAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        office = OfficeAssets.objects.create(**data)
        return office


class SecurityAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = SecurityAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        security = SecurityAssets.objects.create(**data)
        return security


class StorageAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = StorageAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        storage = StorageAssets.objects.create(**data)
        return storage


class SoftwareAssetsSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=False, required=False)

    class Meta:
        model = SoftwareAssets
        fields = '__all__'

    def create(self, data):
        if data.get('assets'):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets
        software = StorageAssets.objects.create(**data)
        return software


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'project_name', 'service_name', 'service_assets')


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'parent_project', 'project_name', 'project_memo', 'service')


class AssetProviderSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=True, read_only=True)

    class Meta:
        model = AssetProvider
        fields = (
            'id', 'asset_provider_name', 'asset_provider_contact', 'asset_provider_telephone', 'asset_provider_memo',
            'assets')


class CabinetSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=True, read_only=True)

    class Meta:
        model = Cabinet
        fields = ('id', 'idc', 'cabinet_name', 'cabinet_memo', 'assets')


class IDCSerializer(serializers.ModelSerializer):
    cabinet = CabinetSerializer(many=True, read_only=True)
    assets = AssetsSerializer(many=True, read_only=True)

    class Meta:
        model = IDC
        fields = ('id', 'idc_name', 'idc_address', 'idc_contact', 'idc_telephone', 'idc_memo', 'cabinet', 'assets')


class UsersSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'mobile', 'is_superuser', 'is_active', 'groups', 'user_permissions', 'assets')


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'user_set', 'permissions')


class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = '__all__'


class AssetsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsLog
        fields = '__all__'
