"""STUB: effect not implemented — do not guess mechanics.
Sylveon-EX (TwentiethAnn #RC21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0af78f68-3867-5101-abce-eba0426f37ab",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonEX.Name",
    display_name="Sylveon-EX",
    searchable_by=["Sylveon-EX", "Basic", "EX", "SylveonEX"],
    subtypes=["Basic", "EX"],
    collector_number=104,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=700,
    abilities=[
        Attack(
            title="Dress Up",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Precious Ribbon",
            game_text="Move a Fairy Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. If you do, heal 50 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)