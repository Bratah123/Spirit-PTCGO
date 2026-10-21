from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on


def _ten_or_more_counters(ctx):
    return damage_counters_on("self")(ctx) >= 10


card = PokemonCardDef(
    guid="599fa033-3f59-5707-b8db-7d46160a6ea9",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGlalieEX.Name",
    display_name="M Glalie-EX",
    searchable_by=["M Glalie-EX", "MEGA", "EX", "MGlalieEX"],
    subtypes=["MEGA", "EX"],
    collector_number=156,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlalieEX.Name",
    family_id=362,
    abilities=[
        Attack(
            title="Cryo Mouth",
            game_text="If this Pok\u00e9mon has 10 or more damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_ten_or_more_counters, 150),
        ),
    ],
)