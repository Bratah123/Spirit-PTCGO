from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


async def blue_surge_gx(ctx):
    """220 damage, then move all Energy from this Pokémon to the Bench."""
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench())


card = PokemonCardDef(
    guid="da7ea9c3-a0f9-5708-bc7a-aeb7a079209a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WishiwashiGX.Name",
    display_name="Wishiwashi-GX",
    searchable_by=["Wishiwashi-GX", "Basic", "GX", "WishiwashiGX"],
    subtypes=["Basic", "GX"],
    collector_number=38,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Torrential Vortex",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Blue Surge-GX",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=blue_surge_gx,
        ),
    ],
)