from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def bright_flame(ctx):
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Bright Flame"))[0]
    if not heads:
        await ctx.discard_energy_from(ctx.attacker, 2)


card = PokemonCardDef(
    guid="7ede9024-e3c6-5ba6-8d74-b92b700c48fd",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Cinderace"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Fire Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=attach_from_discard(predicate=_is_fire_energy, count=1, target="self"),
        ),
        Attack(
            title="Bright Flame",
            game_text="Flip a coin. If tails, discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=bright_flame,
        ),
    ],
)
