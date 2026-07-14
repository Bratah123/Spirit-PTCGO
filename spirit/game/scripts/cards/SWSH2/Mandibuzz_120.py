from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage


async def blindside(ctx):
    """100 damage to 1 of the opponent's Pokemon with any damage counters on it; no W/R on the Bench."""
    candidates = [p for p in ctx.opponent_pokemon_in_play()
                  if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon that has damage counters on it")
    if target is not None:
        active = ctx.opponent_active()
        await ctx.deal_damage(100, target=target, apply_modifiers=(target is active))

card = PokemonCardDef(
    guid="4a93665e-625f-5dac-a813-34831aea0c75",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1", "Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Bone Rush",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
        Attack(
            title="Blindside",
            game_text="This attack does 100 damage to 1 of your opponent's Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=blindside,
        ),
    ],
)