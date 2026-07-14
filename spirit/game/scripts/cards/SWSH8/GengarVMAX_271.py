from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, lock_all_attacks
from spirit.game.card_effects.pokemon import is_pokemon_gx


async def g_max_swallow_up(ctx):
    """250. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="473bf9ce-569f-5b57-9765-f858d26dfeb9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarVMAX.Name",
    display_name="Gengar VMAX",
    searchable_by=["Gengar VMAX", "VMAX", "Single Strike", "GengarVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=271,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GengarV.Name",
    family_id=94,
    abilities=[
        Attack(
            title="Fear and Panic",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon V and Pok\u00e9mon-GX in play.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            damage_operator="x",
            effect=damage_per(
                count_in_play(
                    "opponent",
                    pred=lambda c: is_pokemon_v(c.archetype_id) or is_pokemon_gx(c.archetype_id),
                ),
                60,
            ),
        ),
        Attack(
            title="G-Max Swallow Up",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=250,
            effect=g_max_swallow_up,
        ),
    ],
)