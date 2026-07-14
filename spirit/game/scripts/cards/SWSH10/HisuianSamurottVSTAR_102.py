from spirit.game.card_effects.attacks_common import bonus_if, has_damage
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def moon_cleave_star(ctx):
    """VSTAR Power: you may put 4 damage counters on 1 of your opponent's Pokemon."""
    if not await ctx.ask_yes_no("Put 4 damage counters on 1 of your opponent's Pokémon?"):
        return
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(40, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="1eef51e4-cb3f-598c-a676-381c64aa7200",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottVSTAR.Name",
    display_name="Hisuian Samurott VSTAR",
    searchable_by=["Hisuian Samurott VSTAR", "VSTAR", "HisuianSamurottVSTAR"],
    subtypes=["VSTAR"],
    collector_number=102,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottV.Name",
    family_id=503,
    abilities=[
        Ability(
            title="Moon Cleave Star",
            game_text="During your turn, you may put 4 damage counters on 1 of your opponent's Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=moon_cleave_star,
        ),
        Attack(
            title="Merciless Blade",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 110 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=110,
            damage_operator="+",
            effect=bonus_if(has_damage(), 110),
        ),
    ],
)
