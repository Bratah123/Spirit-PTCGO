from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def _aurora_loop(ctx):
    await ctx.deal_damage()
    water_energies = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.WATER.value)
    ]
    picks = await ctx.choose_cards(
        water_energies, 2,
        prompt="Choose 2 Water Energy to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="1bf418ff-c175-5f25-b650-a956c62cc59c",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aurora Loop",
            game_text="Put 2 Water Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_aurora_loop,
        ),
    ],
)