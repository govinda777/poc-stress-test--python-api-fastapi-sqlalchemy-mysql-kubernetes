#!/bin/bash

# Ajustar permissões
chown -R mysql:mysql /var/lib/mysql

# Iniciar o MySQL
exec docker-entrypoint.sh mysqld
