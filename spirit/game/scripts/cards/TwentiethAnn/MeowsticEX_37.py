"""STUB: effect not implemented — do not guess mechanics.
Meowstic-EX (TwentiethAnn #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="74e60f4b-6ca9-5826-85e6-f254bdd5368a",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowsticEX.Name",
    display_name="Meowstic-EX",
    searchable_by=["Meowstic-EX", "Basic", "EX", "MeowsticEX"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=678,
    abilities=[
        Ability(
            title="Shadow Ear",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)