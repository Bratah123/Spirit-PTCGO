from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


async def rocket_poison(ctx):
    """Your opponent's Active Pokémon is now Poisoned. If this Pokémon
    evolved from Skrelp during this turn, put 8 damage counters instead of 1."""
    counters = 8 if _evolved_this_turn(ctx) else 1
    await ctx.apply_special_condition(
        ctx.defender, SpecialConditions.POISONED, poison_counters=counters)


card = PokemonCardDef(
    guid="5b049f74-2e13-5394-bb2d-7ea832d36233",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1", "Dragalge"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Attack(
            title="Rocket Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. If this Pok\u00e9mon evolved from Skrelp during this turn, put 8 damage counters on that Pok\u00e9mon instead of 1 during Pok\u00e9mon Checkup.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=rocket_poison,
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)