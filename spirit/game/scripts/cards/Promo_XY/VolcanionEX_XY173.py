"""STUB: effect not implemented — do not guess mechanics.
Volcanion-EX (Promo_XY #XY173): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9c10544-822c-5e6d-bae5-46da37ed64fb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name",
    display_name="Volcanion-EX",
    searchable_by=["Volcanion-EX", "Basic", "EX", "VolcanionEX"],
    subtypes=["Basic", "EX"],
    collector_number=173,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Steam Up",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, during this turn, your Basic Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)