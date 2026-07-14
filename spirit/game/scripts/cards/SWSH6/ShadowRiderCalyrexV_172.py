from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.effects import is_special_energy


def _is_stadium_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


async def shadow_mist(ctx):
    """10 damage; during your opponent's next turn, they can't play any
    Special Energy or Stadium cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(
        ctx.opponent_id,
        lambda card: is_special_energy(card) or _is_stadium_card(card),
    )


async def astral_barrage(ctx):
    """Choose 2 of your opponent's Pokemon and put 5 damage counters on each."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    chosen = await ctx.choose_cards(
        candidates, 2, prompt="Choose 2 of your opponent's Pokémon"
    )
    for target in chosen:
        await ctx.deal_damage(50, target=target, as_counters=True)


card = PokemonCardDef(
    guid="8a7cf595-4e42-53e2-a0cc-4231602dbaa6",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    display_name="Shadow Rider Calyrex V",
    searchable_by=["Shadow Rider Calyrex V", "Basic", "V", "ShadowRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=172,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=898,
    abilities=[
        Attack(
            title="Shadow Mist",
            game_text="During your opponent's next turn, they can't play any Special Energy or Stadium cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=shadow_mist,
        ),
        Attack(
            title="Astral Barrage",
            game_text="Choose 2 of your opponent's Pok\u00e9mon and put 5 damage counters on each of them.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=astral_barrage,
        ),
    ],
)