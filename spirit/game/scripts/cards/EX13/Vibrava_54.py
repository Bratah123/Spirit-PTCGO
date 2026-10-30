from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="0060fc78-f152-59d6-ab33-755ef1f9e328",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava δ",
    searchable_by=["Vibrava \u03b4", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=329,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)