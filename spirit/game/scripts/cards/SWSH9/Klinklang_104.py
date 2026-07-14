from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.effects import is_basic_pokemon


def _protects_own_basics(target, carrier):
    return target.owning_player_id == carrier.owning_player_id and is_basic_pokemon(target)

card = PokemonCardDef(
    guid="8dcba8aa-fbbb-5e73-a3ad-5501d3c8f8e5",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Gear Wall",
            game_text="Your Basic Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_protects_own_basics),
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(90),
        ),
    ],
)