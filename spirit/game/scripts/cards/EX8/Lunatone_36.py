"""STUB: effect not implemented — do not guess mechanics.
Lunatone (EX8 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import foresight_reorder, moonglow_solrock_retreat, target_beam_solrock


card = PokemonCardDef(
    guid="0a8462f6-c6f5-508b-8163-fe7e38a70930",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=337,
    abilities=[
        Ability(
            title="Moonglow",
            game_text="The Retreat Cost for each Solrock you have in play is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=moonglow_solrock_retreat(),
        ),
        Attack(
            title="Foresight",
            game_text="Look at the top 5 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=foresight_reorder(),
        ),
        Attack(
            title="Target Beam",
            game_text="Does 20 damage plus 10 more damage for each Solrock you have in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=target_beam_solrock(),
        ),
    ],
)