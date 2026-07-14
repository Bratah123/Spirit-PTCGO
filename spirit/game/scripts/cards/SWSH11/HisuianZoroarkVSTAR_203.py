from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per


async def phantom_star(ctx):
    """VSTAR Power: you may discard your hand and draw 7 cards."""
    if not await ctx.ask_yes_no("Discard your hand and draw 7 cards?"):
        return
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(7)


def _damaged_own_pokemon(ctx):
    return sum(
        1 for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.HP, ctx.max_hp(p)) < ctx.max_hp(p)
    )


card = PokemonCardDef(
    guid="0c8dc18c-cca2-5814-accf-05426543dc61",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkVSTAR.Name",
    display_name="Hisuian Zoroark VSTAR",
    searchable_by=["Hisuian Zoroark VSTAR", "VSTAR", "HisuianZoroarkVSTAR"],
    subtypes=["VSTAR"],
    collector_number=203,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkV.Name",
    family_id=571,
    abilities=[
        Ability(
            title="Phantom Star",
            game_text="During your turn, you may discard your hand and draw 7 cards. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=phantom_star,
        ),
        Attack(
            title="Ticking Curse",
            game_text="This attack does 50 damage for each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(_damaged_own_pokemon, 50),
        ),
    ],
)