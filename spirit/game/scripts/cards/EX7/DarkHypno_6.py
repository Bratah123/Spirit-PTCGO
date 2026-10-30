from spirit.game.card_effects.ex import black_magic_per_opp_bench, dark_link
"""STUB: effect not implemented — do not guess mechanics.
Dark Hypno (EX7 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca41b4f4-7d96-5767-b259-f87f4a55ffbd",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHypno.Name",
    display_name="Dark Hypno",
    searchable_by=["Dark Hypno", "Stage 1", "DarkHypno"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Dark Link",
            game_text="Flip a coin. If heads, choose an attack on 1 of your Pok\u00e9mon in play that has Dark in its name (excluding this one). Dark Link copies that attack except for its Energy cost. (You must still do anything else required for that attack.) (No matter what type that Pok\u00e9mon is, Dark Hypno's type is still Psychic Darkness.) Dark Hypno performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dark_link(),
        ),
        Attack(
            title="Black Magic",
            game_text="Does 20 damage times the number of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=black_magic_per_opp_bench(),
        ),
    ],
)