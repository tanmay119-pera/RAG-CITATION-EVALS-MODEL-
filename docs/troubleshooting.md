# Scheduled Automation & Daemon Troubleshooting Guide

## Why Did a Scheduled Cron Not Fire?

Scheduled automations run as daemon sidecars. If your scheduled commits did not trigger at their scheduled time:
1. **Host Sleep / Shutdown**: If your laptop or workstation was asleep or powered off at 10:00 AM IST, cron daemons cannot execute.
2. **Server Restart**: If the local IDE or agent service was restarted, background tasks must be awake to register the timer.
3. **Automations Dashboard Status**: Verify that the sidecar toggle is enabled in `sidecar://dashboard`.

## Manual Catch-Up Execution
To trigger today's daily cycle immediately:
```bash
python3 scripts/run_daily_25.py
```
