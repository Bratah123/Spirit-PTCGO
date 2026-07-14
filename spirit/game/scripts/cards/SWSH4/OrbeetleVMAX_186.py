from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def eerie_beam(ctx):
    """Put 1 damage counter on each of your opponent's Pokemon."""
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=pokemon, as_counters=True)


card = PokemonCardDef(
    guid="e6f2053a-06c1-5223-a47b-b59a87d1a325",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleVMAX.Name",
    display_name="Orbeetle VMAX",
    searchable_by=["Orbeetle VMAX", "VMAX", "OrbeetleVMAX"],
    subtypes=["VMAX"],
    collector_number=186,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    family_id=826,
    abilities=[
        Ability(
            title="Eerie Beam",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=eerie_beam,
        ),
        Attack(
            title="G-Max Wave",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=50),
        ),
    ],
)