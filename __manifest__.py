{
    "name": "SID Stock Actions OV",
    "version": "15.0.1.0.1",
    "summary": "Anchor existing stock OV actions with stable xml_ids",
    "category": "Inventory",
    "license": "AGPL-3",
    "depends": ["stock", "base"],
    "data": [],
    "post_init_hook": "post_init_create_action_xmlids",
    "installable": True,
    "application": False
}