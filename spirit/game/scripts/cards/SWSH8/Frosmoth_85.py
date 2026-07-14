from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def blizzard_loop(ctx):
    """160 damage, then put all Energy attached to this Pokemon into your
    hand."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.put_in_hand(energies, reveal=False)


card = PokemonCardDef(
    guid="359c4f40-0f78-5596-8d7d-15eea7b13359",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1", "Frosmoth"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Blizzard Loop",
            game_text="Put all Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=blizzard_loop,
        ),
    ],
)
