SID Stock Actions (OV matcher)
=============================

Este módulo NO crea acciones/menús/automatizaciones nuevas.
Su objetivo es asignar XML IDs estables (bajo el namespace sid_stock_actions_ov.*)
a registros ya existentes (creados históricamente por Studio o por importaciones).

Esto permite que módulos posteriores (vistas, menús, etc.) referencien acciones por XML ID
en lugar de IDs numéricos, facilitando migraciones.

