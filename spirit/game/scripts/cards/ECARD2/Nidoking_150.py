from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached,
)


async def rolling_thunder(ctx):
    """50 to Active; flip: heads 10 to each opp bench, tails 10 to each own bench."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Rolling Thunder")
    heads = bool(results and results[0])
    if heads:
        for poke in ctx.opponent_bench():
            await ctx.deal_damage(10, target=poke, apply_modifiers=False)
    else:
        for poke in ctx.my_bench():
            await ctx.deal_damage(10, target=poke, apply_modifiers=False)


card = PokemonCardDef(
    guid="67748930-6103-5622-9f25-e82c0afea1e5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="ECARD2",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Grass, Lightning, or Fire basic Energy card from your hand to Nidoking, Nidoking's type (color) becomes the same as that Energy card type until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.GRASS, PokemonTypes.LIGHTNING, PokemonTypes.FIRE,
            ),
        ),
        Attack(
            title="Poison Horn",
            game_text="The Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Rolling Thunder",
            game_text="Flip a coin, If heads, this attack does 10 damage to each of your opponent's Benched Pokémon. If tails, this attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=rolling_thunder,
        ),
    ],
)
