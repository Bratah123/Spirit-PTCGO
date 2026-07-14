from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.effects import full_stack


async def flower_bearing(ctx):
    heads = (await ctx.flip_coins(1, "Flower Bearing"))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)

card = PokemonCardDef(
    guid="92f69263-b590-5caf-96ce-aeeedec15a9c",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=heal_attack(20),
        ),
        Attack(
            title="Flower Bearing",
            game_text="Flip a coin. If heads, your opponent shuffles their Active Pok\u00e9mon and all attached cards and puts them on the bottom of their deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=flower_bearing,
        ),
    ],
)