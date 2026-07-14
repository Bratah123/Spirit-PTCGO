from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive


async def phantom_force(ctx):
    """120 damage; put 3 damage counters on the opponent's Benched Pokemon
    in any way you like."""
    await ctx.deal_damage()
    await ctx.place_damage_counters(3, candidates=ctx.opponent_bench())


card = PokemonCardDef(
    guid="b48923cd-2056-598f-b21b-5b0136d13792",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Dragapult"],
    subtypes=["Stage 2"],
    collector_number=91,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Ability(
            title="Infiltrator",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Infiltrator"),
        ),
        Attack(
            title="Phantom Force",
            game_text="Put 3 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=phantom_force,
        ),
    ],
)