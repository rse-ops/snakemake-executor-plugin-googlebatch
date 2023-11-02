from typing import Optional

import snakemake.common.tests
import snakemake.settings
from snakemake_executor_plugin_googlebatch import ExecutorSettings
from snakemake_interface_executor_plugins.settings import ExecutorSettingsBase

# from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase


class TestWorkflowsBase(snakemake.common.tests.TestWorkflowsMinioPlayStorageBase):
    __test__ = True

    def get_executor(self) -> str:
        return "googlebatch"

    def get_executor_settings(self) -> Optional[ExecutorSettingsBase]:
        # instatiate ExecutorSettings of this plugin as appropriate
        return ExecutorSettings()

    def get_assume_shared_fs(self):
        return False

    def get_remote_execution_settings(
        self,
    ) -> snakemake.settings.RemoteExecutionSettings:
        return snakemake.settings.RemoteExecutionSettings(
            seconds_between_status_checks=10,
            envvars=self.get_envvars(),
            # TODO: remove once we have switched to stable snakemake for dev
            container_image="snakemake/snakemake:latest",
        )
