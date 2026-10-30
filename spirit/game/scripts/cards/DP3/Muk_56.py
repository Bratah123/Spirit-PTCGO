"""STUB: effect not implemented — do not guess mechanics.
Muk (DP3 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="066c0cd9-5b9f-529b-8fa8-536c6ca17a3d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Toxic Sludge",
            game_text="At the end of each player's turn, each of your opponent's Active Pok\u00e9mon that has any Grass Energy attached to it is now Poisoned. If that Pok\u00e9mon is already Poisoned, Toxic Sludge Pok\u00e9-Body does nothing to that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Panic Liquid",
            game_text="The Defending Pok\u00e9mon is now Confused and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)