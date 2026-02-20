
from odoo import api, SUPERUSER_ID

def post_init_create_action_xmlids(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    IMD = env["ir.model.data"].sudo()

    action_models = [
        "ir.actions.act_window",
        "ir.actions.server",
        "ir.actions.report",
    ]

    for model_name in action_models:
        Model = env[model_name].sudo()
        for rec in Model.search([]):
            existing = IMD.search([
                ("model", "=", model_name),
                ("res_id", "=", rec.id),
            ], limit=1)

            if not existing:
                xml_name = f"action_{rec.id}"
                IMD.create({
                    "module": "sid_stock_actions_ov",
                    "name": xml_name,
                    "model": model_name,
                    "res_id": rec.id,
                })

    env.cr.commit()
