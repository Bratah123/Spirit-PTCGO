from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost


async def _work_up(ctx):
    """During your next turn, this Pokemon's attacks do 20 more damage to the opponent's Active."""
    await apply_own_next_turn_boost(ctx, 20)


card = PokemonCardDef(
    guid="e73ae66a-7e0d-51d2-9224-bc1bda0a3622",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic", "Lillipup"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Work Up",
            game_text="During your next turn, this Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_work_up,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)