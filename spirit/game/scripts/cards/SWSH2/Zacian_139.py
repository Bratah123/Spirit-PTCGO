from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_metal_energy_card


async def smashing_edge(ctx):
    """120 damage. Flip a coin. If tails, discard 2 Energy from this Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Smashing Edge"))[0]
    if not heads:
        await ctx.discard_energy_from(
            ctx.attacker, 2, prompt="Discard 2 Energy from this Pokémon")


card = PokemonCardDef(
    guid="5f77495a-791f-5508-8bcc-1f1917aed094",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Attach a Metal Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(predicate=is_metal_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Smashing Edge",
            game_text="Flip a coin. If tails, discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=smashing_edge,
        ),
    ],
)