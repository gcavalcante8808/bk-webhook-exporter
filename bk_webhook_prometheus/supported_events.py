from enum import Enum


import bk_webhook_prometheus.event_metrics


class BuildKiteEvents(Enum):
    PING = bk_webhook_prometheus.event_metrics.ping
    BUILD_SCHEDULED = bk_webhook_prometheus.event_metrics.build_scheduled
    BUILD_RUNNING = bk_webhook_prometheus.event_metrics.build_running
    BUILD_FINISHED = bk_webhook_prometheus.event_metrics.build_finished
    JOB_SCHEDULED = bk_webhook_prometheus.event_metrics.job_scheduled
    JOB_STARTED = bk_webhook_prometheus.event_metrics.job_started
    JOB_FINISHED = bk_webhook_prometheus.event_metrics.job_finished
    JOB_ACTIVATED = bk_webhook_prometheus.event_metrics.job_activated
    AGENT_CONNECTED = bk_webhook_prometheus.event_metrics.agent_connected
    AGENT_LOST = bk_webhook_prometheus.event_metrics.agent_lost
    AGENT_DISCONNECTED = bk_webhook_prometheus.event_metrics.agent_disconnected
    AGENT_STOPPING = bk_webhook_prometheus.event_metrics.agent_stopping
    AGENT_STOPPED = bk_webhook_prometheus.event_metrics.agent_stopped
