from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _rock_shower(ctx):
    """Flip 3 coins: 20 times heads to each of your opponent's Pokemon."""
    results = await ctx.flip_coins(3, ctx.ability.title) or []
    n = sum(1 for r in results if r)
    if n:
        for p in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(20 * n, target=p)


card = PokemonCardDef(
    guid="f1571194-89da-5c69-b11e-5ee52651697a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Rock Shower",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=_rock_shower,
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)