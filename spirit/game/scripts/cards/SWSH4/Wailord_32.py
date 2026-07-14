from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def water_veil(ctx):
    """Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it."""
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    await ctx.cure_all_conditions(ctx.source)

card = PokemonCardDef(
    guid="7029b0f0-63c1-5d4d-99da-3e67d170fd0c",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Ability(
            title="Water Veil",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=water_veil,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 40 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=10,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.WATER), 40, base=10
            ),
        ),
    ],
)