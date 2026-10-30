"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Carvanha (EX4 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.ex import dark_lift_passive, delayed_condition

card = PokemonCardDef(
    guid="9e850cbe-76ae-5685-b5da-83c1d87e7ba9",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    display_name="Team Aqua's Carvanha",
    searchable_by=["Team Aqua's Carvanha", "Basic", "TeamAquasCarvanha"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Ability(
            title="Dark Lift",
            game_text="If Team Aqua's Carvanha has any Darkness Energy attached to it, the Retreat Cost for Team Aqua's Carvanha is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=dark_lift_passive(),
        ),
        Attack(
            title="Slow-Acting Poison",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=delayed_condition(SpecialConditions.POISONED),
        ),
    ],
)