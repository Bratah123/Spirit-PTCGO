from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.attacks_common import lock_all_attacks

async def frost_wall(ctx):
    """30. During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Evolution Pokemon."""
    await ctx.deal_damage()
    passive = prevent_damage_when(
        lambda calc, carrier: carrier_pokemon(carrier) is calc.target
        and is_evolution_pokemon(calc.attacker)
    )
    ctx.add_passive_through_opponents_turn(ctx.attacker, passive)

async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="c66198bb-0758-5ea0-88e1-5a44c749b9f6",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 2", "Aurorus"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Attack(
            title="Frost Wall",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=frost_wall,
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=_freeze_shock,
        ),
    ],
)
