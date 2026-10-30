"""STUB: effect not implemented — do not guess mechanics.
Charmeleon (EX16 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import scary_face_lock


card = PokemonCardDef(
    guid="d9036f20-0c29-5ebf-9e80-2b1da71f3425",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack or retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=scary_face_lock(),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)