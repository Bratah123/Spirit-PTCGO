"""STUB: effect not implemented — do not guess mechanics.
Croconaw δ (EX15 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import scary_face_lock


card = PokemonCardDef(
    guid="52d03d8b-75ff-5cfc-b419-248108402972",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw δ",
    searchable_by=["Croconaw \u03b4", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=159,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack or retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=scary_face_lock(),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)