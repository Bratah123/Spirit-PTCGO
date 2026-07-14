from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import prevent_damage_when


async def untamed_shout(ctx):
    if not await ctx.ask_yes_no(
            "Put 3 damage counters on 1 of your opponent's Pokémon?"):
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(30, target=target, as_counters=True)


def _attacker_is_basic(calc, carrier) -> bool:
    attacker = calc.attacker
    return attacker is not None \
        and attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


async def obstruct(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_attacker_is_basic))

card = PokemonCardDef(
    guid="fda319f9-4e2c-5630-bc12-3610a9617aa0",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=119,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Untamed Shout",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=untamed_shout,
        ),
        Attack(
            title="Obstruct",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=obstruct,
        ),
    ],
)