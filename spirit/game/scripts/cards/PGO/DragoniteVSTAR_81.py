from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import look_top_attach_energy


def _is_water_or_lightning_energy(card):
    return (
        energy_provides_type(card, PokemonTypes.WATER.value)
        or energy_provides_type(card, PokemonTypes.LIGHTNING.value)
    )


async def giga_impact(ctx):
    """250 damage. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


draconic_star = look_top_attach_energy(12, predicate=_is_water_or_lightning_energy)

card = PokemonCardDef(
    guid="a56db22e-4b35-56f3-ba94-732e42148400",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteVSTAR.Name",
    display_name="Dragonite VSTAR",
    searchable_by=["Dragonite VSTAR", "VSTAR", "DragoniteVSTAR"],
    subtypes=["VSTAR"],
    collector_number=81,
    set_code="PGO",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=giga_impact,
        ),
        Attack(
            title="Draconic Star",
            game_text="Look at the top 12 cards of your deck and attach any number of Water or Lightning Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            vstar=True,
            effect=draconic_star,
        ),
    ],
)