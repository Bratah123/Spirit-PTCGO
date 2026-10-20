"""STUB: effect not implemented — do not guess mechanics.
Wobbuffet BREAK (Promo_XY #XY155): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cfa6326d-5738-5944-bcd1-05c9dec05ad1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetBREAK.Name",
    display_name="Wobbuffet BREAK",
    searchable_by=["Wobbuffet BREAK", "BREAK", "WobbuffetBREAK"],
    subtypes=["BREAK"],
    collector_number=155,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    family_id=202,
    abilities=[
        Attack(
            title="Right Back at You",
            game_text="Discard all Energy attached to this Pok\u00e9mon. During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)