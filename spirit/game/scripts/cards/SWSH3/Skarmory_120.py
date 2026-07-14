from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_tool

card = PokemonCardDef(
    guid="8995eebe-8e3d-56c4-a6ae-506c1c1e652f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Metal Arms",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(lambda ctx: has_tool(ctx.attacker), 40),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)