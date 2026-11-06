from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="2aeb889b-acb5-58ca-908e-4ab56a2d441a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Poison Sludge",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
