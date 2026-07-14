from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def lost_headbutt(ctx):
    """50. Put an Energy attached to your opponent's Active Pokemon in the Lost Zone."""
    await ctx.deal_damage()
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    energies = ctx.attached_energies(target)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy to put in the Lost Zone",
    )
    if picks:
        await ctx.move_to_lost_zone(picks)


card = PokemonCardDef(
    guid="f86d0c9b-7034-5b93-bc19-f06cf5e58e10",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Lost Headbutt",
            game_text="Put an Energy attached to your opponent's Active Pokémon in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=lost_headbutt,
        ),
        Attack(
            title="Superpowered Horns",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)
