from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import full_stack


async def dragon_launcher(ctx):
    """Discard up to (opponent's Pokémon in play) Benched Dreepy; for each
    discarded, choose a different opposing Pokémon and do 100 raw damage."""
    dreepy = [p for p in ctx.my_bench()
              if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Dreepy"]
    opponents = ctx.opponent_pokemon_in_play()
    max_discard = min(len(dreepy), len(opponents))
    if max_discard <= 0:
        return
    picks = await ctx.choose_cards(
        dreepy, max_discard, minimum=0,
        prompt=f"Choose up to {max_discard} Dreepy to discard from your Bench",
    )
    if not picks:
        return
    for pokemon in picks:
        await ctx.discard_cards(full_stack(pokemon))
    remaining_targets = list(opponents)
    for _ in picks:
        if not remaining_targets:
            break
        target = await ctx.choose_pokemon(
            remaining_targets, "Choose 1 of your opponent's Pokémon to damage"
        )
        if target is None:
            break
        await ctx.deal_damage(100, target=target, apply_modifiers=False)
        remaining_targets.remove(target)


card = PokemonCardDef(
    guid="00fe26b0-03f9-5898-b0e5-34d69140da53",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Dragapult"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Dragon Launcher",
            game_text="Discard a number of your Benched Dreepy up to the number of your opponent's Pokémon in play. Then, for each Dreepy you discarded in this way, choose 1 of your opponent's Pokémon and do 100 damage to it. You can't choose the same Pokémon more than once. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=dragon_launcher,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
