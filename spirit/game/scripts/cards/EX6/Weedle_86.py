from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.ex import call_for_family_grass, discard_energy_then_condition

card = PokemonCardDef(
    guid="c1531843-ef1c-57b2-8b37-bac2bda87986",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Grass Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family_grass(2),
        ),
        Attack(
            title="Poison Spurt",
            game_text="Discard a Grass Energy card attached to Weedle. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=discard_energy_then_condition(PokemonTypes.GRASS, SpecialConditions.POISONED),
        ),
    ],
)