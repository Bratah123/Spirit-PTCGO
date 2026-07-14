from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, snipe_attack

_magical_fire_base = snipe_attack(120, also_base=True)


async def magical_fire(ctx):
    """Put 2 Energy attached to this Pokemon in the Lost Zone. Also does 120 damage to 1 of your opponent's Benched Pokemon (no W/R)."""
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        picks = await ctx.choose_cards(
            energies, min(2, len(energies)),
            prompt="Put 2 Energy attached to this Pokémon in the Lost Zone",
        )
        if picks:
            await ctx.move_to_lost_zone(picks)
    await _magical_fire_base(ctx)


card = PokemonCardDef(
    guid="25fa5714-a233-5c79-83d6-3850dc7ae95e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxV.Name",
    display_name="Delphox V",
    searchable_by=["Delphox V", "Basic", "V", "DelphoxV"],
    subtypes=["Basic", "V"],
    collector_number=27,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=655,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Magical Fire",
            game_text="Put 2 Energy attached to this Pokémon in the Lost Zone. This attack also does 120 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=magical_fire,
        ),
    ],
)
