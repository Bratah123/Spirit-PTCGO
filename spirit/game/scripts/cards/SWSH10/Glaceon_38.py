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
    guid="0cdcae9c-a299-5e7d-bac0-240e229456e9",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Glaceon"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Frost Wall",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=frost_wall,
        ),
        Attack(
            title="Ice Blast",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)