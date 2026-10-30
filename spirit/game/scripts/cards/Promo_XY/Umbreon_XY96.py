from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, GameSequence
from spirit.game.session.effects import is_pokemon_card


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)
import random


async def _lunatic_sense(ctx):
    """60+; turn 1 of your face-down Prize cards face up (it stays face up):
    +60 if it is a Pokemon. The pick is blind, so a random face-down Prize."""
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    pool = [c for c in (area.children if area else []) if not getattr(c, "face_up_prize", False)]
    bonus = 0
    if pool:
        card = random.choice(pool)
        await ctx.flush_choreography()
        card.face_up_prize = True
        session = ctx.session
        await session.send_game_sequence(list(session.players.values()), GameSequence.GROUPED_MOVE,
                                         [session._entity_introduced_msg(card)])
        if is_pokemon_card(card):
            bonus = 60
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="85027375-1831-5026-bc93-71873e6f9832",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=197,
    abilities=[
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=feint,
        ),
        Attack(
            title="Lunatic Sense",
            game_text="Turn 1 of your face-down Prize cards face up. If that Prize card is a Pok\u00e9mon, this attack does 60 more damage. (That Prize card remains up for the rest of the game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_lunatic_sense,
        ),
    ],
)