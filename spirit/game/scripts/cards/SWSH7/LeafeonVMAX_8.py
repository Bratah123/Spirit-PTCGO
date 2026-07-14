from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.support_common import heal_attack


def _defender_retreat_cost(ctx):
    active = ctx.opponent_active()
    return int(active.get_attribute(AttrID.RETREAT_COST) or 0) if active else 0

card = PokemonCardDef(
    guid="ef02857d-8e3e-57d9-9d05-0faecc5ad47e",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVMAX.Name",
    display_name="Leafeon VMAX",
    searchable_by=["Leafeon VMAX", "VMAX", "LeafeonVMAX"],
    subtypes=["VMAX"],
    collector_number=8,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Attack(
            title="Grass Knot",
            game_text="This attack does 60 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(_defender_retreat_cost, 60),
        ),
        Attack(
            title="Max Leaf",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=heal_attack(30, target="self"),
        ),
    ],
)