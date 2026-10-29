from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.session.effects import is_basic_pokemon


async def cut_down(ctx):
    """Printed damage; flip a coin, heads: discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Crunch")
    if not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy to discard from the Defending Pokémon.",
    )


card = PokemonCardDef(
    guid="30b5f077-2db8-5ea4-a7d0-735617e53628",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMuk.Name",
    display_name="Alolan Muk",
    searchable_by=["Alolan Muk", "Stage 1", "AlolanMuk"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Power of Alchemy",
            game_text="Each Basic Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ability_lock_passive(lambda p, c: is_basic_pokemon(p)),
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=cut_down,
        ),
    ],
)