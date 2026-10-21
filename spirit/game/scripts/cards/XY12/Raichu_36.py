from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy


async def _spark_bolt(ctx):
    """70; you may discard all Energy attached to this Pokemon for 70 more."""
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no("Discard all Energy attached to this Pokémon for 70 more damage?"):
        await ctx.discard_cards(list(energies))
        await ctx.deal_damage(140)
    else:
        await ctx.deal_damage(70)


card = PokemonCardDef(
    guid="475bad35-5a3a-5d1c-a0ad-df30df6e99d9",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard(predicate=is_lightning_energy),
        ),
        Attack(
            title="Spark Bolt",
            game_text="You may discard all Energy attached to this Pok\u00e9mon. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=_spark_bolt,
        ),
    ],
)