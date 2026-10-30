"""STUB: effect not implemented — do not guess mechanics.
Unown [Q] (DP5 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a44f192b-af6f-5207-8ae3-c4302eab3f18",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownQ.Name",
    display_name="Unown [Q]",
    searchable_by=["Unown [Q]", "Basic", "UnownQ"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="QUICK",
            game_text="Once during your turn (before your attack), if Unown Q is on your Bench, you may discard all cards attached to Unown Q and attach Unown Q to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. As long as Unown Q is attached to a Pok\u00e9mon, you pay Colorless less to retreat that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)