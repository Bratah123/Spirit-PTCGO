from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import conditions_if
from spirit.game.card_effects.ex import defender_is_ex, may_discard_energy_for_condition


card = PokemonCardDef(
    guid="6835f419-d12f-55b5-898e-e89518b261ae",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Seviper"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Deadly Poison",
            game_text="You may discard a Grass Energy card attached to Seviper. If you do, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=may_discard_energy_for_condition(
                PokemonTypes.GRASS, SpecialConditions.POISONED,
                prompt="You may discard a Grass Energy card",
            ),
        ),
        Attack(
            title="Extra Poison",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, the Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=conditions_if(
                defender_is_ex,
                SpecialConditions.ASLEEP, SpecialConditions.POISONED,
            ),
        ),
    ],
)
