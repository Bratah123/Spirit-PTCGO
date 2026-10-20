"""STUB: effect not implemented — do not guess mechanics.
Noivern BREAK (XY8 #113): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="110563a9-f258-524b-8f30-1983b2627214",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernBREAK.Name",
    display_name="Noivern BREAK",
    searchable_by=["Noivern BREAK", "BREAK", "NoivernBREAK"],
    subtypes=["BREAK"],
    collector_number=113,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Synchro Woofer",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)