from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


_water = count_energy('self', energy_type=PokemonTypes.WATER)


async def _blast_geyser(ctx):
    """120+; you may do 20 more per Water Energy on this Pokemon; if you do, discard your top 2 cards."""
    n = _water(ctx)
    if n and await ctx.ask_yes_no(f"Do {20 * n} more damage and discard the top 2 cards of your deck?"):
        await ctx.deal_damage(ctx.ability.damage + 20 * n)
        await ctx.discard_cards(ctx.deck_top(2))
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="e4fa39da-bab0-5519-9556-25f1708cb881",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGyaradosEX.Name",
    display_name="M Gyarados-EX",
    searchable_by=["M Gyarados-EX", "MEGA", "EX", "MGyaradosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=115,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    family_id=130,
    abilities=[
        Attack(
            title="Blast Geyser",
            game_text="You may do 20 more damage for each Water Energy attached to this Pok\u00e9mon. If you do, discard the top 2 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=_blast_geyser,
        ),
    ],
)