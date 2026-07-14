from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on


def _ten_or_more_counters(ctx):
    return damage_counters_on("self")(ctx) >= 10


card = PokemonCardDef(
    guid="4c7ec035-54c6-5359-b5eb-256b7cb95e40",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionV.Name",
    display_name="Volcanion V",
    searchable_by=["Volcanion V", "Basic", "V", "Single Strike", "VolcanionV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=162,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Dynamite Tackle",
            game_text="If this Pok\u00e9mon has 10 or more damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_ten_or_more_counters, 150),
        ),
    ],
)