from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, snipe_attack
from spirit.game.card_effects.pokemon import energy_provides_type


_volt_snipe = snipe_attack(100, pool='any')


async def _volt_bolt(ctx):
    """Discard all Lightning Energy from this Pokémon, then 100 to 1 of the
    opponent's Pokémon."""
    lightning = [e for e in ctx.attached_energies(ctx.attacker)
                 if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    if lightning:
        await ctx.discard_cards(lightning)
    await _volt_snipe(ctx)


card = PokemonCardDef(
    guid="4ddfcac0-4f28-5d26-8841-60d8d7a7eb53",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouEX.Name",
    display_name="Raikou-EX",
    searchable_by=["Raikou-EX", "Basic", "EX", "RaikouEX"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Volt Bolt",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=_volt_bolt,
        ),
    ],
)