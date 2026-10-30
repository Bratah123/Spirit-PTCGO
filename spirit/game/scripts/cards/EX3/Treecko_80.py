from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="05da45d7-9f14-5856-bdcb-90316d19cef4",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko",
    searchable_by=["Treecko", "Basic", "Treecko"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=252,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)