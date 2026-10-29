from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import fire_fling


async def axe_slash(ctx):
    """Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon."""
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="b621e6a0-5b07-561d-8f66-e863f3654236",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=237,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Fire Fling",
            game_text="Put 4 Fire Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.FIRE: 1},
            effect=fire_fling,
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
            effect=axe_slash,
        ),
    ],
)