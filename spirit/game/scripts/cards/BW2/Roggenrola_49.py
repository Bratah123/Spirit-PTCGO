from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when


async def harden(ctx):
    """During opponent's next turn, prevent attack damage of 40 or less."""
    ctx.add_passive_through_opponents_turn(
        ctx.source, prevent_damage_when(lambda calc, c: calc.amount <= 40)
    )


card = PokemonCardDef(
    guid="aa39d889-d160-5119-ac94-88bf2847f022",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 40 or less.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=harden,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
