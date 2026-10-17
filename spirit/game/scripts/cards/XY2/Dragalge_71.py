"""STUB: effect not implemented — do not guess mechanics.
Dragalge (XY2 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb6e3716-4b6a-5969-8c87-5c8aa30e34ad",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1", "Dragalge"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Ability(
            title="Poison Barrier",
            game_text="Your opponent's Poisoned Pok\u00e9mon can't retreat.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)