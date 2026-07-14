from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.support_common import attach_from_discard

_ENERGY_ON_SELF = count_energy("self")


def is_fire_energy_card(card):
    return is_energy_card(card) and PokemonTypes.FIRE.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def exciting_flame(ctx):
    await ctx.deal_damage()
    total_cost = sum(ctx.ability.cost.values())
    if _ENERGY_ON_SELF(ctx) < total_cost + 3:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(180, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="c87d6fb9-2d20-5cfa-ad8f-532b59c883ea",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=attach_from_discard(predicate=is_fire_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Exciting Flame",
            game_text="If this Pok\u00e9mon has at least 3 extra Energy attached (in addition to this attack's cost), this attack also does 180 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=exciting_flame,
        ),
    ],
)