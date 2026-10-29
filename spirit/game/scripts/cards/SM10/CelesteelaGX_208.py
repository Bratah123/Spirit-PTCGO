from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    discovery_gx,
    force_canceler_passive,
)

async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)

card = PokemonCardDef(
    guid="7cb28350-8851-5fbd-9325-ec337378db4c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelesteelaGX.Name",
    display_name="Celesteela-GX",
    searchable_by=["Celesteela-GX", "Basic", "GX", "Ultra Beast", "CelesteelaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=208,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=797,
    abilities=[
        Ability(
            title="Force Canceler",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, prevent all effects of your opponent's GX attacks, including damage, done to your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=force_canceler_passive
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=shadow_cyclone,
        ),
        Attack(
            title="Discovery-GX",
            game_text="Count your Prize cards and put them into your hand. Then, take that many cards from the top of your deck and put them face down as your Prize cards. If you don't have that many cards in your deck, this attack does nothing. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discovery_gx
        ),
    ],
)