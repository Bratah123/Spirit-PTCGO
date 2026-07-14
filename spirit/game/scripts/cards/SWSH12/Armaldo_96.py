from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def reaping_claw(ctx):
    defender = ctx.defender
    if defender is not None and defender.get_attribute(AttrID.HP, 0) <= 100:
        await ctx.knock_out(defender)


card = PokemonCardDef(
    guid="fce33d95-a617-5a10-b332-2f32a0d09033",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name",
    display_name="Armaldo",
    searchable_by=["Armaldo", "Stage 2", "Armaldo"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Reaping Claw",
            game_text="If your opponent's Active Pok\u00e9mon has 100 HP or less remaining, it is Knocked Out.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reaping_claw,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)