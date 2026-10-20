"""STUB: effect not implemented — do not guess mechanics.
Shiftry (XY11 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


card = PokemonCardDef(
    guid="809eec17-47eb-503a-8016-84934c956595",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Wicked Wind",
            game_text="Until the end of your opponent's next turn, each Stadium or Pok\u00e9mon Tool card in play has no effect. (This includes cards that come into play on that turn.)",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(lambda ctx: len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)), 60),
        ),
    ],
)