from prometheus_client import Counter


ping = Counter("bk_webhook_poing", "")

build_scheduled = Counter("bk_webhook_build_scheduled", "")
build_running = Counter("bk_webhook_build_running", "")
build_finished = Counter("bk_webhook_build_finished", "")

job_scheduled = Counter("bk_webhook_job_scheduled", "")
job_started = Counter("bk_webhook_job_started", "")
job_finished = Counter("bk_webhook_job_finished", "")
job_activated = Counter("bk_webhook_job_activated", "")

agent_connected = Counter("bk_webhook_agent_connected", "")
agent_lost = Counter("bk_webhook_agent_lost", "")
agent_disconnected = Counter("bk_webhook_agent_disconnected", "")
agent_stopping = Counter("bk_webhook_agent_stopping", "")
agent_stopped = Counter("bk_webhook_agent_stopped", "")
