#!/usr/bin/env bash
# 系统速览：运行时间、负载、内存、磁盘，一屏看完。
# 用法: ./sysinfo.sh
set -euo pipefail

echo "== uptime =="
uptime
echo
echo "== memory =="
free -h
echo
echo "== disk =="
df -h / | tail -n +2
