from marshmallow import fields, post_load, Schema

from src.plantes.domain.Plante import Plante


class PlanteSchema(Schema):
    id: fields.Integer(required=True)
    common_name: fields.String(required=True)
    slug: fields.String(required=True)
    scientific_name: fields.String(required=True)
    year: fields.String(required=True)
    bibliography: fields.String(required=True)
    author: fields.String(required=True)
    status: fields.String(required=True)
    rank: fields.String(required=True)
    family_common_name: fields.String(required=True)
    genus_id: fields.String(required=True)
    image_url: fields.String(required=True)
    synonyms: fields.List(fields.String, required=True)
    genus: fields.String(required=True)
    family: fields.String(required=True)
    links: fields.List(fields.Dict, required=True)

    @post_load
    def make_plante(self, data, **kwargs):
        return Plante(**data)
