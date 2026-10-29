from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type

async def grass_munch(ctx):
    """10 damage, then discard a Grass Energy from the opponent's Active."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1, predicate=lambda c: energy_provides_type(c, PokemonTypes.GRASS.value),
        prompt="Choose a Grass Energy to discard from the Defending Pokémon")

card = PokemonCardDef(
    guid="0cd6a391-3dec-5fa7-b860-db146ab05157",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic", "Salandit"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Grass Fire",
            game_text="Discard a Grass Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=grass_munch,
        ),
    ],
)