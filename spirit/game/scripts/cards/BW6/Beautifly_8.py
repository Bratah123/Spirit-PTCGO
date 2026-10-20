from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _triple_energy(ctx):
    """Search for 3 basic Energy cards of different types and attach them to
    your Pokemon in any way you like; shuffle."""
    picked, used = [], set()
    for _ in range(3):
        picks = await ctx.search_deck(
            lambda c: is_basic_energy_card(c) and c not in picked
            and not (set(c.get_attribute(AttrID.POKEMON_TYPES) or []) & used),
            count=1, minimum=0,
            prompt="Choose a basic Energy card of a different type")
        if not picks:
            break
        picked.append(picks[0])
        used.update(picks[0].get_attribute(AttrID.POKEMON_TYPES) or [])
    if picked:
        await distribute_energy(ctx, picked, ctx.my_pokemon_in_play())
    await ctx.shuffle_deck()


async def _drainpour(ctx):
    """Printed damage; heal 40 damage from each of your Benched Pokemon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(40, pokemon)


card = PokemonCardDef(
    guid="971ab21f-f516-55bc-b8ac-7b088af8b5bf",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Triple Energy",
            game_text="Search your deck for 3 different types of basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=_triple_energy,
        ),
        Attack(
            title="Drainpour",
            game_text="Heal 40 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_drainpour,
        ),
    ],
)