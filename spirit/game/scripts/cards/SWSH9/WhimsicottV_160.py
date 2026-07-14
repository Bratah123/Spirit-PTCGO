from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.session.effects import is_basic_pokemon


async def fluff_gets_in_the_way(ctx):
    """20. If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        lock_defender_attacks(ctx)

card = PokemonCardDef(
    guid="8862b0c1-8db9-51fe-a01a-74d8c058ea3c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottV.Name",
    display_name="Whimsicott V",
    searchable_by=["Whimsicott V", "Basic", "V", "WhimsicottV"],
    subtypes=["Basic", "V"],
    collector_number=160,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=547,
    abilities=[
        Attack(
            title="Fluff Gets in the Way",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=fluff_gets_in_the_way,
        ),
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)