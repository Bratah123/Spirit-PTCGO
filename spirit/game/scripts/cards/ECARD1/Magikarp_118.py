from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="1853b05a-b74d-5968-8bef-b274925de497",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage times the number of damage counters on Magikarp.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10),
        ),
    ],
)
