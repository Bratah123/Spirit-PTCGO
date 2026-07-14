from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_vmax


async def amazing_shield(ctx):
    """180; next turn, prevent all damage done to this Pokemon by VMAX attacks."""
    await ctx.deal_damage()
    shield = prevent_damage_when(
        lambda calc, c: calc.target is c and calc.attacker is not None
        and is_pokemon_vmax(calc.attacker.archetype_id)
    )
    ctx.add_passive_through_opponents_turn(ctx.attacker, shield)


card = PokemonCardDef(
    guid="2137a21d-8c55-54ef-a688-dc8748e37904",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic", "Zamazenta"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=889,
    abilities=[
        Attack(
            title="Metal Armament",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1, target="self",
                prompt="Choose a basic Energy card from your discard pile to attach to this Pok\u00e9mon.",
            ),
        ),
        Attack(
            title="Amazing Shield",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=180,
            effect=amazing_shield,
        ),
    ],
)