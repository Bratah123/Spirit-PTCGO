"""STUB: effect not implemented — do not guess mechanics.
Jirachi (Promo_XY #XY67a): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7456444a-ae0f-5b2d-92cc-7133ef47e477",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=212,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Stardust",
            game_text="Discard a Special Energy attached to your opponent's Active Pok\u00e9mon. If you do, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dream Dance",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)