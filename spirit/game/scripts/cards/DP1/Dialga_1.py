"""STUB: effect not implemented — do not guess mechanics.
Dialga (DP1 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import flash_cannon_devolve


card = PokemonCardDef(
    guid="6d4b6afc-4d19-5203-a385-664cd87bfd84",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Time Bellow",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=draw_attack(1),
        ),
        Attack(
            title="Flash Cannon",
            game_text="You may return all Energy cards attached to Dialga to your hand. If you do, remove the highest Stage Evolution card from the Defending Pok\u00e9mon and shuffle that card into your opponent's deck.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flash_cannon_devolve(),
        ),
    ],
)