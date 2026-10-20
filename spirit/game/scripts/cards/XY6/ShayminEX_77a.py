from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import EffectContext
from spirit.game.card_effects.support_common import remove_self_from_play


async def set_up(ctx: EffectContext):
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="9b81cdb6-4ef9-57fd-8985-cee3d115060a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=111,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Ability(
            title="Set Up",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may draw cards until you have 6 cards in your hand.",
            trigger=Triggers.ON_PLAY,
            effect=set_up,
        ),
        Attack(
            title="Sky Return",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=remove_self_from_play('hand'),
        ),
    ],
)