"""STUB: effect not implemented — do not guess mechanics.
Diancie-EX (XY10 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive, is_in_active_spot


def _sparkle_veil_protects(target, carrier):
    return target.owning_player_id == carrier.owning_player_id and is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="f5909e1a-2e35-59f0-b1d4-bdb4fcbcef7c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name",
    display_name="Diancie-EX",
    searchable_by=["Diancie-EX", "Basic", "EX", "DiancieEX"],
    subtypes=["Basic", "EX"],
    collector_number=72,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Ability(
            title="Sparkle Veil",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 30 (after applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            passive=takes_less_passive(30, protects=_sparkle_veil_protects),
        ),
        Attack(
            title="Wonder Stage",
            game_text="If there is any Stadium card in play, this attack does 50 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)