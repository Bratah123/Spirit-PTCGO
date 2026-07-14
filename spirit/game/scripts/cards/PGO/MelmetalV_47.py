from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card


async def _arm_charge(ctx):
    await ctx.deal_damage()
    energies = [c for c in ctx.hand() if is_metal_energy_card(c)]
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Attach a Metal Energy card from your hand to this Pokémon?"
    ):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Metal Energy card to attach"
    )
    if picked:
        await ctx.attach_energy(picked[0], ctx.attacker)


card = PokemonCardDef(
    guid="b77472f2-c926-5367-b469-8e680bc0e647",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalV.Name",
    display_name="Melmetal V",
    searchable_by=["Melmetal V", "Basic", "V", "MelmetalV"],
    subtypes=["Basic", "V"],
    collector_number=47,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=809,
    abilities=[
        Attack(
            title="Arm Charge",
            game_text="You may attach a Metal Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            effect=_arm_charge,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.METAL: 3},
            damage=140,
        ),
    ],
)