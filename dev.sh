#!/bin/bash
cd /opt/nexus
source nexus-env/bin/activate
echo "🔷 NEXUS PROTOCOL DEVELOPMENT ENVIRONMENT"
echo "========================================"
echo "🐍 Python: $(python --version)"
echo "📁 Project: /opt/nexus/"
echo "👤 Git: $(git config user.name) <$(git config user.email)>"
echo "🌐 Remote: https://github.com/Blackstar-sys-101/nexus-protocol"
echo "📁 Branch: $(git branch --show-current)"
echo "💾 Database: PostgreSQL (nexus_protocol)"
echo "📊 Redis: $(redis-cli ping 2>/dev/null && echo 'Ready' || echo 'Not responding')"
echo "🐳 Docker: $(docker --version 2>/dev/null | cut -d' ' -f3 || echo 'Not available')"
echo "🌐 Nginx: $(nginx -v 2>&1 | cut -d'/' -f2 || echo 'Not available')"
echo "========================================"
echo "Ready to build secure decentralized coordination! 🚀"
