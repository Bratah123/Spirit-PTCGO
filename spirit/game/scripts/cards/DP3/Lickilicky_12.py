"""STUB: effect not implemented — do not guess mechanics.
Lickilicky (DP3 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fbc1354-3338-5540-ba7e-920e593c4b99",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Tongue Reel",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. If you choose a Benched Pok\u00e9mon, switch the Defending Pok\u00e9mon with that Pok\u00e9mon. This attack does 20 damage to the Pok\u00e9mon you chose. Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, Lickilicky can't attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)