from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import carrier_pokemon


async def frost_wall(ctx):
    """30. During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Evolution Pokemon."""
    await ctx.deal_damage()
    passive = prevent_damage_when(
        lambda calc, carrier: carrier_pokemon(carrier) is calc.target
        and is_evolution_pokemon(calc.attacker)
    )
    ctx.add_passive_through_opponents_turn(ctx.attacker, passive)


card = PokemonCardDef(
    guid="8ddfec3c-156a-5d10-9ef1-1f2f0691f531",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1", "Gorebyss"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Deflecting Splash",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=frost_wall,
        ),
    ],
)