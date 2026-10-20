"""STUB: effect not implemented — do not guess mechanics.
Celebi (Promo_XY #XY93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3fe533d2-cbc3-5384-b0be-eba42cb313c4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Leap Through Time",
            game_text="When this Pok\u00e9mon is Knocked Out, flip a coin. If heads, shuffle this Pok\u00e9mon and all cards attached to it into your deck, and your opponent can't take any Prize cards for it.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sparkle Motion",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)