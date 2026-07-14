from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


async def sonic_strike(ctx):
    await ctx.discard_energy_from(ctx.attacker, 3, prompt="Choose 3 Energy to discard")
    await snipe_attack(220, pool="any", count=1)(ctx)


card = PokemonCardDef(
    guid="2db2e893-50d1-50b9-b12a-9f748f583367",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompV.Name",
    display_name="Garchomp V",
    searchable_by=["Garchomp V", "Basic", "V", "GarchompV"],
    subtypes=["Basic", "V"],
    collector_number=178,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=445,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Sonic Strike",
            game_text="Discard 3 Energy from this Pok\u00e9mon. This attack does 220 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=sonic_strike,
        ),
    ],
)