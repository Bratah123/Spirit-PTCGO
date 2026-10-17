"""STUB: effect not implemented — do not guess mechanics.
Dragonite-EX (XY3 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb07f4ae-8d61-5224-971d-1f1c414bb5e0",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=108,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=149,
    abilities=[
        Ability(
            title="Bust In",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may move any number of basic Energy attached to your Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jet Sonic",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.LIGHTNING: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)