from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


async def link_blast(ctx):
    """40 if Energy counts match; 10 if they differ."""
    amount = 40 if count_energy("self")(ctx) == count_energy("defender")(ctx) else 10
    await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="59a13542-6036-52e4-8c10-36ad6419364c",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts", "Basic", "Ralts"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=280,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Link Blast",
            game_text="If Ralts and the Defending Pok\u00e9mon have a different amount of Energy attached to them, this attack's base damage is 10 instead of 40.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=link_blast,
        ),
    ],
)
