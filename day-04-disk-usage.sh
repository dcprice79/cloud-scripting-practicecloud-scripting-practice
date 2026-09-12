#!/bin/bash
echo "=== Disk Usage Report ==="
echo "Date: $(date)"
echo ""
df -h | grep -v tmpfs
echo ""
ech "Top 5 largest directories:"
du -sh /* 2>/dev/null | sort -rh | head -5
