"""STUB: effect not implemented — do not guess mechanics.
Genesect-EX (XY10 #120): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37e4d0b2-4a80-5439-8bf9-59a0a23400da",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "GenesectEX"],
    subtypes=["Basic", "EX"],
    collector_number=120,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Ability(
            title="Drive Change",
            game_text="Once during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to this Pok\u00e9mon into your hand.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rapid Blaster",
            game_text="Discard as many Metal Energy attached to this Pok\u00e9mon as you like. This attack does 20 more damage for each Metal Energy you discarded.",
            cost={PokemonTypes.METAL: 3},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)