"""STUB: effect not implemented — do not guess mechanics.
Skiploom (EX7 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import miracle_powder, buffer_passive


card = PokemonCardDef(
    passive=buffer_passive(),
    guid="7f0eaeb2-cd7d-51af-8c50-3358de50e3a1",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Skiploom"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Buffer",
            game_text="If Skiploom would be Knocked Out by an opponent's attack, flip a coin. If heads, Skiploom is not Knocked Out and its remaining HP becomes 10 instead.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose 1 Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=miracle_powder(),
        ),
    ],
)