from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost


async def hone_claws(ctx):
    """60; during your next turn, this Pokémon's attacks do 30 more."""
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 30)


card = PokemonCardDef(
    guid="86d1814e-6ee5-59c4-83ae-ebede51795c4",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Team Plasma", "Druddigon"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=80,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    family_id=621,
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Boost Claw",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=hone_claws,
        ),
    ],
)