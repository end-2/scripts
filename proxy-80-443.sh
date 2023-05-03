#!/bin/bash

# Set variables
PROXY_SERVER="proxy-server"
PROXY_PORT="8080"
DESTINATION_SERVER="localhost"
DESTINATION_PORT="9000"
SSL_PORT="443"
NON_SSL_PORT="80"

# Set iptables rules for port 80 and 443
iptables -t nat -A PREROUTING -p tcp --dport $SSL_PORT -j DNAT --to-destination $DESTINATION_SERVER:$SSL_PORT
iptables -t nat -A PREROUTING -p tcp --dport $NON_SSL_PORT -j DNAT --to-destination $DESTINATION_SERVER:$NON_SSL_PORT

# Set proxy for 80 and 443 ports
export http_proxy=$PROXY_SERVER:$PROXY_PORT
export https_proxy=$PROXY_SERVER:$PROXY_PORT

# Test connections to port 80 and 443
curl -I http://localhost:$NON_SSL_PORT
curl -I https://localhost:$SSL_PORT

# Remove proxy settings
unset http_proxy
unset https_proxy

# Remove iptables rules for port 80 and 443
iptables -t nat -D PREROUTING -p tcp --dport $SSL_PORT -j DNAT --to-destination $DESTINATION_SERVER:$SSL_PORT
iptables -t nat -D PREROUTING -p tcp --dport $NON_SSL_PORT -j DNAT --to-destination $DESTINATION_SERVER:$NON_SSL_PORT
