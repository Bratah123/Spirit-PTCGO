from spirit.game.card_effects.support_common import heal_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def raging_repeated_strike(ctx):
    """Discard any amount of Energy from your Pokemon; +30 damage per card discarded."""
    energies = [e for p in ctx.my_pokemon_in_play()
                for e in ctx.attached_energies(p)]
    picks = []
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Choose any amount of Energy to discard from your Pokémon.",
        )
    if picks:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(120 + 30 * len(picks))


card = PokemonCardDef(
    guid="65961c5c-6705-536e-bdd2-c6f13f626101",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rapid Strike", "Rillaboom"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=18,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Attack(
            title="Wood Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=heal_attack(30),
        ),
        Attack(
            title="Raging Repeated Strike",
            game_text="Discard any amount of Energy from your Pok\u00e9mon. This attack does 30 more damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=raging_repeated_strike,
        ),
    ],
)