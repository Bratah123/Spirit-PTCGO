from spirit.game.card_effects.ex import rainbow_moves, holy_shield_passive
"""STUB: effect not implemented — do not guess mechanics.
Togetic (EX7 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=holy_shield_passive(),
    guid="0006943e-b85c-5c0e-9bac-491754069f24",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Holy Shield",
            game_text="Prevent all effects of attacks, including damage, done to Togetic by your opponent's Pok\u00e9mon that has Dark in its name.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Dive",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Rainbow Moves",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon's attacks. Rainbow Moves copies that attack except for its Energy cost. (You must still do anything else required for that attack.) (No matter what type that Pok\u00e9mon is, Togetic's type is still Colorless.) Togetic performs that attack.",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=rainbow_moves(),
        ),
    ],
)