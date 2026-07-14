from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def dreaming_tone_watch(ctx):
    """During opponent's next turn, if an Energy card is attached to the
    Defending Pokémon from their hand, that Pokémon becomes Asleep."""
    if not ctx.attack_used_last_turn(title="Dreaming Tone", entity=ctx.source):
        return
    if ctx.attaching_player_id != ctx.opponent_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None or receiver is not ctx.opponent_active():
        return
    await ctx.apply_special_condition(receiver, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="eda95826-9622-5b5a-82fb-167d6a136d6a",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=358,
    abilities=[
        Attack(
            title="Dreaming Tone",
            game_text="During your opponent's next turn, if an Energy card is attached to the Defending Pok\u00e9mon from your opponent's hand, that Pok\u00e9mon will be Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
        ),
        Ability(
            title="Dreaming Tone",
            game_text="During your opponent's next turn, if an Energy card is attached to the Defending Pok\u00e9mon from your opponent's hand, that Pok\u00e9mon will be Asleep.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=dreaming_tone_watch,
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)