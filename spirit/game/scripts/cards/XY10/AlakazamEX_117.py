"""STUB: effect not implemented — do not guess mechanics.
Alakazam-EX (XY10 #117): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a52adcfb-baa4-5b52-888f-6b478ce00a37",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    display_name="Alakazam-EX",
    searchable_by=["Alakazam-EX", "Basic", "EX", "AlakazamEX"],
    subtypes=["Basic", "EX"],
    collector_number=117,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Ability(
            title="Kinesis",
            game_text="When you play M Alakazam-EX from your hand to evolve this Pok\u00e9mon, before it evolves, you may put 2 damage counters on your opponent's Active Pok\u00e9mon and 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Suppression",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)