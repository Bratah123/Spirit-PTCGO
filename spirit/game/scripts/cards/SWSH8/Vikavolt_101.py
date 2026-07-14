from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import energy_provides_type


async def electro_blaster(ctx):
    """Discard 2 Lightning Energy from this Pokemon. 200 damage to 1 of your
    opponent's Pokemon (no W/R on Benched)."""
    await ctx.discard_energy_from(
        ctx.attacker, 2,
        predicate=lambda c: energy_provides_type(c, PokemonTypes.LIGHTNING.value),
        prompt="Choose 2 Lightning Energy to discard from this Pokémon",
    )
    await snipe_attack(200, pool="any", count=1)(ctx)


card = PokemonCardDef(
    guid="69a5225e-f2e2-589b-9c02-ba9b2a8640a4",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=101,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title="Electro Blaster",
            game_text="Discard 2 Lightning Energy from this Pokémon. This attack does 200 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            effect=electro_blaster,
        ),
    ],
)
