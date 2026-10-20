"""STUB: effect not implemented — do not guess mechanics.
Azelf (Promo_XY #XY142): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d19ff267-9833-5cca-9e2f-23eb21cb166c",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Attack(
            title="Shining Eyes",
            game_text="Put 2 damage counters on each of your opponent's Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)