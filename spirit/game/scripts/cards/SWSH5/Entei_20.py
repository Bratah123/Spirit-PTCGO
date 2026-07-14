from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import energy_provides_type


async def heat_dash(ctx):
    await ctx.deal_damage()
    fire_energy = [c for c in ctx.hand() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    if not fire_energy:
        return
    if await ctx.ask_yes_no(
        "Attach a Fire Energy card from your hand to this Pokémon?"
    ):
        picks = await ctx.choose_cards(
            fire_energy, 1, prompt="Choose a Fire Energy card to attach"
        )
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="fcee5e8d-5d17-5574-826e-db745ca23697",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Heat Dash",
            game_text="You may attach a Fire Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=heat_dash,
        ),
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)