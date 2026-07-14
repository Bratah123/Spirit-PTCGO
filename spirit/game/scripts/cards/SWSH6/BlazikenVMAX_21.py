from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_energy_card


async def max_blaze(ctx):
    """130 damage. Choose up to 2 Benched Rapid Strike Pokémon and attach a
    discard-pile Energy card to each of them."""
    await ctx.deal_damage()
    bench = [p for p in ctx.my_bench() if "Rapid Strike" in subtypes_for(p.archetype_id)]
    if not bench:
        return
    targets = await ctx.choose_cards(
        bench, min(2, len(bench)), minimum=0,
        prompt="Choose up to 2 of your Benched Rapid Strike Pokémon",
    )
    for target in targets:
        energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not energies:
            break
        picks = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy card to attach",
        )
        if not picks:
            continue
        if target.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(target.entity_id)
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="25ed89e9-39a3-5bab-83e4-16f101a043c1",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenVMAX.Name",
    display_name="Blaziken VMAX",
    searchable_by=["Blaziken VMAX", "VMAX", "Rapid Strike", "BlazikenVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=21,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenV.Name",
    family_id=257,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Max Blaze",
            game_text="Choose up to 2 of your Benched Rapid Strike Pokémon and attach an Energy card from your discard pile to each of them.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=max_blaze,
        ),
    ],
)
