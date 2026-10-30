from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import healing_block_passive
from spirit.game.session.passives import carrier_pokemon


async def _moongeist_beam(ctx):
    """120; the Defending Pokemon can't be healed during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and defender.parent is not None and not ctx.effects_blocked(defender):
        ctx.add_passive_through_opponents_turn(
            defender, healing_block_passive(lambda t, c: t is carrier_pokemon(c)))


card = PokemonCardDef(
    guid="5703b5e1-33d3-5d49-9352-caf72c3be070",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=72,
    abilities=[
        Attack(
            title="Sludge Shock",
            game_text="The Defending Pok\u00e9mon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=_moongeist_beam,
        ),
    ],
)