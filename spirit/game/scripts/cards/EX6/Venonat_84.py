from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.ex import discard_energy_then_condition

card = PokemonCardDef(
    guid="13d4b986-3bbc-514d-a079-39e0c504ae0e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Psycho Waves",
            game_text="Discard an Energy card attached to Venonat. The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_energy_then_condition(None, SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)