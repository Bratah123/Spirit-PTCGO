"""STUB: effect not implemented — do not guess mechanics.
Flareon-EX (TwentiethAnn #RC6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f46d1d42-ff21-5633-84d5-0eaae89c57bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonEX.Name",
    display_name="Flareon-EX",
    searchable_by=["Flareon-EX", "Basic", "EX", "FlareonEX"],
    subtypes=["Basic", "EX"],
    collector_number=89,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Ability(
            title="Flash Fire",
            game_text="Once during your turn (before your attack), you may move a Fire Energy from 1 of your Pok\u00e9mon to this Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)