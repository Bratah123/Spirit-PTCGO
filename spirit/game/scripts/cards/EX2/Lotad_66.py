from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import rain_dish


card = PokemonCardDef(
    guid="1c8f1391-9453-5b33-ab9b-376029093dd6",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    display_name="Lotad",
    searchable_by=["Lotad", "Basic", "Lotad"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=270,
    abilities=[
        Ability(
            title="Rain Dish",
            game_text="At any time between turns, remove 1 damage counter from Lotad.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=rain_dish(),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
