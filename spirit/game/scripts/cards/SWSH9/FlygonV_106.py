from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import defender_is_vmax


async def draconic_impulse(ctx):
    if defender_is_vmax(ctx):
        await ctx.deal_damage(320)
        await ctx.discard_energy_from(ctx.attacker, 3)
    else:
        await ctx.deal_damage(160)


card = PokemonCardDef(
    guid="f0b0b7aa-4f77-55e5-a5a9-db7736002ab7",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonV.Name",
    display_name="Flygon V",
    searchable_by=["Flygon V", "Basic", "V", "FlygonV"],
    subtypes=["Basic", "V"],
    collector_number=106,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=330,
    abilities=[
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
        Attack(
            title="Draconic Impulse",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon VMAX, this attack does 160 more damage, and discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=draconic_impulse,
        ),
    ],
)