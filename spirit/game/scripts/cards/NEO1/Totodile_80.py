from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="3d12e662-fc33-5ef5-8ea5-e7b04ba91e1f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=158,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Totodile.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=10),
        ),
    ],
)
