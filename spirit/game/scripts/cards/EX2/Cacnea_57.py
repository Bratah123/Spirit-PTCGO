from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.ex import condition_on_damaged


card = PokemonCardDef(
    guid="9421f58c-ba81-5bee-a21f-84477a8960cd",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic", "Cacnea"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=331,
    abilities=[
        Ability(
            title="Poison Payback",
            game_text="If Cacnea is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Cacnea is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=condition_on_damaged(SpecialConditions.POISONED),
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
