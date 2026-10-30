from spirit.game.card_effects.ex import darkness_shield_flip, cold_crush
"""STUB: effect not implemented — do not guess mechanics.
Dark Golduck (EX7 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3c04315-12a4-5c84-af2c-084db5e6fac3",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolduck.Name",
    display_name="Dark Golduck",
    searchable_by=["Dark Golduck", "Stage 1", "DarkGolduck"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Darkness Shield",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to each of your Active Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=darkness_shield_flip(),
        ),
        Attack(
            title="Cold Crush",
            game_text="You may discard an Energy card attached to Dark Golduck. If you do, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=cold_crush(),
        ),
    ],
)