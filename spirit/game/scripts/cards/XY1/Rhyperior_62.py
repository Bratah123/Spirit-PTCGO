from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, count_energy, lock_all_attacks


async def _rock_wrecker(ctx):
    """130, not affected by Weakness or Resistance; this Pokemon can't attack
    during your next turn."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="c7853afb-a3e6-53c2-af16-bb2024f69964",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Rock Black",
            game_text="Flip a coin for each Fighting Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy('self', energy_type=PokemonTypes.FIGHTING), per_heads=50),
        ),
        Attack(
            title="Rock Wrecker",
            game_text="This attack's damage isn't affected by Weakness or Resistance. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=_rock_wrecker,
        ),
    ],
)