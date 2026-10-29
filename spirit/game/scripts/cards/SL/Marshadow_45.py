"""STUB: effect not implemented — do not guess mechanics.
Marshadow (SL #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sl import let_loose


async def puncture(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="b287060d-ab17-57e8-bcdf-7358c21c3e2b",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Marshadow"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Ability(
            title="Let Loose",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may have each player shuffle their hand into their deck and draw 4 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=let_loose,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=puncture,
        ),
    ],
)