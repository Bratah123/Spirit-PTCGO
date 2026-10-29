from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.passives_common import apply_own_next_turn_boost


async def feather_dance(ctx):
    """Next turn, Pom-Pom Punch's base damage is 100 (printed 20, so +80)."""
    await apply_own_next_turn_boost(ctx, 80, attack_title="Pom-Pom Punch")


card = PokemonCardDef(
    guid="69d3848d-e1e6-5534-afe4-69d1d8117bf0",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title="Feather Dance",
            game_text="During your next turn, this Pok\u00e9mon's Pom-Pom Punch attack's base damage is 100.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=feather_dance,
        ),
        Attack(
            title="Pom-Pom Punch",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)