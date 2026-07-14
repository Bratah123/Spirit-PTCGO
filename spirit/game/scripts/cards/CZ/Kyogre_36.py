from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy


def _is_water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


async def dynamic_wave(ctx):
    """Put 3 Energy attached to this Pokemon into hand; 180 to 1 of opponent's Pokemon."""
    attached = ctx.attached_energies(ctx.attacker)
    if attached:
        picks = await ctx.choose_cards(
            attached, 3,
            prompt="Choose 3 Energy attached to this Pokémon to put into your hand",
        )
        await ctx.put_in_hand(picks, reveal=False)
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(), "Choose 1 of your opponent's Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(180, target=target)


card = PokemonCardDef(
    guid="32672775-3b7e-5d18-a914-d5eaced8cdc9",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Wave Summoning",
            game_text="Search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=_is_water_energy, count=1, to_self=True),
        ),
        Attack(
            title="Dynamic Wave",
            game_text="Put 3 Energy attached to this Pok\u00e9mon into your hand. This attack does 180 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            effect=dynamic_wave,
        ),
    ],
)