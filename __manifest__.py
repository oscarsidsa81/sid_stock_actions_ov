# -*- coding: utf-8 -*-
{
    "name": "SID Stock Actions (OV matcher)",
    "summary": "Assign stable XML IDs to existing Stock custom actions/menus/automations (OV) for migration-safe references.",
    "version": "15.0.1.0.0",
    "category": "Inventory/Inventory",
    "license": "LGPL-3",
    "author": "SIDSA",
    "website": "",
    "depends": ["stock", "base_automation"],
    "data": [],
    "post_init_hook": "post_init_match_stock_actions_ov",
    "installable": True,
    "application": False,
}
