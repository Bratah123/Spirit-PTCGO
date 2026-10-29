from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import doom_count_gx

async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)

async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)

card = PokemonCardDef(
    guid="9f7b9735-52db-54d1-8236-20b05bb0c7bd",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalGX.Name",
    display_name="Yveltal-GX",
    searchable_by=["Yveltal-GX", "Basic", "GX", "YveltalGX"],
    subtypes=["Basic", "GX"],
    collector_number=124,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Absorb Vitality",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=gulp_down,
        ),
        Attack(
            title="Sonic Evil",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=sonic_boom,
        ),
        Attack(
            title="Doom Count-GX",
            game_text="If your opponent's Active Pok\u00e9mon has exactly 4 damage counters on it, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=doom_count_gx,
        ),
    ],
)
